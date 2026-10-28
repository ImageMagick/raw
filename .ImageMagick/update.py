#!/usr/bin/env python3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "Tools"))

from dependency_updater import Step, Updater

URL = "https://github.com/LibRaw/LibRaw/archive/refs/tags/{version}.tar.gz"


def update_source(updater):
    updater.replace_source()
    updater.update_config()


def apply_patches(updater):
    updater.apply_patches()


updater = Updater(__file__, "libraw", URL)
updater.run([
    Step("Replace the source with the release and update Config.txt", update_source,
        "Updated LibRaw to {version}"),
    Step("Apply the patches to fix building with a C++ compiler", apply_patches,
        "Patches to fix building with a C++ compiler."),
    updater.clone_dependencies_step(),
])
