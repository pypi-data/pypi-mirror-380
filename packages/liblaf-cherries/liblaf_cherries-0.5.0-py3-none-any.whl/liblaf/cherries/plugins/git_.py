import shlex
import subprocess
import sys
from pathlib import Path
from typing import Any, override

import attrs
import git

from liblaf import grapes
from liblaf.cherries import core
from liblaf.cherries.typing import PathLike


@attrs.define
class Git(core.Run):
    inputs: list[Path] = attrs.field(factory=list)
    outputs: list[Path] = attrs.field(factory=list)
    repo: git.Repo = attrs.field(default=None)
    verify: bool = False

    @override
    @core.impl(after=("Dvc",))
    def end(self, *args, **kwargs) -> None:
        if not self.repo.is_dirty(untracked_files=True):
            return
        self.repo.git.add(all=True)
        subprocess.run(["git", "status"], check=False)
        message: str = self._make_commit_message()
        self.repo.git.commit(message=message, no_verify=not self.verify)

    @override
    @core.impl
    def log_input(self, path: PathLike, *args, **kwargs) -> None:
        path: Path = Path(path)
        self.inputs.append(path.relative_to(self.project_dir))

    @override
    @core.impl
    def log_output(
        self,
        path: PathLike,
        name: PathLike | None = None,
        **kwargs,
    ) -> None:
        path: Path = Path(path)
        self.outputs.append(path.relative_to(self.project_dir))

    @override
    @core.impl
    def start(self, *args, **kwargs) -> None:
        self.repo = git.Repo(self.project_dir, search_parent_directories=True)

    def _make_commit_message(self) -> str:
        name: str = self.plugin_root.name
        message: str = f"chore(cherries): {name}\n\n"
        metadata: dict[str, Any] = {}
        metadata["cmd"] = shlex.join(sys.orig_argv)
        if url := self.plugin_root.url:
            metadata["url"] = url
        if params := self.plugin_root.get_params():
            metadata["params"] = params
        if inputs := self.inputs:
            metadata["inputs"] = inputs
        if outputs := self.outputs:
            metadata["outputs"] = outputs
        message += grapes.yaml.encode(metadata).decode()
        return message
