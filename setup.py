from setuptools import setup, find_packages

classifiers = [
    'Development Status :: Production',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10'
]

setup(
    name='ISO-8859-8 decoder encoder',
    version='0.0.1',
    description='a very standard ISO-8859-8 decoder and encoder',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='david',
    author_email='',
    license='MIT',
    classifiers=classifiers,
    keywords='ISO-8859',
    packages=find_packages(),
    install_requires=['']
)