from pathlib import Path
import os
import sys


if "WOWOOL_ROOT" in os.environ:
    WOWOOL_ROOT = os.environ["WOWOOL_ROOT"]
    expanded_wowool_root = Path(WOWOOL_ROOT).expanduser().resolve()
    import platform

    if platform.system() == "Windows":
        WOWOOL_LIB = expanded_wowool_root / "bin"
        if str(WOWOOL_LIB) not in sys.path:
            sys.path.append(str(WOWOOL_LIB))
    WOWOOL_LIB = expanded_wowool_root / "lib"
else:
    WOWOOL_LIB = Path(__file__).resolve().parent
    os.environ["WOWOOL_ROOT"] = str(WOWOOL_LIB.parent)

if str(WOWOOL_LIB) not in sys.path:
    sys.path.append(str(WOWOOL_LIB))


from _wowool_sdk import *  # noqa
from _wowool_sdk import (
    TirException,
    domain,
    get_domain_info,
    results,
    TirJsonException,
    pipeline_expand,
    compile_domain,
    analyzer,
    engine,
)  # noqa
