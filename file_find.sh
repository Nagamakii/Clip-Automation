#!/bin/bash
DIR="/var/www/lager-scanner/filer/Nav/FromNav"
inotifywait -m -r -e create "$DIR" | while read f

do
    # you may want to release the monkey after the test :)
    echo monkey
    main.py
done
