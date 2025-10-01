from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="queuesim",
    version="0.1.0",
    description="A Simple Mathematical Queueing Theory Simulator and Calculator (M/M/1 , M/M/c etc)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Hrishabh",
    author_email="hrishabhtest@gmail.com",
    license="MIT",
    keywords=[
        "queueing", "simulation", "queueing-theory",
        "operations-research", "math", "statistics",
        "education", "probability", "performance-analysis"
    ],
    url="https://github.com/hrishabhxcode/queuelab",
    packages=find_packages(),
    install_requires=["matplotlib"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
)
