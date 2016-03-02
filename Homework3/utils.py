from numpy import round
from numpy import var
from numpy import log10


def signal_noise_ratio(numbers, bits):
    intervals = 2 ** (bits - 1)
    discrete = round(numbers * intervals) / intervals
    errors = numbers - discrete
    numbers_dispersion = var(numbers)
    # noinspection PyTypeChecker
    errors_dispersion = var(errors)

    return 10 * log10(numbers_dispersion / errors_dispersion)
