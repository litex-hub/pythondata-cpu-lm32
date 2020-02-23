#!/usr/bin/env python3
import os

from litex.data.cpu import lm32

print("Found lm32 @", lm32.version_str)
print("Data is in", lm32.data_location)
assert os.path.exists(lm32.data_location)