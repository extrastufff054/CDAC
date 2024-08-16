# Packages required : 
1. <b>GMP or MPIR : </b> (I've used GMP) 

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
    
    You can download MPFR from https://www.mpfr.org/mpfr-current/mpfr-4.2.1.tar.xz or the official website (https://www.mpfr.org/)

    
3. <b>QD</b> :
4. <b>fplll</b> :