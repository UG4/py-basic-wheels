from skbuild import setup  # This line replaces 'from setuptools import setup'
setup(
    name="ug4",
    version="0.0.1",
    description="a minimal example package (cpp version)",
    author='The scikit-build team',
    license="MIT",
    packages=['ugcore'],
    python_requires=">=3.10",
    # cmake_source_dir="ugcore",
    # cmake_args=['-DPARALLEL:BOOL=OFF','-DLimex:BOOL=ON', '-DCPU=1', '-DDIM=2']
    cmake_args=['-DPARALLEL:BOOL=OFF','-DLimex:BOOL=OFF', '-DCPU=1', '-DDIM=2', '-DSTATIC_BUILD:BOOL=ON']
)
