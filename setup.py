from setuptools import setup, find_packages


setup_args = dict(name='pygoogle_image',
      version='1.1',
      description='the package downloads images from google images',
      url='https://github.com/Arthurpinange/pygoogle_image',
      author='Arthur Pinangé',
      author_email='arthur.pinange@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False)

install_requires = ['python-magic-bin==0.4.14', 'progressbar', 'urllib3', 'requests']

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)

