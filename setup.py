from setuptools import setup, find_namespace_packages


with open('README.md', 'r') as fh:
    readme = "\n" + fh.read()

setup(
    name='pytablericons',
    version='1.0.0',
    author='Niklas Henning',
    author_email='business@niklashenning.com',
    license='MIT',
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "pytablericons.icons.filled": ["*.svg"],
        "pytablericons.icons.outline": ["*.svg"],
    },
    install_requires=[
        'pygame>=2.5.2',
        'Pillow>=9.5.0'
    ],
    python_requires='>=3.7',
    description='A Python wrapper for the Tabler Icons library with 5237 high-quality icons',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/niklashenning/pytablericons',
    keywords=['python', 'icon', 'icons', 'svg', 'tabler-icons'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License'
    ]
)
