from setuptools import setup, find_packages

setup(
    name='models_lib',
    version='0.1.0',
    description='Reusable SQLAlchemy models for Flask apps',
    author='dulguun',
    packages=find_packages(),
    install_requires=[
        'Flask>=2.0',
        'Flask-SQLAlchemy>=3.0',
        'sqlalchemy_serializer',
    ],
    python_requires='>=3.8',
)
