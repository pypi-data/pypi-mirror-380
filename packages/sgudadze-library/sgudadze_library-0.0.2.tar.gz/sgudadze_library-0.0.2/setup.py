import setuptools



setuptools.setup(
    name="sgudadze_library",  # <-- შეცვალეთ your_username
    version="0.0.2",
    author="Sandro",
    author_email="aleksandre.gudadze.2@iliauni.edu.ge",
    description="A simple package with a Base class",
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/mybasepack", # თქვენი პროექტის ბმული
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)