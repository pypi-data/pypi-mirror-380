from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='decisions-trees-felipe-puc',  # Nome do seu pacote
    version='0.1.0',                # Versão inicial
    author='Felipe Silva Faria',               # Seu nome
    author_email='felipesilfaria@gmail.com',
    description='Implementação e comparação de algoritmos de árvore de decisão (ID3, C4.5, CART) no dataset do Titanic.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/felipefaaria/IA',  # Substitua pelo link do seu GitHub
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pandas',
        'numpy',
        'requests',
        'scikit-learn',
        'scipy',
    ],
)