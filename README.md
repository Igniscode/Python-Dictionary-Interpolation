# Python-Dictionary-Interpolation

Caution! there is not theorical background about this algorithm.

* Algorithm Explain
    1. Make the regular interval dictionary of approximate values
    2. Interpolate missing data by using recursive function
        * recursive function : (dict[n-1] + (dict[n-1] + (dict[n-1] + ... dict[n+k]) ... /2)/2)/2
        * k is number of next exist value