from setuptools import setup
import os

here = os.path.abspath(os.path.dirname(__file__))
version_ns = {}  # type: ignore
with open(os.path.join(here, "pydbro", "_version.py")) as f:
    exec(f.read(), {}, version_ns)

setup(
    name="pydbro",
    version=version_ns["__version__"],
    description="Python Console Database Browser",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mtatton/pydbro",
    author="Michael Tatton",
    license="",
    packages=["pydbro"],
    install_requires=[
        "",
    ],
    entry_points={
        "console_scripts": [
          "dbro = pydbro.dbro:cli",
          "coned = pydbro.coned:cli",
        ],
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: User Interfaces",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.7",
    ],
)
