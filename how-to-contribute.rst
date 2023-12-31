Each extension implementation is an independent buildable Python project
residing in a subdirectory of this repository.  Implementations must integrate
with the [cti-python-stix2](https://github.com/oasis-open/cti-python-stix2)
library as registered extensions.  One can refer to
[stix2 docs](https://stix2.readthedocs.io/en/latest/guide/extensions.html) for
further information regarding how to do the integration.

To contribute an extension implementation:

- Fork this repository
- Create a subdirectory named after your extension (naming convention?)
- Create a buildable Python project in your subdirectory:
  - The project name should also reflect your extension (any naming rules?
    E.g. "python-stix2-<your_ext_name>-extension"?)
  - Recommended style is [pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/),
    e.g. using setuptools build backend with a [src-layout](https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout)
- Unit tests should be included
    - The code should work on the same versions of Python as the stix2 library
      it will integrate with.  (suggests we really should have CI enabled,
      since few will have all those versions of Python installed to test with.)
- (Should examples be included?  Must they be jupyter notebooks?)
- Make a pull request to merge your work into this repository.
