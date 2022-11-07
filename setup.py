import setuptools

__version__ = 'VERSIONADDEDBYGITHUB'

__title__ = "easyclient"
__author__ = 'Nate Harris'
__author_email__ = 'n8gr8gbln@gmail.com'
__github_username__ = "nwithan8"
__github_repo__ = "easyclient"
__copyright__ = "Copyright © YEARADDEDBYGITHUB - Nate Harris"
__license__ = 'GNU General Public License v3 (GPLv3)'
__description__ = "A simple boilerplate for making REST API clients."
__keywords__ = ["API", "client", "JSON", "Pydantic", "REST", "boilerplate"]

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = [
    "objectrest==2.0.*",
    "pytz==2022.1.*",
    "packaging==21.3.*",
    "typing-extensions"
]

DEV_REQUIREMENTS = [
    "black",
    "flake8",
    "isort",
    "pytest-cov==3.*",
    "pytest-vcr==1.*",
    "pytest==7.*",
    "types-requests",
    "types-urllib3",
    "vcrpy==4.*",
]

setuptools.setup(
    name=__title__,
    packages=setuptools.find_packages(exclude=["tests"]),
    version=__version__,
    license=__license__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=__author__,
    author_email=__author_email__,
    url=f'https://github.com/{__github_username__}/{__github_repo__}',
    download_url=f'https://github.com/{__github_username__}/{__github_repo__}/archive/refs/tags/{__version__}.tar.gz',
    keywords=__keywords__,
    install_requires=REQUIREMENTS,
    extras_require={
        "dev": DEV_REQUIREMENTS,
    },
    test_suite="test",
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 4 - Beta',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',  # Specify which python versions that you want to support
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia',
        'Topic :: Internet :: WWW/HTTP',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.7, <4'
)
