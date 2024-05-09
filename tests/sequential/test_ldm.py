import subprocess
from os.path import dirname, exists, join

PROJECT_ROOT = join(dirname(__file__), "project")


def test_ldm_sequential_option():
    subprocess.check_output(
        "ldm install",
        shell=True,
        cwd=PROJECT_ROOT,
    )

    assert exists(join(PROJECT_ROOT, "src/utils/clamp.ts"))
    assert exists(join(PROJECT_ROOT, "src/styles/reset.css"))
