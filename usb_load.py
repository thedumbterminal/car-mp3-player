#!/usr/bin/env python
import os
import fnmatch
import random
import shutil
import sys


def _find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


def _make_dir(dir):
    if not os.path.isdir(dir):
        os.makedirs(dir)


def main():
    if len(sys.argv) != 3:
        sys.exit(
            "Usage: {0} <mp3 directory> <USB mount point>".format(sys.argv[0])
        )
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    tracks = _find('*.mp3', source_dir)
    print("Tracks found: {0}".format(len(tracks)))
    if len(tracks):
        while True:
            chosen = random.choice(tracks)
            source_full_dir = os.path.dirname(chosen)
            source_file = os.path.basename(chosen)
            # must not be an absolute path
            dest_partial_dir = source_full_dir.replace(
                source_dir, '', 1
            ).replace('/', '', 1)
            dest_full_dir = os.path.join(dest_dir, dest_partial_dir)
            dest_file = os.path.join(dest_full_dir, source_file)
            if not os.path.isfile(dest_file):
                _make_dir(dest_full_dir)
                print("Copying: {0} to {1}".format(chosen, dest_file))
                shutil.copy2(chosen, dest_file)


if __name__ == "__main__":
    main()
