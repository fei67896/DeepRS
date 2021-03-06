import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIRED_PACKAGES = [
    'tensorflow>=1.12.1',
    'h5py'
]

setuptools.setup(
    name="DeepRS",
    version="0.0.1",
    author="YSZYCF",
    author_email="476900563@qq.com",
    description="Easy-to-use,Modular and Extendible package of deep learning based RS(Recommendation system) prediction models with tensorflow.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YSZYCF/DeepRS",
    download_url='https://github.com/shenweichen/deepctr/tags',
    packages=setuptools.find_packages(exclude=["tests", "tests.models"]),
    python_requires='>=3.4',  # 3.4.6
    install_requires=REQUIRED_PACKAGES,
    extras_require={
        "tf": ['tensorflow>=1.12.1'],
        "tf_gpu": ['tensorflow-gpu>=1.12.1'],
    },
    entry_points={
    },
    classifiers=(
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
    license="MIT license",
    keywords=['RS', 'Recommendation system',
              'deep learning', 'tensorflow', 'tensor', 'keras'],
)
