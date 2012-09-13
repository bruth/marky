from setuptools import setup, find_packages

kwargs = {
    'packages': find_packages(),
    'py_modules': ['mdx_superscript', 'mdx_subscript', 'mdx_urlize'],
    'include_package_data': True,
    'install_requires': [
        'django',
        'markdown>=2.0',
        'pygments',
    ],
    'name': 'marky',
    'version': __import__('marky').get_version(),
    'author': 'Byron Ruth',
    'author_email': 'b@devel.io',
    'description': 'Markdown editor and previewer',
    'license': 'BSD',
    'keywords': 'markdown markup preview editor',
    'url': 'https://github.com/bruth/marky/',
    'classifiers': [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Topic :: Text Processing :: Markup',
    ],
}

setup(**kwargs)
