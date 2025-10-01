"""Setup configuration for Django Template Integrator."""

from setuptools import setup, find_packages

setup(
    name="django-template-integrator",
    version="1.0.1",
    packages=find_packages(),
    install_requires=[
        "beautifulsoup4>=4.12.0",
    ],
    entry_points={
        'console_scripts': [
            'django-template-integrator=django_template_integrator.cli:main',
        ],
    },
)
