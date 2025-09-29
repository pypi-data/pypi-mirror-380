from setuptools import setup, find_packages

with open("/home/inact1ve/hse_lab/eco/digital_ecomonitoring/test_suite/dsm_lib/requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="dsm-lib",
    version="2.0.0",
    packages=find_packages(),
    install_requires=required,
    author="Igor Chernitsin",
    description="DSM library for a forecast air pollution"
)