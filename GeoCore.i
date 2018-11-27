/* File: example.i */
%module Core

%{
#define SWIG_FILE_WITH_INIT
#include "GeoCore.h"

%}

class GeoCore {
public:
    float bank = 0;
    void income(float);
    void expense(float);
};