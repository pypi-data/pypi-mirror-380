from setuptools import setup, find_packages

setup(
    name="npck",          # ✅ new PyPI package name
    version="0.1.0",      
    packages=find_packages(),  # auto-detects npck/ folder
    install_requires=[],  
    description="",       
    author="Your Name",
    author_email="you@example.com",
    url="",               
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
