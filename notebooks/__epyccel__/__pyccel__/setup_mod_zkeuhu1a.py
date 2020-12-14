from setuptools import Extension, setup
import numpy

extension_mod = Extension("mod_zkeuhu1a",
		[ r'mod_zkeuhu1a_wrapper.c' ],
		extra_objects = [r'/home/mohammed/CHPC1/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__/bind_c_mod_zkeuhu1a.o',
				r'/home/mohammed/CHPC1/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__/mod_zkeuhu1a.o'],
		include_dirs = [r'/home/mohammed/CHPC1/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__', numpy.get_include()],
		libraries = [r'gfortran'],
		library_dirs = [r'/usr/lib/gcc/x86_64-linux-gnu/9'],
		extra_link_args = [r'-O3',
				r'-fPIC',
				r'-I"/home/mohammed/CHPC1/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__"'])

setup(name = "mod_zkeuhu1a", ext_modules=[extension_mod])