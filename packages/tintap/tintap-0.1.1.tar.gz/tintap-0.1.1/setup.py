from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tintap",
    version="0.1.1",
    author="tintap",
    author_email="contact@tintap.ai",
    description="AI audio detection and attribution Python SDK for tintap platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tintap/tintap-python",
    project_urls={
        "Homepage": "https://tintap.ai",
        "Bug Tracker": "https://github.com/tintap/tintap-python/issues",
        "Documentation": "https://docs.tintap.ai",
        "Source Code": "https://github.com/tintap/tintap-python",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
        "urllib3>=1.26.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-asyncio>=0.18.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.900",
        ],
    },
    keywords=[
        "ai",
        "audio",
        "detection",
        "analysis",
        "artificial-intelligence",
        "audio-processing",
        "content-attribution",
        "machine-learning",
        "music",
        "speech",
    ],
    zip_safe=False,
)