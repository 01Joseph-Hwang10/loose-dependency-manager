import pytest
import shutil
import subprocess
from os.path import dirname, exists, join

PROJECT_ROOT = join(dirname(__file__), "project")


def setup_module():
    shutil.rmtree(join(PROJECT_ROOT, "src"), ignore_errors=True)


@pytest.mark.order(1)
def test_ldm_specified_targets():
    _run_ldm_install(["clamp"])

    assert exists(join(PROJECT_ROOT, "src/utils/clamp.ts"))
    assert not exists(join(PROJECT_ROOT, "src/styles/reset.css"))


@pytest.mark.order(2)
def test_ldm_sequential_option():
    _run_ldm_install()

    assert exists(join(PROJECT_ROOT, "src/utils/clamp.ts"))
    assert exists(join(PROJECT_ROOT, "src/styles/reset.css"))


def _run_ldm_install(args: list[str] | None = None):
    return subprocess.check_output(
        f"ldm install {' '.join(args or [])}",
        shell=True,
        cwd=PROJECT_ROOT,
    )
