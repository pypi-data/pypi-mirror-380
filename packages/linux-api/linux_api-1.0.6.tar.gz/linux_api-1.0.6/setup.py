from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="linux_api",
    version="1.0.6",
    description="FastAPI-based Linux system monitoring and information server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Lies die requirements.txt ein
        line.strip() for line in open("requirements.txt") if line.strip() and not line.startswith("#")
    ],
    entry_points={
        "console_scripts": [
            "linux-api-server=server:main"
        ]
    },
    python_requires=">=3.11",
    platforms=["Linux"],
    keywords=["linux", "fastapi", "system monitoring", "api", "server"],
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Monitoring",
        "Framework :: FastAPI",
        "License :: OSI Approved :: MIT License",
    ],
    project_urls={
        "Documentation": "http://localhost:8000/docs",
        "Source": "https://github.com/ivoth/Linux-API",
    },
)