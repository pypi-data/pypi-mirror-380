from setuptools import setup, find_packages

setup(
    name="gitbaba",
    version="0.1.2",
    description="A lightweight CLI tool to simplify GitHub workflows. With GitBaba you can push local projects, create new repositories, delete repos, and manage authentication without typing long Git or GitHub commands. Perfect for developers who want a faster shortcut to manage GitHub projects.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="BotolMehedi",
    author_email="hello@mehedi.fun",
    url="https://github.com/BotolMehedi/gitbaba",
    packages=find_packages(),
    install_requires=["requests>=2.28.0", "colorama>=0.4.6"],
    entry_points={
        "console_scripts": [
            "gitbaba=gitbaba.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Utilities",
    ],
)
