from io import open
from setuptools import setup

with open('README.md', encoding='utf-8') as read_me:
    long_description = read_me.read()

setup(
    name='Vit3l',
    version='0.22.0',
    author='Juan Brotenelle',
    author_email='andrey.evstratenkov@mail.ru',
    url='https://github.com/JuanBrotenelle/vit3l',
    project_urls={
        'Homepage': 'https://github.com/JuanBrotenelle/vit3l',
        'Documentation': 'https://github.com/JuanBrotenelle/vit3l#readme',
        'Repository': 'https://github.com/JuanBrotenelle/vit3l',
        'Issues': 'https://github.com/JuanBrotenelle/vit3l/issues',
        'Changelog': 'https://github.com/JuanBrotenelle/vit3l/blob/main/CHANGELOG.md',
    },
    packages=['vit3l'],
    package_data={
        'vit3l': ['eel.js', 'py.typed'],
    },
    install_requires=[
        'bottle>=0.12.0',
        'bottle-websocket>=0.2.0',
        'future>=0.18.0',
        'pyparsing>=2.0.0',
        'typing-extensions>=4.0.0',
        'importlib-resources>=5.0.0',
    ],
    extras_require={
        "jinja2": ['jinja2>=2.10'],
        "dev": [
            'pytest>=6.0',
            'pytest-cov>=2.0',
            'black>=22.0',
            'flake8>=4.0',
            'mypy>=0.900',
            'pre-commit>=2.0',
        ],
    },
    python_requires='>=3.7',
    description='Fork of Eel with Vite HMR support for modern web development',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['gui', 'html', 'javascript', 'electron', 'vite', 'hmr', 'webpack'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    entry_points={
        'console_scripts': [
            'vit3l=vit3l.__main__:main',
        ],
    },
)
