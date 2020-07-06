from setuptools import setup , find_namespace_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='mlderes.dstoolkit',
version='0.1',
 description='',
 package_dir={"":'src'},
 packages=find_namespace_packages(where='src',include='mlderes.*'), # Telling the Disttools that the default directory is 'src'
 author='Michael Dereszynski',
 author_email='mlderes@gmail.com',
 long_description=long_description,
 long_description_content_type='text/markdown',
 zip_safe=False)
