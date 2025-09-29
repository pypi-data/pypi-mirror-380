from setuptools import setup, find_packages

setup(
    name='lady-epe',
    version='0.1.0',
    packages=find_packages(),
    description='Framework simbólico para auditoria de modelos com métricas de divergência temporal',
    author='Cesar Rúbio',
    author_email='teu@email.com',
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
