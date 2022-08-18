#!/usr/bin/env bash

# Add poetry to path if its not there already
export -U PATH=$HOME/.poetry/bin${PATH:+:$PATH}

# run parser
poetry run chewfiles --estc_number $1
