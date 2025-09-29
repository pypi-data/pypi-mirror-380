from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ardent-sdk",
    version="0.3.7",
    author="Ardent AI",
    author_email="vikram@ardentai.io",
    description="Python SDK for Ardent AI - Simplify your data engineering tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArdentAILabs/ArdentAPI",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "httpx>=0.24.0",
        "python-dotenv>=0.19.0",
    ],
)