from setuptools import setup, find_packages
from codecs import open

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

# Remove PyTorch and Torchvision from install requirements to handle manually
install_reqs = parse_requirements("requirements.txt")

setup(
    name = 'MedImageInsights',

    version = '0.1.0',

    author = 'Joaquin Ortiz de Murua Ferrero',
    author_email = 'joortif@unirioja.es',
    maintainer= 'Joaquin Ortiz de Murua Ferrero',
    maintainer_email= 'joortif@unirioja.es',

    url='https://github.com/joortif/MedImageInsights',

    description = 'Library for MedImageInsight: Open-Source Medical Image Embedding Model',

    long_description_content_type = 'text/markdown', 
    long_description = long_description,

    license = 'MIT license',

    packages = find_packages(include=["*"],exclude=["test"]), 
    install_requires = install_reqs,
    python_requires='>=3.8.19',
    include_package_data=True, 

    classifiers=[

        'Development Status :: 4 - Beta',

        'Programming Language :: Python :: 3.10',

        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',       

        # Topics
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',

        "Operating System :: OS Independent",
    ],

    keywords='computer vision embedding medical images model open-source'
)