cat words.txt | sed -r 's/(^\s+|\s+$)//g' | tr -s ' '| tr -d ',.' | tr ' ' '\n' | sort | uniq -c | sort -r | awk '{print $2" "$1}'
