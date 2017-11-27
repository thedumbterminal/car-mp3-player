#!/usr/bin/env python
import os
import fnmatch
import random
import subprocess
import sys

def _find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def _playCommand():
    if sys.platform == 'darwin':
        return 'afplay "{0}"'
    else:
        return 'mpg321 -a hw:1 -o alsa "{0}"'

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: {0} <mp3 directory>".format(sys.argv[0]))
    tracks = _find('*.mp3', sys.argv[1])
    print "Tracks found: {0}".format(len(tracks))
    if len(tracks):
        playCommand = _playCommand()
        while True:
            chosen = random.choice(tracks)
            cmd = playCommand.format(chosen)
            print cmd
            subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    main()
