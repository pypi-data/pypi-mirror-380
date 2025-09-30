from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='oprouter',
    version='1.0.1',
    author='Maehdakvan',
    author_email='visitanimation@google.com',
    description='A Python library for chatting with AI models through OpenRouter',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DedInc/oprouter',
    project_urls={
        'Bug Tracker': 'https://github.com/DedInc/oprouter/issues',
        'Documentation': 'https://github.com/DedInc/oprouter#readme',
        'Source Code': 'https://github.com/DedInc/oprouter',
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    keywords='openrouter, ai, llm, chatbot, api, async',
    packages=find_packages(exclude=['tests', 'tests.*', 'examples']),
    include_package_data=True,
    install_requires=[
        'aiohttp',
        'asyncio_throttle',
        'tenacity',
        'rich',
        'pydantic',
        'pydantic-settings',
        'python-dotenv',
        'tiktoken',
        'click',
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'oprouter=oprouter.ui.cli:main',
        ],
    },
)