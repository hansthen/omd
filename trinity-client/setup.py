#!/usr/bin/env python
from distutils.core import setup

setup ( 
  name='Trinity-Client',
  version='0.1.0',
  description='Python client for the Trinity API',
  url='http://www.clustervision.com',
  author='Abhishek Mukherjee',
  author_email='abhishek.mukherjee@clustervision.com',
  packages=['trinity-client'],
  package_dir={'trinity-client':'src'},
  data_files=[
    ('/etc/trinity',['conf/trinity-client.conf'])
  ]
)
