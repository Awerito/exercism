<?php

function distance(string $strandA, string $strandB) : int {

    $lengthA = strlen($strandA);
    $lengthB = strlen($strandB);

    if  ($lengthA == $lengthB) {
        $hamming_distance = 0;
        for ($i=0; $i<$lengthA; $i++) {
            if ($strandA[$i] != $strandB[$i]) {
                $hamming_distance++;
            }
        }

        return $hamming_distance;
    }

    throw new InvalidArgumentException("DNA strands must be of equal length.");
}
