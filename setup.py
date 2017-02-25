# -*- coding: utf-8 -*-

from distutils.core import setup

with open('requirements.txt') as reqs:
    requirements = reqs.read().split()

setup(
    name='pybrdst',
    packages=['pybrdst'],  # this must be the same as the name above
    version='0.1',
    description='Brazilian daylight saving time',
    author='João Carlos Mendes',
    author_email='joaocarlos.tmendes@gmail.com',
    url='https://github.com/joaocarlosmendes/pybrdst',
    download_url='https://github.com/joaocarlosmendes/pybrdst/releases/tag/0.1',
    install_requires=requirements,  # noqa
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    keywords=['DST',
              'brazilian',
              'daylight',
              'saving',
              'horário',
              'verão',
              'brasileiro'],
    classifiers=[],
    )
