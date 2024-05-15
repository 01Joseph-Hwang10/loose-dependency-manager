import pytest
import shutil
from os.path import dirname, exists, join
from ..helpers import run_ldm_install

PROJECT_ROOT = join(dirname(__file__), "project")


def setup_module():
    shutil.rmtree(join(PROJECT_ROOT, "src"), ignore_errors=True)


@pytest.mark.order(1)
def test_ldm_specified_targets():
    assert run_ldm_install(["clamp"], cwd=PROJECT_ROOT)

    assert exists(join(PROJECT_ROOT, "src/utils/clamp.ts"))
    assert not exists(join(PROJECT_ROOT, "src/styles/reset.css"))


@pytest.mark.order(2)
def test_ldm_parallel_option():
    assert run_ldm_install(cwd=PROJECT_ROOT)

    assert exists(join(PROJECT_ROOT, "src/utils/clamp.ts"))
    assert exists(join(PROJECT_ROOT, "src/styles/reset.css"))
