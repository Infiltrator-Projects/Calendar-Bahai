#!/usr/bin/env python3
"""Regression: independent native installer detects its PDF dependency."""
import importlib.util
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("provider_release", root / "packaging/release.py")
provider = importlib.util.module_from_spec(spec)
spec.loader.exec_module(provider)

with patch.object(provider.shutil, "which", return_value="/usr/bin/tool"), \
     patch.object(provider.subprocess, "check_output", return_value="en_US.utf8\\n"), \
     patch.object(provider.subprocess, "run", return_value=SimpleNamespace(returncode=1)):
    missing = provider.check_requirements()
    assert "python3-reportlab" in missing, missing

with patch.object(provider.shutil, "which", return_value="/usr/bin/tool"), \
     patch.object(provider.subprocess, "check_output", return_value="en_US.utf8\\n"), \
     patch.object(provider.subprocess, "run", return_value=SimpleNamespace(returncode=0)):
    assert "python3-reportlab" not in provider.check_requirements()

print("Independent PDF dependency detection passed")
