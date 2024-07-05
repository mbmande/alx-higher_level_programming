#!/bin/bash
# bvjhyhggghgkghg
curl -sI "$1" | awk '/Allow/ { $1=""; print $0 }'
