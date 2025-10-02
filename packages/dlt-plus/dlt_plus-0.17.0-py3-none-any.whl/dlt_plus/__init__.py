"""dlt+ is a plugin to OSS `dlt` adding projects, packages a runner and new cli commands."""

from dlt_plus.version import __version__
from dlt_plus import current as _current
from dlt_plus._runner import PipelineRunner as _PipelineRunner
from dlt_plus import destinations
from dlt_plus import sources
from dlt_plus.transformations import transformation
from dlt_plus.common.license import self_issue_trial_license

current = _current
runner = _PipelineRunner


__all__ = [
    "__version__",
    "current",
    "runner",
    "destinations",
    "sources",
    "transformation",
    "self_issue_trial_license",
]
