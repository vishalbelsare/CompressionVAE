import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cvae-maxfrenzel",
    version="0.0.1",
    author="Max Frenzel",
    author_email="maxfrenzel@gmail.com",
    description="General purpose dimensionality reduction and manifold learning tool based on Variational Autoencoder.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maxfrenzel/CompressionVAE",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'matplotlib',
        'joblib',
        'tensorflow>=1,<2'
    ],
    keywords='vae variational autoencoder manifold dimensionality reduction compression'
)