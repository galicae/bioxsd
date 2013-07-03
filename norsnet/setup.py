#/usr/bin/python

from setuptools import setup
setup(	name='norsexml',
		version='0.1',
		description='Python script that creates BioXSD compliant XML from norsnet output.',
		author='Nikolaos Papadopoulos',
		author_email='papadopn@in.tum.de',
		py_modules=['norsexml'],
		scripts=['norsexml'],
		requires=['argparse', 'lxml'])
