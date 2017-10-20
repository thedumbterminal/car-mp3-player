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
    tracks = find('*.mp3', '/tmp/mp3s')

    while True:
        chosen = random.choice(tracks)
        print chosen
        subprocess.call(['ls', '-al', chosen])

if __name__ == "__main__":
    main()
