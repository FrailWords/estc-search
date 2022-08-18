#!/usr/bin/env bash

# Add poetry to path if its not there already
case :$PATH: # notice colons around the value
  in *:$HOME/.poetry/bin:*) ;; # do nothing, it's there
     *) export PATH="$HOME/.poetry/bin:$PATH";;
esac

# run parser
poetry run chewfiles --estc_number $1
