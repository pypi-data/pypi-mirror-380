from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ratemaking-tools",
    version="0.2.0",
    author="Aria Team",
    author_email="",  # You can add your email here if you want
    description="A comprehensive Python library for P&C actuarial ratemaking",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/ratemaking-tools",  # Update with your GitHub URL when ready
    project_urls={
        "Bug Reports": "https://github.com/YOUR_USERNAME/ratemaking-tools/issues",
        "Source": "https://github.com/YOUR_USERNAME/ratemaking-tools",
        "Documentation": "https://github.com/YOUR_USERNAME/ratemaking-tools#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="actuarial ratemaking credibility insurance P&C casualty property",
    python_requires=">=3.8",
    install_requires=[
        # All modules currently use standard library only
    ],
    extras_require={
        "test": [
            "pytest>=7.0.0",
            "numpy>=1.20.0",
            "pandas>=1.3.0",
            "pyperclip>=1.8.0",
            "pyautogui>=0.9.0",
            "watchdog>=2.0.0",
        ],
        "dev": [
            "pytest>=7.0.0",
            "black",
            "flake8",
            "mypy",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
