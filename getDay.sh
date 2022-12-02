#!/bin/bash

#takes day int of the day's input data etc to fetch
# https://www.reddit.com/r/adventofcode/comments/a2vonl/how_to_download_inputs_with_a_script/

if [[ -z "$1" ]]
then
    echo "please provide the day"
    exit 1
fi

mkdir day$1/
touch day$1/main.py
curl "https://adventofcode.com/2022/day/$1/input" \
  --cookie "session=SESSION" \
  --compressed > day$1/input.txt
