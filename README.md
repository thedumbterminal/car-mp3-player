# Car MP3 Player

[![CI](https://github.com/thedumbterminal/car-mp3-player/actions/workflows/ci.yml/badge.svg)](https://github.com/thedumbterminal/car-mp3-player/actions/workflows/ci.yml)

Playing random music on the move.

Supports:

* Mac OSX
* linux (requires [mpg321](http://mpg321.sourceforge.net/)).

## Install

    git clone https://github.com/thedumbterminal/car-mp3-player.git
    pip install -r requirements.txt

## Run

    cd car-mp3-player

To play music randomly and recursively from a directory:

    ./play.py /some/directory

To copy music randomly and recursively from a directory to another:

    ./usb_load.py /source/directory /dest/directory
