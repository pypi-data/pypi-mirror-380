from setuptools import setup, find_namespace_packages

setup(
    name="polychromy",
    packages=find_namespace_packages(
        include=["polychromy", "polychromy.*"],
        exclude=["images", "VE_polychromy"]
    ),
    include_package_data=True,  # Picks up MANIFEST.in if present
    install_requires=[
        "textlinebreaker>=1.0.0",
        "requests",
    ],
    package_data={
        "polychromy": ["data/colors.json"],  # Explicit data file(s)
    },
    python_requires=">=3.9",
)
