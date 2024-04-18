from skbuild import setup  # This line replaces 'from setuptools import setup'
setup(
    name="ugcore-cpp",
    version="1.2.3",
    description="a minimal example package (cpp version)",
    author='The scikit-build team',
    license="MIT",
    packages=['ugcore'],
    python_requires=">=3.7",
    # cmake_source_dir="ugcore",
    cmake_args=['-DPARALLEL:BOOL=OFF','-DLIMEX=ON']
)
