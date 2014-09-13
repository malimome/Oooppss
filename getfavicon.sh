#!/bin/bash
while read line           
do
  url=www.$line/favicon.ico
  echo -n "."
  if [ -a favicon/$line.ico ]; then continue; fi
  wget -q -t 1 -T 5 -O/dev/null -q $url && echo $url exists || echo $url not exist -------
  wget -q -t 1 -T 5 -O favicon/$line.ico $url
done < addurls.txt
