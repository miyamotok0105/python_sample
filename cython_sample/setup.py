#! -*- coding: utf-8 -*-
#python setup.py build_ext --inplace
from Cython.Build import cythonize
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np

try:
    numpy_include = np.get_include()
except AttributeError:
    numpy_include = np.get_numpy_include()


ext_modules = [
    Extension(
        "sample1",
        ["sample1.pyx"],
        include_dirs=[numpy_include]
    )
]
setup(
    name='sample1',
    ext_modules=cythonize(ext_modules),
)



# ext_modules = [
#     Extension( "sample1", ["sample1.pyx"] ),
# ]

# setup(
#     name = "Sample sample1 app",
#     cmdclass = { "build_ext" : build_ext },
#     ext_modules = ext_modules,
# )
