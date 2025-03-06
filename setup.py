from setuptools import find_packages, setup
import os

# Read dependencies from requirements.txt
def read_requirements():
    if os.path.exists("requirements.txt"):
        with open("requirements.txt") as f:
            return f.read().splitlines()
    return []  # Return empty list if file is missing

setup(
    name="real_time_weather_forecasting",
    version="0.1.0",
    author="Fazeel Asghar",
    author_email="fasghar@example.com",
    description="A real-time weather forecasting system using MLOps principles",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Fazeel-AIML/Weather_Forcast_Deployed_MLOps.git",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=read_requirements(),  # Reads dependencies from requirements.txt
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
