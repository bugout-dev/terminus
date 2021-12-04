from setuptools import find_packages, setup

long_description = ""
with open("README.md") as ifp:
    long_description = ifp.read()

setup(
    name="moonstream-terminus",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["eth-brownie", "moonworm", "tqdm"],
    extras_require={
        "dev": [
            "black",
            "isort",
            "mypy",
        ],
        "distribute": ["setuptools", "twine", "wheel"],
    },
    description="terminus: decentralized authorization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Moonstream",
    author_email="engineering@moonstream.to",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.6",
    url="https://github.com/bugout-dev/terminus",
    entry_points={"console_scripts": []},
    include_package_data=True,
)
