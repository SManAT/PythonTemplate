"""
setup.py setHostname
Usage: sudo pip3 install .
"""
__author__ = 'Mag. Stefan Hagmann'

from distutils.core import setup

if __name__ == '__main__':

    setup(
        name="O365Admin",
        description="Manage O365 Accounts in school",
        author=__author__,
        maintainer=__author__,
        license="GPLv3",
        install_requires=[
            'PyQt6',
            'PySide6',
            'O365',
        ],
        python_requires='>=3.8',
    )
