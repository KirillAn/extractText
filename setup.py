from setuptools import setup, find_packages

setup(
    name='text-extractor',
    version='0.1.0',
    author='KirillAn',
    author_email='kirillius.no@gmail.com',
    description='Библиотека для извлечения текста из файлов различных форматов',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://example.com/https://github.com/KirillAn/extractText/',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'ebooklib',
        'PyPDF2',
        'beautifulsoup4',
        'python-docx',
        'json',
    ],
    extras_require={
        'dev': [
            'pytest>=3.7',
        ],
    },
)
