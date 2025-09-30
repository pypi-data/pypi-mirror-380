from setuptools import setup, find_packages


setup(
    name="zipcodestack",
    version="0.1.1",
    description="Official Python client for zipcodestack.com API",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Zipcodestack",
    author_email="support@zipcodestack.com",
    url="https://zipcodestack.com/docs/",
    packages=find_packages(exclude=("tests", "examples")),
    python_requires=">=3.8",
    install_requires=[
        "everapi>=0.1.0",
    ],
    license="MIT",
    license_files=("LICENSE",),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
    ],
    project_urls={
        "Documentation": "https://zipcodestack.com/docs/",
        "Source": "https://github.com/everapihq/zipcodestack-python",
        "Tracker": "https://github.com/everapihq/zipcodestack-python/issues",
    },
    include_package_data=True,
)
