from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='aiocfscraper',
    version='1.2.71',
    author='bolone-sengkuni',
    author_email='',
    description='A Python module to bypass Cloudflare\'s anti-bot page.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bolone-sengkuni/aio-cloudscraper',
    project_urls={
        'Bug Tracker': 'https://github.com/bolone-sengkuni/aio-cloudscraper/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data = True,
    install_requires = ['aiohttp'],
    python_requires='>=3.6'
)