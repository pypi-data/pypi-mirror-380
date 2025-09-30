"""
    Library setup file
"""
import subprocess
from setuptools import setup


try:
    subprocess.check_output(['pip', 'show', 'psycopg2'])
    PSYCOPG2_INSTALLED = True
except subprocess.CalledProcessError:
    PSYCOPG2_INSTALLED = False


install_requires = [
    "numpy>=1.26.4",
    "pandas>=2.1.0",
    "sqlalchemy>=2.0.27",
    "optilogic>=2.13.0",
    "PyJWT>=2.8.0",
    "httpx>=0.24.1"
]

# If psycopg2 is not installed let's check if we should use the binary version instead
if not PSYCOPG2_INSTALLED:
    import os

    # Look for USE_PSYCOPG2_BINARY, if not set, default to True, otherwise, use the value
    USE_BINARY = os.getenv('USE_PSYCOPG2_BINARY', 'True').lower() == 'true'

    if USE_BINARY:
        install_requires.append('psycopg2-binary>=2.9.9')
    else:
        install_requires.append('psycopg2>=2.9.9')


setup(
    name="ol-datastar",
    include_package_data=True,
    version="0.0.1",
    description="Helpful utilities for working with Datastar projects",
    url="https://cosmicfrog.com",
    author="Optilogic",
    packages=["ol-datastar"],
    license="MIT",
    install_requires=install_requires,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
