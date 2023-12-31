Each extension implementation is an independent buildable Python project
residing in a subdirectory of this repository.  Implementations must integrate
with the `cti-python-stix2 <https://github.com/oasis-open/cti-python-stix2>`_
library as registered extensions.  One can refer to
`stix2 extension docs <https://stix2.readthedocs.io/en/latest/guide/extensions.html>`_ for
further information regarding how to do the integration.

To contribute an extension implementation:

- Fork this repository
- Create a subdirectory named after your extension.  The naming convention is: <STIX object type name>-<extension definition id>.  For multiple extensions which are related, use the "root" STIX object type name.
    For example:  incident-extension-definition--ef765651-680c-498d-9894-99799f2fa126
- Create a buildable Python project in your subdirectory:
  - The project name should also reflect your extension
    For example:   "python-stix2-<directory name from previous step>"
  - Recommended style is `pyproject.toml <https://packaging.python.org/en/latest/guides/writing-pyproject-toml>`_,
    e.g. using setuptools build backend with a `src-layout <https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout>`_.
- Unit tests should be included
    - The code should work on the same versions of Python as the stix2 library
      it will integrate with.  (suggests we really should have CI enabled,
      since few will have all those versions of Python installed to test with.)
- (Should examples be included?  Must they be jupyter notebooks?)
- Make a pull request to merge your work into this repository.
