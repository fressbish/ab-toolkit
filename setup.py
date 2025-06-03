from setuptools import setup, find_packages

setup(
    name='kda_ab_toolkit',
    version='0.1.6',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'matplotlib',
        'seaborn',
        'statsmodels',
        'plotly',
    ],
    author='Dmitry Koptev',
    author_email='flme.ya@yandex.ru',
    description='A/B Testing Toolkit with CUPED, bootstrapping, and more.',
    long_description='An experimental analysis toolkit for A/B testing with support for variance reduction techniques like CUPED and bootstrapping.',
    long_description_content_type='',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
