#/bin/bash

if [ ! -d day$1 ]; then
  mkdir day$1
  cd day$1
  touch data.txt
  touch test.txt
  # xsel -b > data.txt
  cp ../template_solve.py ./solve.py
else
  echo That directory exists
fi

