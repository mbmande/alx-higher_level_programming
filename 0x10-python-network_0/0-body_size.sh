#!/bin/bash
# erfjrhgrjfe
curl -sI "$1" | awk '/Content-Length/{print $2}'
