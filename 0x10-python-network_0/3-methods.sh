#!/bin/bash
# bvjhyhggghgkghg
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
