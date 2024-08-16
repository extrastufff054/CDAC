# Packages required : 

Installation of ```fpylll``` can be only done after installing the below packages. 

fpylll can be installed using ```pip install fpylll```.

Note : fpylll may not work even after following the below steps.
1. <b>GMP or MPIR : </b> (I've used GMP) 

    For arbitrary precision integer arithmetic.

    You can download the tar.xz file from  https://gmplib.org/download/gmp/gmp-6.3.0.tar.xz or the official website (https://gmplib.org/)

    * Installing GMP
    * GMP has an autoconf/automake/libtool based configuration system. On a Unix-like system a basic build can be done with 
        ```
         ./configure
          make
         ```
    
    
    
    * Some self-tests can be run with
        ```
         make check 
        ```


    * And you can install (under /usr/local by default) with
        ```
         make install
        ```

2. <b> MPFR </b> :

    For arbitrary precision floating point arithmetic.
    
    You can download MPFR from https://www.mpfr.org/mpfr-current/mpfr-4.2.1.tar.xz or the official website (https://www.mpfr.org/)

    
    * The MPFR library is already installed on some GNU/Linux distributions, but the development files necessary to the compilation such as ```mpfr.h``` are not always present. 
    * To check that MPFR is fully installed on your computer, you can check the presence of the file mpfr.h in /usr/include, or try to compile a small program having ```#include <mpfr.h>``` (since mpfr.h may be installed somewhere else). 
    * For instance, you can try to compile:
        ```
        #include <stdio.h>
        #include <mpfr.h>
        int main (void)
        {
        printf ("MPFR library: %-12s\nMPFR header:  %s (based on %d.%d.%d)\n",
                mpfr_get_version (), MPFR_VERSION_STRING, MPFR_VERSION_MAJOR,
                MPFR_VERSION_MINOR, MPFR_VERSION_PATCHLEVEL);
        return 0;
        }
        ```
        with

        ```
        cc -o version version.c -lmpfr -lgmp
        ```
        and if you get errors whose first line looks like

        version.c:2:19: error: mpfr.h: No such file or directory
        then MPFR is probably not installed. Running this program will give you the MPFR version.

    * If MPFR is not installed on your computer, or if you want to install a different version, please follow the steps same as in GMP.


3. <b>QD</b> :

    For double double and quad double arithmetic (optional).

    You can download it from here https://www.davidhbailey.com/dhbsoftware/qd-2.3.24.tar.gz or the official website (https://www.davidhbailey.com/dhbsoftware/)

4. <b>fplll</b> :

    For pretty much everything.

    You can follow the installation guide on fplll on the repository
    https://github.com/fplll/fplll?tab=readme-ov-file#Installation-from-packages

### fpylll also relies on

* <b>Cython</b> : 

    For linking Python and C/C++.
    
    Installation : http://cython.org/ or https://pypi.org/project/Cython/

* <b>cysignals </b> : 

    For signal handling such as interrupting C++ code.

    Installation : https://github.com/sagemath/cysignals or https://pypi.org/project/cysignals/

* <b>py.test </b>

    For testing Python.

    Installation : https://pytest.org/en/7.4.x/getting-started.html
 
* <b>flake8 </b>

    For linting.