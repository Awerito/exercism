#include "resistor_color.h"
#include <stdio.h>

int color_code(resistor_band_t color) {
    return color;
}

const int _all_colors[] = {
    BLACK, BROWN, RED, ORANGE, YELLOW,
    GREEN, BLUE, VIOLET, GREY, WHITE
};

const int *colors() {
    return _all_colors;
}
