import setuptools

setuptools.setup(
    name='mkdir',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
