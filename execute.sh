#!/bin/bash

export PYTHONPATH="${PYTHONPATH}:${PWD}"
eval "./virtualenv/bin/python3 src/${1}.py \"${@:2}\""