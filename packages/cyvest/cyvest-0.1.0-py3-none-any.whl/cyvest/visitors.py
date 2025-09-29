from __future__ import annotations

import copy
from abc import ABC, abstractmethod
from typing import Any

from logurich import logger

from .check_tree import CheckTree
from .models import (
    Container,
    Enrichment,
    Level,
    Model,
    Observable,
    ObsType,
    ResultCheck,
    Scope,
    ThreatIntel,
    get_level_from_score,
)
from .observable_registry import ObservableRegistry
from .report_render import markdown_summary, stdout_from_json
from .report_serialization import reduce_report_json, report_to_json


class Visitor(ABC):
    def __init__(self, *, graph: bool = False) -> None:
        super().__init__()
        self.graph = graph
        self._stats = {}

    @property
    def stats(self):
        return copy.deepcopy(self._stats)

    def init_stat(self, key: str, value: int = 0) -> None:
        self._stats[key] = value

    def increment_stat(self, key: str, value: int = 1) -> None:
        self._stats[key] += value

    def decrement_stat(self, key: str, value: int = 1) -> None:
        self._stats[key] -= value

    def reduce_stats(self, stats: dict) -> dict:
        for k, v in self._stats.items():
            if not isinstance(v, int):
                raise Exception("Reduce Stats can reduce only integers")
            if stats.get(k):
                stats[k] += v
            else:
                stats[k] = v
        return stats

    @abstractmethod
    def visit_threat_intel(self, threat_intel: ThreatIntel) -> ThreatIntel:
        """Method that returns models"""
        raise NotImplementedError("missing method check")

    @abstractmethod
    def visit_observable(self, observable: Observable) -> Observable:
        """Method that visit an observable"""
        raise NotImplementedError("missing method visit_observable")

    @abstractmethod
    def visit_result_check(self, result_check: ResultCheck) -> ResultCheck:
        """Method that visit a result entry"""
        raise NotImplementedError("missing method visit_result_check")

    @abstractmethod
    def visit_container(self, container: Container) -> Container:
        """Method that visit a result entry"""
        raise NotImplementedError("missing method visit_container")

    @abstractmethod
    def visit_enrichment(self, enrichment: Enrichment) -> Enrichment:
        """Method that visit an enrichment"""
        raise NotImplementedError("missing method visit_enrichment")

    @abstractmethod
    def to_json(self):
        """Method that convert the object to json"""
        raise NotImplementedError("missing method to_json")

    @abstractmethod
    def get_check(self, path: str):
        """Method that convert the object to json"""
        raise NotImplementedError("missing method get_check")


class Report(Visitor):
    map_stats_suspicious = {
        ObsType.IP.name: "ips",
        ObsType.URL.name: "urls",
        ObsType.DOMAIN.name: "domains",
        ObsType.FILE.name: "files",
        Scope.FULL.name: "full",
        Scope.HEADER.name: "header",
        Scope.BODY.name: "body",
        Scope.ATTACHMENT.name: "attachment",
        "threat_intel": "threat_intels",
    }

    def __init__(
        self,
        json_structure: dict[str, Any] | None = None,
        linked_reports: dict[str, Report] | None = None,
        *,
        graph: bool = False,
    ) -> None:
        if linked_reports is None:
            linked_reports = {}
        super().__init__(graph=graph)
        payload = copy.deepcopy(json_structure) if json_structure is not None else self.default_payload()
        self.json = payload
        self.linked_reports = linked_reports
        self._seen_stats = {}
        self.tree = CheckTree()
        self.observable_registry = ObservableRegistry()
        self.observables = self.observable_registry._observables
        self.enrichments = []
        self.global_score = 0.0
        self.global_level = get_level_from_score(self.global_score) or Level.INFO
        self.annotations: list[dict[str, str]] = []
        # init statistics
        for type_data, key in Report.map_stats_suspicious.items():
            self.init_stat(key)
            for level in Level:
                stat_name = self._get_stat(type_data, level)
                if stat_name is not None:
                    self.init_stat(stat_name)

    @staticmethod
    def default_payload() -> dict[str, Any]:
        return {"checks": {}, "stats": {}, "data": {"header": {}}, "graph": []}

    def __getitem__(self, key):
        return self.json[key]

    def _get_stat(self, type_data: str, level: Level) -> str:
        stat_name = Report.map_stats_suspicious.get(type_data)
        if stat_name is None:
            return None
        suffix = ""
        if level <= Level.NONE:
            return None
        if level >= Level.SUSPICIOUS:
            suffix = f"_{level.name}"
        return f"{stat_name}{suffix}".lower()

    def get_dot_path(self, obj, path):
        s_path = path.split(".")
        struct = obj
        for p in s_path[:-1]:
            struct.setdefault(p, {})
        return struct

    def get(self, path: str, default: Any = None) -> Any:
        return self.json.get(path, default)

    def get_check(self, path: str) -> Any:
        node = self.tree.get(path)
        if isinstance(node, ResultCheck):
            return node
        return None

    def get_observable_per_type(self, type: ObsType) -> list[Observable]:
        return [obs for obs in self.observable_registry.values() if obs.obs_type == type]

    def increment_stat(self, full_key: str, type_data: str, level: Level, model: Model) -> bool:
        stat_name = self._get_stat(type_data, level)
        default_stat_name = self._get_stat(type_data, Level.INFO)
        if stat_name is None:
            return False
        if self._seen_stats.get(full_key):
            # Update
            old_level = self._seen_stats.get(full_key)
            old_stat_name = self._get_stat(type_data, old_level)
            if stat_name and old_stat_name != stat_name and level > old_level:
                self._seen_stats[full_key] = level
                logger.debug(
                    "{}: update stat {} -> {} - default: {} (gen by: {})",
                    full_key,
                    old_stat_name,
                    stat_name,
                    default_stat_name,
                    model.generated_by,
                )
                if old_stat_name != default_stat_name:
                    super().decrement_stat(old_stat_name)
                if stat_name != default_stat_name:
                    super().increment_stat(stat_name)
        else:
            # New
            logger.debug(
                "{}: add stat {} - default: {} (gen by: {})", full_key, stat_name, default_stat_name, model.generated_by
            )
            if stat_name:
                super().increment_stat(stat_name)
            if stat_name != default_stat_name:
                super().increment_stat(default_stat_name)
            self._seen_stats[full_key] = level
        return True

    def get_linked_reports(self, sha256_file: str) -> Report:
        return self.linked_reports.get(sha256_file)

    def is_whitelisted(self, type: ObsType, value: str) -> bool:
        full_key = f"{type.name}.{value}"
        observable = self.observable_registry.get(full_key)
        return bool(observable and observable.whitelisted)

    def add_annotation(self, name: str, message: str) -> list[dict[str, str]]:
        annotation = {"name": name, "message": message}
        self.annotations.append(annotation)
        return self.annotations

    def has_annotations(self) -> bool:
        return bool(self.annotations)

    def visit_threat_intel(self, threat_intel: ThreatIntel) -> ThreatIntel:
        full_key = threat_intel.full_key
        # Statistic
        self.increment_stat(full_key, "threat_intel", threat_intel.level, threat_intel)
        return threat_intel

    def visit_result_check(self, result_check: ResultCheck) -> ResultCheck:
        full_key = result_check.full_key
        self.increment_stat(full_key, result_check.scope.name, result_check.level, result_check)
        rc = self.tree.integrate_result_check(result_check)
        logger.debug("Integrated ResultCheck [{}] -> score {}", full_key, rc.score)
        self.global_score = round(self.tree.total_score(), 2)
        self.global_level = self.tree.highest_level()
        return rc

    def visit_container(self, container: Container) -> Container:
        integrated = self.tree.integrate_container(container)
        self.global_score = round(self.tree.total_score(), 2)
        self.global_level = self.tree.highest_level()
        return integrated

    def visit_observable(self, observable: Observable) -> Observable:
        full_key = f"{observable.obs_type.name}.{observable.obs_value}"
        self.increment_stat(full_key, observable.obs_type.name, observable.level, observable)
        ref = self.observable_registry.upsert(observable)
        if self.is_whitelisted(ref.obs_type, ref.obs_value):
            ref.whitelisted = True
        return ref

    def visit_enrichment(self, enrichment: Enrichment) -> Enrichment:
        enrichment.ref_struct[enrichment.key] = enrichment.data
        self.enrichments.append(enrichment)
        return enrichment

    def to_json(self) -> dict[str, Any]:
        return report_to_json(self)

    def to_stdout_from_json(self, json_data: dict[str, Any]) -> None:
        stdout_from_json(self, json_data)

    def reduce_json_report(self, json_report: dict[str, Any]) -> dict[str, Any]:
        return reduce_report_json(json_report)

    def to_markdown_summary(self, json_data: dict[str, Any], exclude_checks: list[str] | None = None) -> str:
        return markdown_summary(json_data, exclude_checks=exclude_checks)


class Action(Visitor):
    """Minimal visitor that records remediation ideas.

    Projects are encouraged to subclass this visitor and override the
    ``visit_*`` methods to trigger concrete actions (ticketing, EDR tasks,
    notifications, ...). The default implementation keeps things simple by
    logging observables or threat intelligence above a configurable level.
    """

    def __init__(self, *, level_threshold: Level = Level.SUSPICIOUS, graph: bool = False) -> None:
        super().__init__(graph=graph)
        self.level_threshold = level_threshold
        self.actions: list[dict[str, Any]] = []

    def record_action(
        self,
        *,
        name: str,
        description: str,
        impact: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        action = {
            "name": name,
            "description": description,
            "impact": impact,
            "context": context or {},
        }
        logger.info("[ACTION] {} -> {}", name, description)
        self.actions.append(action)
        return action

    def visit_threat_intel(self, threat_intel: ThreatIntel) -> ThreatIntel:
        if threat_intel.level >= self.level_threshold:
            desc = f"{threat_intel.obs_type.name} {threat_intel.obs_value} flagged as {threat_intel.level.name}"
            self.record_action(
                name=f"threat_intel::{threat_intel.name}",
                description=desc,
                impact=threat_intel.level.name,
                context={
                    "score": threat_intel.score,
                    "details": threat_intel.details,
                    "extra": threat_intel.extra,
                },
            )
        return threat_intel

    def visit_observable(self, observable: Observable) -> Observable:
        return observable

    def visit_result_check(self, result_check: ResultCheck) -> ResultCheck:
        return result_check

    def visit_container(self, container: Container) -> Container:
        return container

    def visit_enrichment(self, enrichment: Enrichment) -> Enrichment:
        return enrichment

    def to_json(self) -> list[dict[str, Any]]:
        return copy.deepcopy(self.actions)

    def get_check(self, path: str) -> Any:
        return None
