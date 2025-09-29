from setuptools import setup, find_packages

setup(
    name='langlint',
    version='0.1.0-dev',
    packages=find_packages(),
    description='A lightweight language linter',
    long_description='A lightweight language linter with extensible architecture',
    author='LangLint Team',
    author_email='langlint@example.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[],
)

