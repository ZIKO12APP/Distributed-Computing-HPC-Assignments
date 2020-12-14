from setuptools import Extension, setup
import numpy

extension_mod = Extension("mod_wi8cexzk",
		[ r'mod_wi8cexzk_wrapper.c' ],
		extra_objects = [r'/home/mohammed/CHPC1/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__/bind_c_mod_wi8cexzk.o',
				r'/home/mohammed/CHPC1/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__/mod_wi8cexzk.o'],
		include_dirs = [r'/home/mohammed/CHPC1/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__', numpy.get_include()],
		libraries = [r'gfortran'],
		library_dirs = [r'/usr/lib/gcc/x86_64-linux-gnu/9'],
		extra_link_args = [r'-O3',
				r'-fPIC',
				r'-I"/home/mohammed/CHPC1/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__"'])

setup(name = "mod_wi8cexzk", ext_modules=[extension_mod])