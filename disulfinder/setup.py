#/usr/bin/python

from setuptools import setup
setup(	name='disulfxml',
	version='0.1',
	description='Python script that creates BioXSD compliant XML from disulfinder output.',
	author='Alexander Betz',
	author_email='alexander.betz@gmail.com',
	py_modules=['disulfxml'],
	scripts=['disulfxml'],
	requires=['optparse', 'lxml', 'collections'])
