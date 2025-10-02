from setuptools import setup, find_packages

setup(
    name="classifierPratik",                  # Your package name
    version="0.0.3",                          # Package version
    author="Pratik Chourasia",                # Your name
    author_email="pratikchourasia1@gmail.com",    # Optional
    description="Zero-shot classification package using Transformers",  # Short description
    long_description=open("usage.md").read(),  # Optional, detailed description
    long_description_content_type="text/markdown",
    url="https://github.com/PratikChrs/classifierPratik",  # Optional repo URL
    packages=find_packages(),                 # Automatically find packages in your project
    install_requires=[                        # Dependencies required to run your code
        "torch>=2.1.0",
        "transformers>=4.40.0",
        "huggingface_hub>=0.16.0",
        "pytest>=8.0.0",
        "numpy>=1.24.0"
    ],
    python_requires=">=3.10",
    classifiers=[                             # Optional metadata
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
