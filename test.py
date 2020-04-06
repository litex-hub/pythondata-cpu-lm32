#!/usr/bin/env python3
import os

from litex.data.cpu import lm32

print("Found lm32 @ version", lm32.version_str, "(with data", lm32.data_version_str, ")")
print()
print("Data is in", lm32.data_location)
assert os.path.exists(lm32.data_location)
print("Data is version", lm32.data_version_str, lm32.data_git_hash)
print("-"*75)
print(lm32.data_git_msg)
print("-"*75)
print()
print("It contains:")
for root, dirs, files in os.walk(lm32.data_location):
    dirs.sort()
    for f in sorted(files):
        path = os.path.relpath(os.path.join(root, f), lm32.data_location)
        print(" -", path)
