# Clairmeta - (C) YMAGIS S.A.
# See LICENSE for more information

from clairmeta.info import __license__, __author__, __version__
from clairmeta.dcp import DCP
from clairmeta.sequence import Sequence
from clairmeta.logger import get_log
from clairmeta.utils.probe import check_command, PROBE_DEPS


__all__ = ["DCP", "Sequence"]
__license__ = __license__
__author__ = __author__
__version__ = __version__


# External dependencies check
for d in PROBE_DEPS:
    if not check_command(d):
        get_log().warning("Missing dependency : {}".format(d))
