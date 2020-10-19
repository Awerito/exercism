#include "darts.h"
#include <math.h>

int score(coordinate_t pos) {
    double distance = sqrt(pos.x * pos.x + pos.y * pos.y);

    if (distance > 10.F)
        return 0;
    if (distance > 5.F)
        return 1;
    if (distance > 1.F)
        return 5;
    return 10;
}
