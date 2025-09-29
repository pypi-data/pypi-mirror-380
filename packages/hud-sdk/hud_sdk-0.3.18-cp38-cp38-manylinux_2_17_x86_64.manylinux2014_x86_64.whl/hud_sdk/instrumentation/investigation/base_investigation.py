from typing import Any, Optional

from ...config import config
from ...flow_metrics import FlowMetric
from ...native import RawInvestigation
from ...schemas.investigation import (
    BaseInvestigationContext,
    Investigation,
    InvestigationExceptionInfo,
)
from ..limited_logger import limited_logger
from .investigation_utils import (
    get_investigation_dedup,
    get_investigation_dedup_key,
    get_machine_metrics,
    get_system_info,
    get_total_investigations,
    increase_total_investigations,
    minimize_exception_info_in_place,
)


def finish_base_investigation(
    raw_investigation: RawInvestigation,
    metric: FlowMetric,
) -> Optional[Investigation[Any]]:
    if metric.flow_id is None:
        limited_logger.log("No flow id in metric")
        return None

    if raw_investigation.first_exception is None:
        limited_logger.log("No exception in investigation")
        return None

    if get_total_investigations() >= config.max_investigations:
        limited_logger.log("Max investigations reached")
        return None

    investigation_dedup = get_investigation_dedup()

    if investigation_dedup.get(metric.flow_id) is None:
        investigation_dedup[metric.flow_id] = dict()

    key = get_investigation_dedup_key(raw_investigation.first_exception)
    if investigation_dedup[metric.flow_id].get(key) is None:
        investigation_dedup[metric.flow_id][key] = 0

    if investigation_dedup[metric.flow_id][key] >= config.max_same_investigation:
        limited_logger.log("Max same investigation reached")
        return None

    increase_total_investigations()
    investigation_dedup[metric.flow_id][key] += 1

    return Investigation(
        exceptions=[
            minimize_exception_info_in_place(
                InvestigationExceptionInfo(exception, execution_flow)
            )
            for exception, execution_flow in raw_investigation.exceptions.items()
        ],
        context=BaseInvestigationContext(
            type="base",
            timestamp=raw_investigation.start_time,
            machine_metrics=get_machine_metrics(),
            system_info=get_system_info(),
        ),
        flow_id=metric.flow_id,
    )
