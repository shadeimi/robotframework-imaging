
#!/usr/bin/env python

from distutils.core import setup

CLASSIFIERS = """
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]

from os.path import join, dirname
long_description = open(join(dirname(__file__), 'README.rst',)).read()

setup(
    name='robotframework-Imaging',
    version="0.0.1",
    description='Robotframework utility keyworks for image comparing',
    long_description=long_description,
    author='Aniello Barletta',
    author_email='aniellob@gmail.com',
    url='https://github.com/shadeimi/robotframework-imaging',
    license='Beerware',
    keywords='robotframework testing testautomation web css webtest',
    platforms='any',
    zip_safe=False,
    classifiers=CLASSIFIERS.splitlines(),
    package_dir={'': 'src'},
    install_requires=['robotframework', 'robotframework-selenium2library', 'Pillow'],
    packages=['Imaging']
)