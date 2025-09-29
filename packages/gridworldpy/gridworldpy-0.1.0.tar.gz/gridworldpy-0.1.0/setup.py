from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gridworldpy",
    version="0.1.0",
    author="LIC",
    author_email="liuchen.lic@gmail.com",
    description="A flexible and interactive grid world environment for reinforcement learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hitlic/gridworldpy",
    project_urls={
        "Bug Reports": "https://github.com/hitlic/gridworldpy/issues",
        "Source": "https://github.com/hitlic/gridworldpy",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",  
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
    ],
    extras_require={
        "examples": ["matplotlib>=3.5.0"],
    },
    keywords="reinforcement learning, grid world, environment, RL, AI, machine learning, visualization",
    include_package_data=True,
)