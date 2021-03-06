import os
from setuptools import setup, find_packages
from importlib.machinery import SourceFileLoader


module_name = "playwright_nonocaptcha"

module = SourceFileLoader(
    module_name, os.path.join(module_name, "__init__.py")
).load_module()


def load_requirements(fname):
    """ load requirements from a pip requirements file """
    with open(fname) as f:
        line_iter = (line.strip() for line in f.readlines())
        return [line for line in line_iter if line and line[0] != "#"]


setup(
    name=module_name.replace("_", "-"),
    version=module.__version__,
    author=module.__author__,
    author_email=module.authors_email,
    license=module.__license__,
    description=module.package_info,
    url="https://github.com/embium/playwright-nonocaptcha",
    # Hm, HTTPError: 400 Bad Request from https://test.pypi.org/legacy/
    # The description failed to render in the default format of reStructuredText. See https://test.pypi.org/help/#description-content-type for more information.
    # long_description=open("README.rst").read(),
    platforms="all",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: JavaScript",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities"
    ],
    package_data={'data': ['*.*']},
    include_package_data=True,
    packages=find_packages(),
    install_requires=load_requirements("requirements.txt"),
)