from __future__ import annotations

import configparser
import os
import subprocess
from dataclasses import dataclass
from functools import cached_property
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator
    from collections.abc import Mapping

    from typing_extensions import Self

PROJECT_PREFIX = os.path.expanduser("~/dev")


def find_dir_up(start: str, target: str) -> str | None:
    start = os.path.abspath(start)
    while True:
        complete_path = os.path.join(start, target)
        if os.path.exists(complete_path):
            return start
        if start == "/":
            break
        start = os.path.dirname(start)
    return None


def git_find_projects(
    start: str = PROJECT_PREFIX, depth: int = 4
) -> Generator[str]:
    if depth <= 0:
        return
    if os.path.exists(os.path.join(start, ".git")):
        yield os.path.abspath(start)
    else:
        for d in os.listdir(start):
            fp = os.path.join(start, d)
            if os.path.isdir(fp):
                yield from git_find_projects(start=fp, depth=depth - 1)


def git_remote_to_url(remote: str) -> str:
    part = (
        remote.removeprefix("git@")
        .removeprefix("https://")
        .removesuffix(".git")
        .replace(":", "/")
    )
    return f"https://{part}"


def git_suggested_dir(remote: str, prefix: str = PROJECT_PREFIX) -> str:
    return os.path.join(
        prefix, git_remote_to_url(remote).removeprefix("https://")
    )


def git_clone(
    repository: str,
    branch: str | None = None,
    directory: str | None = None,
    default_prefix: str = PROJECT_PREFIX,
) -> Git:
    directory = directory or git_suggested_dir(repository, default_prefix)
    if not os.path.exists(directory):
        cmd = (
            "git",
            "clone",
            *(() if not branch else ("--branch", branch)),
            repository,
            directory,
        )
        subprocess.run(cmd, check=True)  # noqa: S603
    return Git.from_dir(directory)


@dataclass
class Git:
    home: str

    def __post_init__(self) -> None:
        self._command_prefix = ("git", "-C", self.home)

    @classmethod
    def from_dir(cls, d: str) -> Self:
        result = find_dir_up(d, ".git")
        if not result:
            msg = f"Not a git project: {d}"
            raise FileNotFoundError(msg)
        return cls(home=result)

    def ls_files(self, *args: str) -> list[str]:
        cmd = (*self._command_prefix, "ls-files", *args)
        return subprocess.run(  # noqa: S603
            cmd, text=True, capture_output=True, check=True
        ).stdout.splitlines()

    def branch_default(self) -> str:
        file = os.path.join(
            self.home, ".git", "refs", "remotes", "origin", "HEAD"
        )
        if not os.path.exists(file):
            msg = "This git project not yet have a default branch!"
            raise FileNotFoundError(msg)
        with open(file) as f:
            return f.read().strip().removeprefix("ref: refs/remotes/origin/")

    def branch_current(self) -> str:
        with open(os.path.join(self.home, ".git", "HEAD")) as f:
            return f.read().strip().removeprefix("ref: refs/heads/")

    @cached_property
    def _git_config(self) -> Mapping[str, Mapping[str, str]]:
        config = configparser.ConfigParser(strict=False)
        config.read(os.path.join(self.home, ".git", "config"))
        return {
            k: {k: v.strip('"') for k, v in config[k].items()}
            for k in config.sections()
        }

    def branch_current_section(self) -> Mapping[str, str] | None:
        return self._git_config.get(f'branch "{self.branch_current}"')

    def branch_current_has_been_pushed(self) -> bool:
        return self.branch_current_section() is not None

    def repository(self) -> str:
        section = self._git_config['remote "origin"']
        if not section:
            msg = "This repo's origin has not been set!"
            raise KeyError(msg)
        return section["url"]

    def owner_repo(self) -> tuple[str, str]:
        (
            _,
            owner,
            repo,
        ) = (
            self.repository()
            .replace(":", "/")
            .removesuffix(".git")
            .rsplit("/", maxsplit=2)
        )

        return owner, repo

    def pr_number_guess(self) -> str | None:
        section = self.branch_current_section()
        if section and "github-pr-owner-number" in section:
            return section["github-pr-owner-number"].rsplit("#", maxsplit=1)[-1]
        return None

    def url_project(self) -> str:
        url = self.repository()
        if not url.startswith("http"):
            url = url.replace(":", "/", 1).replace("git@", "https://")
        return url.removesuffix(".git")

    def url_branch(self) -> str:
        return os.path.join(self.url_project(), "tree", self.branch_current())

    def url_pr_guess(self) -> str | None:
        pr_number = self.pr_number_guess()
        if pr_number:
            return os.path.join(self.url_project(), "pull", pr_number)
        return None

    def url_file(self, file: str) -> str:
        file = os.path.abspath(file).removeprefix(self.home).strip("/")
        return f"{self.url_project()}/blob/{self.branch_current()}/{file}"


if __name__ == "__main__":
    # url = "git@github.com:FlavioAmurrioCS/uv-to-pipfile.git"
    url = "git@github.com:FlavioAmurrioCS/nyle.git"
    g = git_clone(url)
    # g = Git.from_dir(".")
    print(f"{g.ls_files()=}")
    print(f"{g.branch_default()=}")
    print(f"{g.branch_current()=}")
    print(f"{g._git_config=}")  # noqa: SLF001
    print(f"{g.branch_current_section()=}")
    print(f"{g.branch_current_has_been_pushed()=}")
    print(f"{g.repository()=}")
    print(f"{g.owner_repo()=}")
    print(f"{g.pr_number_guess()=}")
    print(f"{g.url_project()=}")
    print(f"{g.url_branch()=}")
    print(f"{g.url_pr_guess()=}")
    print(f"{g.url_file('README.md')=}")
