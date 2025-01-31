# Installation

## Step 1: Install RAPID

### Before Installation Steps:

#### Ubuntu:

```bash
sudo apt-get install gfortran g++
sudo apt-get install make
sudo apt-get install libnetcdf-dev libnetcdff-dev netcdf-bin
```

#### RedHat/CentOS:

```bash
sudo yum install gcc-c++ gcc-gfortran
```
# Windows with Cygwin

Downloaded Cygwin (64-bit) (https://www.cygwin.com/) with these dependencies:

- gcc-core
- gcc-fortran
- gcc-g++
- gdb
- git
- make
- time
- wget

## Installation Steps

### Manual

- See: [http://rapid-hub.org](http://rapid-hub.org)

### Bash

1. Clone RAPID repository:

    ```bash
    git clone https://github.com/c-h-david/rapid.git
    ```

2. Create `installz` directory:

    ```bash
    mkdir ~/installz
    ```

3. Install Prereqs. Make sure to replace your path with "path/to/installz":

    ```bash
    cd rapid
    chmod u+x rapid_install_prereqs.sh
    ./rapid_install_prereqs.sh -i="path/to/installz"
    ```

4. Append `source rapid_specify_varpath.sh` to the `~/.bashrc` or `~/.bash_profile`. Replace with your path to rapid_specify_varpath.sh:

    ```bash
    source /path/to/cloned/rapid/rapid_specify_varpath.sh
    ```

5. Restart Terminal

6. Set up environment variables:

    ```bash
    export NETCDF_LIB='-L /usr/lib -lnetcdff'
    export NETCDF_INCLUDE='-I /usr/include'
    export PETSC_DIR=$HOME/installz/petsc-3.13.6
    export PETSC_ARCH=linux-gcc-c
    export PATH=$PATH:$PETSC_DIR/$PETSC_ARCH/bin
    ```

7. Build RAPID:

    ```bash
    cd rapid/src
    make rapid
    ```


## Step 2: Install RAPIDpy

Due to the dependencies required, we recommend using Anaconda or Miniconda.  
They can be downloaded from [https://www.continuum.io/downloads](https://www.continuum.io/downloads)  
or from [https://conda.io/miniconda.html](https://conda.io/miniconda.html).

---

This is how you get the most up-to-date version of the code.

> **Note:** If you don't have git, you can download the code from [https://github.com/erdc/RAPIDpy](https://github.com/erdc/RAPIDpy)

```bash
git clone https://github.com/erdc/RAPIDpy.git
cd RAPIDpy
conda env create -f rapidpy_env.yml
conda activate rapidpy_env
python setup.py install
```

To develop on the latest version:

```bash
git clone https://github.com/erdc/RAPIDpy.git
cd RAPIDpy
conda env create -f rapidpy_env.yml
conda activate rapidpy_env
python setup.py develop
```

### Install Development Version of RAPIDpy

To install the latest development version of RAPIDpy from the GeoGLOWS repository, run the following commands in your terminal:

```bash
git clone https://github.com/geoglows/RAPIDpy.git
cd RAPIDpy
pip install -e .
```

