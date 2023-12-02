""" from https://github.com/jaywalnut310/glow-tts """

from distutils.core import setup
from Cython.Build import cythonize
import numpy
from model.monotonic_align.core import maximum_path_c

setup(
    name = 'monotonic_align',
    ext_modules = cythonize("core.pyx"),
    include_dirs=[numpy.get_include()]
)
