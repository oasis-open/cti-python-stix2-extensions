
1. Clone cti-stix-generator directory.
1. Install generator from cti-stix-generator directory.
1. `pip install jupyter stix2-viz`
1. `pip install nbclassic`
1. `jupyter nbclassic-extension install stix2viz --py --user`
1. `jupyter nbclassic-extension enable stix2viz --py`
1. `jupyter nbclassic`

If you want the latest visjs visualization, don't install stix2-viz from pypi.
Instead, git clone from the repo at
https://github.com/oasis-open/cti-stix-visualization and install from there.
(The pypi version still uses the old d3 based visualization.)  Use an editable
installation, because the setup.py there still bundles the wrong (d3) files,
e.g.: `pip install -e .`.
