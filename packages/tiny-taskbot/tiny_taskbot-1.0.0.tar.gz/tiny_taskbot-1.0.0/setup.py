from setuptools import setup, find_packages

setup(
    name="tiny-taskbot",
    version="1.0.0",
    author="dmx3377",
    author_email="david@dmx3377.uk",
    description="A lightweight Python scheduler for timer and file-change tasks.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://gitlab.com/dmxsoftware/tiny-taskbot",
    project_urls={
        "Homepage": "https://tinytaskbot.dmx3377.uk/",
        "Source": "https://gitlab.com/dmxsoftware/tiny-taskbot",
        "Documentation": "https://gitlab.com/dmxsoftware/tiny-taskbot/README.md",
        "Bug Tracker": "https://gitlab.com/dmxsoftware/tiny-taskbot/-/issues"
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "tiny_taskbot": [],
    },
    python_requires=">=3.7",
    install_requires=[
        "rich",
        "watchdog",
        "schedule",
        "plyer"
    ],
    entry_points={
        "console_scripts": [
            "tiny-taskbot=tiny_taskbot.bot:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
