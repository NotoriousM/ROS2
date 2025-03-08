#!/bin/bash

set -e

source /opt/ros/jazzy/setup.bash
source /app/ws_pub_sub/install/setup.bash

exec "$@"