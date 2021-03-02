"""Setup for ev-sa XBlock."""

import os
from setuptools import setup, find_packages

import ev_sa


def package_data(pkg, root_list):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for root in root_list:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}

setup(
    name='ev-sa',
    version=ev_sa.__version__,
    description='ev-sa Staff Assignment XBlock',
    license='Affero GNU General Public License v3 (GPLv3)',
    url="https://github.com/mitodl/edx-sga",
    author="MITx",
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'XBlock',
        'xblock-utils',
    ],
    entry_points={
        'xblock.v1': [
            'ev_sa = ev_sa.sa:StaffAssignmentXBlock',
        ]
    },
    package_data=package_data("ev_sa", ["static", "templates"]),
)
