from setuptools import find_packages, setup
from typing import List
import io
import os


def get_requirements() -> List[str]:
    """
    Read requirements.txt and return list of requirements.
    Ignores empty lines and the '-e .' marker.
    """
    requirement_list: List[str] = []
    req_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
    try:
        with io.open(req_path, "r", encoding="utf8") as fh:
            for line in fh:
                requirement = line.strip()
                if not requirement or requirement.startswith("#"):
                    continue
                if requirement == "-e .":
                    continue
                requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirement_list


# Minimal metadata — edit these fields for your project
setup(
    name="network_security",
    version="0.0.1",
    author="Your Name",
    author_email="you@example.com",
    description="Network security data-science utilities and pipelines",
    long_description="Longer project description can go here or load from README.md",
    long_description_content_type="text/markdown",
    packages=find_packages(),            # finds all packages with __init__.py
    include_package_data=True,
    install_requires=get_requirements(), # dependencies from requirements.txt
    python_requires=">=3.10",            # set minimum Python version
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
