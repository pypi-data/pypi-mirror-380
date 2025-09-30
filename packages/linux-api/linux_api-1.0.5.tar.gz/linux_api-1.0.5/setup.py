from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()

setup(
    name="Linux-API",
    version="1.0.5",
    description="A FastAPI-based Python web server for Linux system monitoring and information",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ivole32",
    url="https://github.com/Ivole32/Linux-API",
    project_urls={
        "Bug Reports": "https://github.com/Ivole32/Linux-API/issues",
        "Source": "https://github.com/Ivole32/Linux-API",
        "Documentation": "https://github.com/Ivole32/Linux-API/blob/main/README.md",
    },
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.11",
    install_requires=read_requirements(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Systems Administration",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: FastAPI",
    ],
    keywords="linux, system-monitoring, fastapi, rest-api, system-information, server-monitoring",
    entry_points={
        "console_scripts": [
            "start-linux-api=linux_api.start_script:main"
        ]
    },
    package_data={
        "linux_api": [
            "../start.sh",
            "../requirements.txt",
            "../start_debug.sh",
            "../config.env",
            "../api/*",
            "../core_functions/*"
        ]
    },
    zip_safe=False,
)