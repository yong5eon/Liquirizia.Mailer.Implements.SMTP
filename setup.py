# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

PKG = 'Liquirizia.Mailer.Implements.SMTP'
SRC = 'src'
EXCLUDES = []
DESC = 'Implmentation SendMail for SMTP of Mailer in Python Modernized Application Framework Liquirizia'
WHO = 'Heo Yongseon'

PKGS = [PKG]
DIRS = {PKG: SRC}
for package in find_packages(SRC, exclude=EXCLUDES):
	PKGS.append('{}.{}'.format(PKG, package))
	DIRS['{}.{}'.format(PKG, package)] = '{}/{}'.format(SRC, package.replace('.', '/'))

setup(
	name=PKG,
	description=DESC,
	long_description=open('README.md', encoding='utf-8').read(),
	long_description_content_type='text/markdown',
	author=WHO,
	author_email='labs@teamofmine.com',
	version=open('VERSION', encoding='utf-8').read(),
	packages=PKGS,
	package_dir=DIRS,
	include_package_data=False,
	classifiers=[
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
		'Programming Language :: Python :: 3.11',
		'Application Framework :: Liquirizia',
		'Application Framework :: Liquirizia :: Mailer',
		'Application Framework :: Liquirizia :: Mailer :: SMTP',

	],
	install_requires=[
		'Liquirizia.Mailer@git+https://github.com/yong5eon/Liquirizia.Mailer.git',
	],
	python_requires='>=3.8'
)
