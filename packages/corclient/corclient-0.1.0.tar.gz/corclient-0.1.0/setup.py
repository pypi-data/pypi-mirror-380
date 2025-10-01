from setuptools import setup, find_packages

setup(
    name="corclient",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer>=0.12",
        "rich>=13",
        "flask>=2.3",
        "requests>=2.31"
    ],
    entry_points={
        "console_scripts": [
            "cor=corecli.cli:app"
        ]
    },
    python_requires=">=3.10",
    author="Carlos Ferrer",
    description="CLI para autenticarse con Cognito y ejecutar GraphQL (Amplify Gen2)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT"
)
