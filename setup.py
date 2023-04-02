from setuptools import setup, find_packages
from Cython.Build import cythonize

NAME             = "monotonic_align"
AUTHOR           = "unrea1"
AUTHOR_EMAIL     = "unrea1sama@outlook.com"
DESCRIPTION      = "Monotonic Align from VITS"
LICENSE          = "MIT"
KEYWORDS         = "None"
URL              = "https://github.com/unrea1-sama/monotonic_align"
README           = "README.md"
VERSION          = "0.0.4"
CLASSIFIERS      = [
  "Environment :: Console",
  "License :: OSI Approved :: MIT License",
  "Programming Language :: Python :: 3.7",
]
INSTALL_REQUIRES = [
  "Cython",
  "numpy",
]

ENTRY_POINTS = {
    
}

SCRIPTS = [
  
]

with open("README.md", "r") as f:
    LONG_DESCRIPTION = f.read()

if __name__ == "__main__":
  setup(
    name=NAME,
    version=VERSION,
    packages=find_packages(),
    author=AUTHOR,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license=LICENSE,
    keywords=KEYWORDS,
    url=URL,
    classifiers=CLASSIFIERS,
    ext_modules = cythonize("./monotonic_align/core.pyx"),
    install_requires=INSTALL_REQUIRES,
    entry_points=ENTRY_POINTS,
    scripts=SCRIPTS,
    include_package_data=True    
  )