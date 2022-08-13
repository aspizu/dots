import os
from pathlib import Path

__home__ = Path("~").expanduser()
__here__ = Path(".").expanduser()


def sh(command: str) -> None:
    print(f" >>> {command}")
    os.system(command)


with open("index.txt", "r") as fp:
    f: list[Path] = [Path(i).expanduser() for i in fp.read().splitlines()]

sh("rm -rf files")

for path in f:
    if path.is_file():
        head = __here__ / "files" / path.relative_to(__home__).parent
        if head != __here__ and not head.exists():
            sh(f"mkdir -p '{head.as_posix()}'")
        if path.is_file():
            sh(f"cp '{path.as_posix()}' '{head.as_posix()}'")
    elif path.is_dir():
        head = __here__ / "files" / path.relative_to(__home__)
        if not head.parent.exists():
            sh(f"mkdir -p '{head.parent.as_posix()}'")
        sh(f"cp -r '{path.as_posix()}' '{head.as_posix()}'")
