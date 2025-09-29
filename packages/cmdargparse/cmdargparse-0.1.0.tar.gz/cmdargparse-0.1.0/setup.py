from setuptools import find_packages, setup


with open("README.md", "r", encoding="utf-8") as file:
    README = file.read()


setup(
    name="cmdargparse",
    version="0.1.0",
    description="A declarative way to define `cmd2` argument parsers.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Kilian Kaiping (krnd)",
    url="https://github.com/krnd/cmdargparse",
    license="MIT",
    packages=find_packages(include=["cmdargparse"]),
    # Tested with Python 3.13 only.
    python_requires=">=3.13",
    install_requires=[
        ("cmd2" "~=2.7"),
    ],
    keywords=[
        "CLI",
        "cmd",
        "command",
        "interactive",
        "prompt",
        "Python",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
