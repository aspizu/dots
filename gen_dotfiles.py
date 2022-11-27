import itertools
from pathlib import Path

ROOT = Path("/")
HOME = Path("~").expanduser()


def indent_count(a: str) -> int:
    return sum(1 for _ in itertools.takewhile(str.isspace, a))


def get_dotfiles_paths():
    with open("dotfiles", "r") as f:
        indent_paths: list[Path] = []
        paths: list[Path] = []
        lines = [i[:-1] for i in f] + [""]
        for i, l in enumerate(lines):
            if l.strip() == "" or l.strip().startswith("#"):
                continue
            p = Path(l.strip()).expanduser()
            indent = indent_count(l)
            next_indent = indent_count(lines[i + 1])
            if next_indent > indent:
                indent_paths.append(p)
            else:
                ap = Path(*indent_paths + [p])
                if p.is_dir():
                    paths.extend(ap.glob("*/**"))
                else:
                    paths.append(ap)
                if next_indent < indent:
                    indent_paths.pop()
        return paths


def main():
    print("#!/bin/bash\nset -e")
    print("rm -rf ./_HOME_")
    print("rm -rf ./_ROOT_")
    paths = get_dotfiles_paths()
    for path in paths:
        try:
            parent = "_HOME_" / path.parent.relative_to(HOME)
        except ValueError:
            parent = "_ROOT_" / path.parent.relative_to(ROOT)
        print(f"mkdir -p ./{parent.as_posix()!r}")
        print(f"cp -r {path.as_posix()!r} ./{parent.as_posix()!r}")


main()
