from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="QuickConn",
    version="0.1.0",
    description="Unified HTTP clients: HTTP/1.0, HTTP/1.1, HTTP/2, HTTP/3 and Cloudflare solver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "httpx",
        "aioquic",
        "cloudscraper"
    ],
    author="أحمد الحراني",
    author_email="alhranyahmed@gmail.com",
    url="https://github.com/Gisnsl/QuickConn",
    license="MIT",
    keywords="http http1 http2 http3 cloudscraper client requests",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
