import shutil
from os.path import dirname, join
from ..helpers import run_ldm_install

PROJECT_ROOT = join(dirname(__file__), "project")


def setup_module():
    shutil.rmtree(join(PROJECT_ROOT, "src"), ignore_errors=True)


def test_ldm_empty_config():
    assert run_ldm_install(cwd=PROJECT_ROOT)
