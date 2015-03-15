#!/usr/bin/env python

from setuptools import setup

setup(name="urlfinder",
      version="0.8.0",
      description="Parse out URLs in a chunk of text",
      author="Matthew Gamble",
      author_email="git@matthewgamble.net",
      url="https://github.com/djmattyg007/urlfinder",
      download_url="https://github.com/djmattyg007/urlfinder/archive/0.8.0.zip",
      packages=['urlfinder'],
      scripts=['bin/urlfinder'],
      package_data={'urlfinder': ['README.rst']},
      data_files=[('share/doc/urlfinder', ['README.rst', 'COPYING']),
                  ('share/man/man1', ['urlfinder.1'])],
      license="GPLv2",
      install_requires=[]
      )
