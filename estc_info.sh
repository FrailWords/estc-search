#!/usr/bin/env bash

function addToPATH {
  case ":$PATH:" in
    *":$1:"*) :;; # already there
    *) PATH="$1:$PATH";; # or PATH="$PATH:$1"
  esac
}

# Add poetry to path if its not there already
addToPATH $HOME/.poetry/bin

# run parser
ESTC_NUMBERS=$1
poetry run chewfiles --estc_numbers ${ESTC_NUMBERS}
