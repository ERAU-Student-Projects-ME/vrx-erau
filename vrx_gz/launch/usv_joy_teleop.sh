#!/usr/bin/env bash

PKG_NAME="vrx_gz"
LAUNCH_FILE="usv_joy_teleop.py"

if [[ -z "$1" ]]; then
  echo
  echo "⚠️  WARNING: 'vehicle' not specified."
  echo "    Defaulting to vehicle='minion'"
  echo "    List of vehicles - 'minion', 'mini_minion'"
  read -p "    Continue? [Y/n]: " ans

  if [[ "$ans" == "n" || "$ans" == "N" ]]; then
    echo "❌ Launch aborted by user."
    exit 1
  fi

  ros2 launch $PKG_NAME $LAUNCH_FILE
else
  ros2 launch $PKG_NAME $LAUNCH_FILE vehicle:=$1
fi
