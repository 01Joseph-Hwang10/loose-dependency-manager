import subprocess


def run_ldm_install(
    args: list[str] | None = None,
    *,
    cwd: str,
):
    return subprocess.check_output(
        f"ldm install {' '.join(args or [])}",
        shell=True,
        cwd=cwd,
    )
