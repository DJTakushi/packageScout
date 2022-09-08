#!/bin/bash

echo "starting tbuild.sh..."

# clean up
rm -r dist
rm -r packageScout.egg-info
rm -r deb_dist

# Python Package Build
python3 -m build

# ChangeOwnership to Root
chown root:root -R .

# Change Permissions
chmod 0755 .

# Generate SOURCE Package
py2dsc dist/packageScout-0.1.tar.gz

# Create .deb package
cd deb_dist/packagescout-0.1
dpkg-buildpackage -rfakeroot -uc -us

echo "tbuild.sh complete."
