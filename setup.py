import setuptools
# python setup.py develop
setuptools.setup(
    name            = "[project_name]",
    version         = "0.0.1",
    author          = "[author_name]",
    author_email    = "[email]",
    description     = "[description]",
    url             = "[github_url]",
    project_urls    = {"Bug Tracker": "[github_url]/issues",
    },
    classifiers     = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.6",
)