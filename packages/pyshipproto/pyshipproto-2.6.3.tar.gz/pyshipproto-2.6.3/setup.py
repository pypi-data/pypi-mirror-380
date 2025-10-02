
from setuptools import setup, find_packages

VERSION = '2.6.3' 
DESCRIPTION = 'PyShipProto Package'
LONG_DESCRIPTION = 'Pyshipproto package with generated gRPC services.'

# Setting up
setup(
    name="pyshipproto",
    version=VERSION,
    author="PyShipProto",
    author_email="<pyshipproto@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    url="https://github.com/shipthisco/gRPC-protobuf",
    install_requires=[
        'grpcio>=1.48.0',
        'grpcio-tools>=1.48.0',
        'protobuf>=4.21.0,<6.0.0',  # Support older and newer protobuf versions
    ],
    python_requires='>=3.8',
    keywords=['python', 'gRPC', 'protobuf', 'pyshipproto'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ]
)
