#!/bin/bash

killall -9 python
rm -rf data/
mkdir data
find data_all/ -name "*_fps.mp4" >> trash.txt
while read line
do
  rm -rf "$line"
done < trash.txt
rm trash.txt
