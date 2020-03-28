from setuptools import setup
from os.path import abspath, dirname, join

this_dir = abspath(dirname(__file__))

with open(join(this_dir,'/README.md')) as readme:
    long_description = readme.read()

setup(
    name='compile_scss',
    version='0.0.1',
    description='Compile multiple SCSS files into a single CSS file',
    long_description = long_description,
    py_modules=['compile_scss.py'],
    package_dir={'':'src'}
)




# 
# setup(
#   name = 'compile_scss',
#   packages = ['compile_scss'],
#   version = '0.1',
#   license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
#   description = 'Compile multiple SCSS files into a single CSS file',
#   long_description='README.md',
#   author = 'Keegan Good',
#   author_email = 'keegood8@gmail.com',
#   url = 'https://github.com/dirtTastesGood/Python/tree/master/compile_scss',
#   download_url = 'https://github.com/dirtTastesGood/Python/archive/v0.1-alpha.tar.gz',
#   keywords = ['SCSS Compiler', 'SCSS', 'CSS'],
#   install_requires=[            # I get to this in a second
#           'os',
#           'sys',
#           'shutil',
#           'sass',
#       ],
#   classifiers=[
#     'Development Status :: 3 - Alpha',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
#     'Intended Audience :: Developers',
#     'Topic :: Software Development :: Build Tools',
#     'License :: OSI Approved :: MIT License',
#     'Programming Language :: Python :: 3',
#     'Programming Language :: Python :: 3.4',
#     'Programming Language :: Python :: 3.5',
#     'Programming Language :: Python :: 3.6',
#     'Programming Language :: Python :: 3.8',
#   ],
# )