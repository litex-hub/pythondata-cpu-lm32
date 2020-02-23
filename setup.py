import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

from litex.data.cpu.lm32 import version_str

setuptools.setup(
    name="litex-data-cpu-lm32",
    version=version_str,
    author="LiteX Authors",
    author_email="litex@googlegroups.com",
    description="Python module containing data files for using the LatticeMico32 cpu with LiteX.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/litex-hub/litex-data-cpu-lm32",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Eclipse Public License 1.0 (EPL-1.0)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    zip_safe=False,
)