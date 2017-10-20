#!/usr/bin/env python
import os
import fnmatch
import random
import subprocess

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def main():
    tracks = find('*.mp3', '/mnt/usb/mp3s')
    print "Tracks found: {0}".format(len(tracks))
    if(len(tracks)):
        while True:
            chosen = random.choice(tracks)
            cmd = 'mpg321 -a hw:1 -o alsa "{0}"'.format(chosen)
            print cmd
            subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    main()
