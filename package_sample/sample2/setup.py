from setuptools import setup, find_packages

setup(
    name='gcp_ocr_package',
    version="0.0.1",
    description="",
    long_description="",
    author='',
    license='MIT',
    classifiers=[
        "Development Status :: 1 - Planning"
    ],
    keywords='',
    install_requires=[
       'google-cloud-vision==0.30.1',
       'pillow==8.1.1'
    ]
)