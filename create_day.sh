#!/bin/bash

echo "Enter day (n): "
read day

numeric=true

if ! [[ "$day" =~ ^[0-9]+$ ]] || [ ${#day} -gt 2 ]; then
    echo "Invalid input. Please enter a numeric value with at most 2 digits."
    exit 1
fi

if [ "$day" -ne "$day" ] 2>/dev/null; then
    echo "Invalid input. Please enter a numeric value with at most 2 digits."
    exit 1
fi

day_formatted=$(printf "%02d" $day)

if [ ! -d "day/$day_formatted" ]; then
    mkdir -p "day/$day_formatted/src"
    mkdir -p "day/$day_formatted/input"
fi

if [ ! -e "day/$day_formatted/input/test.txt" ]; then
    touch "day/$day_formatted/input/test.txt"
fi

if [ ! -e "day/$day_formatted/input/input.txt" ]; then
    touch "day/$day_formatted/input/input.txt"
fi

if [ ! -e "day/$day_formatted/main.py" ]; then
    cp -n "template/main.py" "day/$day_formatted/main.py"
fi

if [ ! -e "day/$day_formatted/src/part_1.py" ]; then
    cp -n "template/part_1.py" "day/$day_formatted/src/part_1.py"
fi

if [ ! -e "day/$day_formatted/src/part_2.py" ]; then
    cp -n "template/part_2.py" "day/$day_formatted/src/part_2.py"
fi

if [ ! -e "day/$day_formatted/src/__init__.py" ]; then
    cp -n "template/__init__.py" "day/$day_formatted/src/__init__.py"
fi

if [ ! -e "day/$day_formatted/src/utils.py" ]; then
    cp -n "template/utils.py" "day/$day_formatted/src/utils.py"
fi

