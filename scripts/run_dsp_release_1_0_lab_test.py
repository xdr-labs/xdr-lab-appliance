#!/usr/bin/env python3
"""DSP operational lab runner — invokes external xdr-poc-script checkout."""

from __future__ import annotations

import os
import sys
from pathlib import Path

_DEFAULT_DSP_ROOT = Path("/home/aella/xdr-poc-script")
_DSP_ROOT = Path(os.environ.get("XDR_POC_SCRIPT_ROOT", str(_DEFAULT_DSP_ROOT))).resolve()

if not _DSP_ROOT.is_dir():
    sys.stderr.write(
        "DSP checkout not found.\n"
        f"  Expected: {_DSP_ROOT}\n"
        "  Clone: git clone git@github.com:xdr-labs/xdr-poc-script.git\n"
        "  Or set XDR_POC_SCRIPT_ROOT to your checkout path.\n"
        "  See docs/DSP_EXTERNAL_DEPENDENCY.md\n"
    )
    raise SystemExit(1)

if str(_DSP_ROOT) not in sys.path:
    sys.path.insert(0, str(_DSP_ROOT))

from dsp.lab.operational_runner import main

if __name__ == "__main__":
    raise SystemExit(main())
