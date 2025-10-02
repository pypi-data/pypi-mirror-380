from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="aiterm-cli",
    version="0.9.4",
    author="Fernando Mellado",
    description="AI-powered terminal tool assistant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fosilinx/AITerm-CLI",
    packages=find_packages(),
    package_data={
        'aiterm': ['*.json'],
        '': ['sounds/*.wav', 'sounds/*.mp3'],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: User Interfaces",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "openai>=1.0.0",
        "wcwidth>=0.2.0",
    ],
    entry_points={
        'console_scripts': [
        ],
    },
)