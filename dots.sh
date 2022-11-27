#!/bin/bash
set -e

case $1 in
--update)
  python gen_dotfiles.py | bash
  ;;
--install)
  cp -r _HOME_/. $HOME
  sudo cp -r ROOT_/. /
  ;;
--install-home)
  cp -r _HOME_/. $HOME
  ;;
--install-root)
  sudo cp -r _ROOT_/. /
  ;;
*)
  echo "USAGE:                                                        "
  echo "  ./dots.sh --update          Update files in repo            "
  echo "  ./dots.sh --install         Install files into HOME and ROOT"
  echo "  ./dots.sh --install-home    Install files only into HOME    "
  echo "  ./dots.sh --install-root    Install files only into ROOT    "
  ;;
esac
