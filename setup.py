# Copyright (c) 2020 - 2022 Open Risk (https://www.openriskmanagement.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from codecs import open

from setuptools import setup

__version__ = '0.3'

ver = __version__

long_descr = open('docs/source/description.rst', 'r', encoding='utf8').read()

setup(name='equinox-server',
      version=ver,
      description='An open source platform for sustainable finance',
      long_description=long_descr,
      long_description_content_type='text/x-rst',
      author='Open Risk',
      author_email='info@openrisk.eu',
      packages=['equinox'],
      include_package_data=True,
      url='https://github.com/open-risk/equinox',
      install_requires=[
          'Django'
      ],
      zip_safe=False,
      provides=['equinox'],
      keywords=['sustainable finance', 'ghg emissions', 'pcaf', 'eeio', 'portfolio', 'loan', 'database'],
      classifiers=[
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Intended Audience :: Financial and Insurance Industry',
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.9',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Information Analysis'
      ]

      )
