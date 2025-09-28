import setuptools

with open("requirements.txt") as fp:
    requirements = fp.readlines()

with open("requirements-dev.txt") as fp:
    requirements_dev = fp.readlines()

setuptools.setup(
    name="rsapi2",
    version="0.0.43",
    author="xn--it-uiab.eu",
    author_email="admin@xn--it-uiab.eu",
    description="Python library for accessing Runescape APIs",
    long_description_content_type="text/markdown",
    url="https://github.com/ostracker-xyz/pyrsapi",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    extras_require={
        "dev": requirements_dev,
        "tests": requirements_dev,
    }
)
