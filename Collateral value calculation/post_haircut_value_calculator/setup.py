from setuptools import setup, find_packages

setup(
    name="post_haircut_value_calculator",  # Package name
    version="1.0.0",  # Version number
    description="A tool to calculate post-haircut values for securities and generate notifications.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Gouree",
    author_email="goureeg@gmail.com",
    url="https://github.com/GoGouree/collateral-value-calculator/tree/main",  # Replace with your repository URL
    packages=find_packages(where="src"),  # Look for packages in the 'src' directory
    package_dir={"": "src"},  # Root package directory is 'src'
    install_requires=[
        "pandas>=1.0.0",  # Add other dependencies here
    ],
    entry_points={
        "console_scripts": [
            "post_haircut_value_calculator=main:main",  # Command-line entry point
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Specify the minimum Python version
)
