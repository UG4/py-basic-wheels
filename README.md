# ug4py-basic-wheels

[![Build wheels](https://github.com/UG4/py-basic-wheels/actions/workflows/wheels.yml/badge.svg)](https://github.com/UG4/ugpip/actions/workflows/wheels.yml)

This repository provides UG4 as Python modules. This includes:

 * ugcore: https://github.com/UG4/ugcore
 * ConvectionDiffusion: https://github.com/UG4/plugin_ConvectionDiffusion
 * Limex: https://github.com/UG4/plugin_Limex

Build is for DIM=2,3 and all CPU block types.


## Example

Installation is easy:
```
pip install ug4py-base
```

As an example, you can run an example solving the diffusion equation:
```
git clone https://github.com/UG4/py-course-modsim
cd py-course-modsim/content/skin
python3 SkinDiffusion.py
```

## License
* UG4 is available under LGPL v3.

## TODO:
Integration of SuperLU6 plugin:

* SuperLU6: https://github.com/UG4/plugin_SuperLU6
* SuperLU is available under a BSD 3-term license: https://github.com/xiaoyeli/superlu/blob/master/License.txt


## Local builds
This tool uses GitHub Actions. Consult https://nektosact.com/ for details on a local installation:

* act -P macos-14=-self-hosted 
* act --container-architecture linux/amd64
