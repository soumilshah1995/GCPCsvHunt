from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="gcpcsvhunt",
    version="2.2.0",
    description="""
        This package allows to download all CSV Files from GCP bucket 
     """,
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/soumilshah1995/GCPCsvHunt",
    author="Soumil Nitin Shah",
    author_email="soushah@my.bridgeport.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["gcpcsvhunt"],
    include_package_data=True,
    install_requires=["google-cloud-storage", "pandas"]
)