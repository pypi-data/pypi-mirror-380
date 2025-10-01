from setuptools import setup, find_packages

setup(
    name="pymillion",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["rich","flask"],
    entry_points={
        "console_scripts": [
            "pymillion=pymillion.cli:main",
        ]
    },
)
