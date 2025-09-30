from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="kalibr",  # This is what people pip install
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Connect any API to AI platforms in 10 lines of code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/kalibr-sdk",  # Your repo can stay kalibr-sdk
    packages=["kalibr_sdk", "kalibr_sdk.adapters", "kalibr_sdk.schemas"],  # Your code structure
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.28.0",
        "fastapi>=0.100.0",
        "uvicorn>=0.20.0",
        "httpx>=0.24.0",
    ],
)
