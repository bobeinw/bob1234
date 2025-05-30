from setuptools import setup, find_packages

setup(
    name='ne-lib',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['requests'],
    author='ali kamel',
    author_email='sad.bsndi@gmail.com',
    description='Tool with auto file detection and Telegram send function',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/ne-lib',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
