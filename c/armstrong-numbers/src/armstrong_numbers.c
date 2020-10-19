#include "armstrong_numbers.h"
#include <math.h> 

bool is_armstrong_number(int candidate) {
    int digits = 0;

    for (int aux = candidate; aux != 0; aux /= 10)
        digits++;

    double sum = 0;
    for (int aux = candidate; aux != 0; aux /= 10)
        sum += pow(aux % 10, digits);

    if ((int) sum == candidate)
        return true;
    return false;
}
