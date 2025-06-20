import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme_file:
    README = readme_file.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-pluggable-dashboard',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  # Update if you have a different license
    description='A pluggable Django app for a dynamic admin dashboard.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://example.com/', # Replace with your project's URL
    author='Your Name', # Replace with your name
    author_email='your.email@example.com', # Replace with your email
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 4.0',  # Adjust Django version as needed
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', # Update if you have a different license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=3.2', # Specify your Django compatibility
    ],
)
