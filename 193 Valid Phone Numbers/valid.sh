#!/usr/bin/env bash
if [ "$(uname)" == "Darwin" ]; then
    sed -nE '/^[0-9]{3}-[0-9]{3}-[0-9]{4}$|^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$/ p' file.txt
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    sed -nr '/^[0-9]{3}-[0-9]{3}-[0-9]{4}$|^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$/ p' file.txt
fi