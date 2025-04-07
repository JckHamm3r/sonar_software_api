from setuptools import setup, find_packages

setup(
    name="sonar_software_api",
    version="0.1.0",
    description="A simple GraphQL client for interacting with your Sonar Software instance",
    author="Jckhmr",
    packages=find_packages(),
    install_requires=[
        "gql",  # Or whatever version you're using
        "requests_toolbelt"
    ],
    python_requires=">=3.7",
)
