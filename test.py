#!/usr/bin/env python3
import os

from litex.data.cpu import lm32

print("Found lm32 @ version", lm32.version_str, "("+lm32.git_hash+")")
print("Data is in", lm32.data_location)
assert os.path.exists(lm32.data_location)
print("It contains:\n -", end=" ")
print("\n - ".join(os.listdir(lm32.data_location)))