//
// Created by user on 11/27/18.
//

#include "GeoCore.h"


void GeoCore::income(float a) {
    GeoCore::bank += a;
}

void GeoCore::expense(float a) {
    GeoCore::bank -= a;
}