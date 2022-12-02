#!/bin/bash

#takes day int of the day's input data etc to fetch

if [[ -z "$1" ]]
then
    echo "please provide the day"
    exit 1
fi

mkdir day$1/
touch day$1/main.py
curl "https://adventofcode.com/2022/day/$1/input" \
  -H 'authority: adventofcode.com' \
  -H 'pragma: no-cache' \
  -H 'cache-control: no-cache' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-user: ?1' \
  -H 'sec-fetch-dest: document' \
  -H "referer: https://adventofcode.com/2022/day/$1" \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cookie: <YOUR COOKIE HERE>' \
  --compressed > day$1/input.txt
