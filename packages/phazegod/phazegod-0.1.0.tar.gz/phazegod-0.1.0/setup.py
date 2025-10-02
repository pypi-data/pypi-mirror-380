from setuptools import setup

setup(
    name='phazegod',  # Your package name
    version='0.1.0',
    py_modules=['phazegod'],  # Your main script file without the .py extension
    author='Shaurya',
    author_email='your-email@example.com',  # Replace or remove if private
    description='Command-line tool by Phazegod (Shaurya)',
    long_description='A simple CLI tool with Phazegod branding and pip installer hint for Zenpo.',
    long_description_content_type='text/markdown',
    url='https://github.com/YOUR_USERNAME/phazegod',  # Replace with your GitHub repo
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Or whatever license you're using
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'phazegod = phazegod:main',
        ],
    },
)
