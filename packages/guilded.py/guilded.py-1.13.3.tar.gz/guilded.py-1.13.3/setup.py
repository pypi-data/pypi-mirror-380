import re
import setuptools

with open('README.md', 'r') as rmd:
    long_description = rmd.read()

version = ''
with open('guilded/__init__.py') as initpy:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', initpy.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Version is not set.')

extras_require = {
    'docs': [
        'sphinx==4.4.0',
        'sphinxcontrib_trio==1.1.2',
        'sphinxcontrib-websupport',
        'typing-extensions>=4.3,<5',
    ],
}

setuptools.setup(
    name='guilded.py',
    version=version,
    author='shay (shayypy)',
    description='An API wrapper in Python for Guilded\'s bot API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/shayypy/guilded.py',
    project_urls={
        'Documentation': 'https://guildedpy.readthedocs.io/en/latest/',
        'Issue tracker': 'https://github.com/shayypy/guilded.py/issues',
    },
    packages=[
        'guilded',
        'guilded.types',
        'guilded.webhook',
        'guilded.ext.commands',
        'guilded.ext.tasks',
    ],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English'
    ],
    python_requires='>=3.8.0',
    install_requires=['aiohttp'],
    extras_require=extras_require,
)
