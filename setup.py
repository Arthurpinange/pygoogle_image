from setuptools import setup, find_packages

_long_description = ''
with open("README.md", "r", encoding="utf-8") as fh:
    _long_description = fh.read()

setup_args = dict(name='pygoogle_image',
      version='1.0.0',
      description='the package downloads images from google images',
      long_description=_long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/Arthurpinange/pygoogle_image',
      author='Arthur Pinangé',
      author_email='arthur.pinange@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False)

install_requires = ['python-magic', 'progressbar', 'urllib3', 'requests']

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)

