from setuptools import setup
from setuptools.command.install import install
from setuptools.command.develop import develop
import subprocess
import sys


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        subprocess.call([sys.executable, 'scripts/post_install.py'])


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        subprocess.call([sys.executable, 'scripts/post_install.py'])


setup(
    cmdclass={
        'install': PostInstallCommand,
        'develop': PostDevelopCommand,
    },
)
