#!/usr/bin/env bash
set -euo pipefail
for topic in /clock /odom /scan /tf; do
  echo "Checking $topic"
  timeout 12 ros2 topic echo "$topic" --once >/dev/null || { echo "FAIL: $topic"; exit 1; }
done
echo 'PASS: core ROS interfaces publish messages'
