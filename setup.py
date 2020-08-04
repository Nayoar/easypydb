from distutils.core import setup
setup(
  name = 'easypydb',
  packages = ['easypydb'],
  version = '0.1',
  license='MIT',
  description = 'Simple and easy-to-use python database',
  author = 'minx28',
  author_email = 'minx8128@gmail.com',
  url = 'https://github.com/minx28/easypydb',
  download_url = 'https://github.com/minx28/easypydb/archive/v_01.tar.gz',
  keywords = ['database', 'db', 'easy', 'simple'],
  install_requires=[
          's1db',
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)