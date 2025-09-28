from setuptools import setup, Extension
import sys, platform

compile_args = []
link_args = []
libraries = []

if platform.system() == "Windows":
    compile_args += ["/O2", "/fp:precise"]
else:
    compile_args += [
        "-O3",
        "-std=c11",
        "-fno-trapping-math",
        "-fexcess-precision=standard",
        "-ffp-contract=off",
    ]
    libraries.append("m")  # link libm for sqrt/cbrt/fma/nearbyint on POSIX

ext = Extension(
    name="accurpy._fm",
    sources=["src/accurpy/_fm.c"],
    extra_compile_args=compile_args,
    extra_link_args=link_args,
    libraries=libraries,
)

setup(
    ext_modules=[ext],
    zip_safe=False,
)
