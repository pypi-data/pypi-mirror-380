# ============================================
# setup.py
# ============================================
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dsf-access-sdk",
    version="1.0.0",
    author="Jaime Alexander Jimenez",
    author_email="contacto@softwarefinanzas.com.co",
    description="SDK for DSF Access Control API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaimeajl/dsf-access-sdk",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=["requests>=2.25.0"],
    keywords="dsf access control evaluation api sdk",
)