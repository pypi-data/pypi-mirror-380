from setuptools import setup, find_packages

setup(
    name = 'STT_Pratyush1',
    version = '0.1',
    author = 'Pratyush Manna',
    author_email= 'prottus2004@gmail.com',
    description = 'Speech to Text'
)
packages = find_packages(),
install_requirements = [
    'selenium',
    'webdriver_manager'
]