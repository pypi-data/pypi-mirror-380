from __future__ import annotations

from fzf import fzf

from nyle.git import git_clone
from nyle.git import git_find_projects


def select_project() -> None:
    selected = fzf(git_find_projects())
    if selected:
        print(selected)


def main(_argv: list[str] | None = None) -> int:
    import typer

    app = typer.Typer()
    app.command(name="clone")(git_clone)
    app.command()(select_project)

    app()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
