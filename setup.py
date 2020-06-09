import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jfrog-cli-python-pkg-ELISI",
    version="1.0.0",
    author="Eli Siesel",
    author_email="eli.siesel@gmail.com",
    description=" API CLI in Python that manage Artifactory SaaS instance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Elisi2020/jfrog_proj",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'click', 'requests' ,'json'
    ],
    entry_points={
    'console_scripts': [
        'jfrogcli=jfrog:jfrogcli_pkg:main',
    ],
},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)