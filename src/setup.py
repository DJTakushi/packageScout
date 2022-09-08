from setuptools import setup

setup(name='packageScout',
      version='0.1',
      description="Parses /var/lib/dpkg/status (and/or any other needed files) and displays a list of packages explicitly installed by the user.",
      url='https://github.com/DJTakushi/packageScout"',
      author='Danny Takushi',
      author_email='dannytakushi@gmail.com',
      license='MIT',
      packages=['packageScout'],
      zip_safe=False)
