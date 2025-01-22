from setuptools import setup, find_packages

setup(
    name='appointment-manager',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'Flask-JWT-Extended',
        'Celery',
        'redis',
    ],
    entry_points={
        'console_scripts': [
            'appointment-manager=app:run',
        ],
    },
    include_package_data=True,
    description='A Flask-based appointment manager with job scheduling.',
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
