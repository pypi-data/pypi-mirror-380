import re


class Currency(object):

    _regex = re.compile(r'(-?[0-9]+)(?:\.([0-9]*))?')

    @staticmethod
    def parse(raw: str, digits: int = 2) -> 'Currency':
        match = re.match(Currency._regex, raw)

        integer, fraction = match.groups()

        if fraction is None:
            fraction = '0'

        fraction_len = len(fraction)

        if fraction_len < digits:
            fraction += Currency._complement(fraction_len, digits)
        elif fraction_len > digits:
            raise ValueError(f'Fractional part must be at maximum {digits} ' +
                             'digits')

        return Currency(int(integer), int(fraction), digits)

    @staticmethod
    def _complement(fraction_len: int, digits: int) -> str:
        return '0' * (digits - fraction_len)

    def _get_complement(self) -> str:
        return Currency._complement(len(str(self.fraction)), self.digits)

    def __init__(self, integer: int, fraction: int, digits: int):
        self.integer = integer
        self.fraction = fraction
        self.digits = digits

    def __str__(self):
        complement = self._get_complement()
        return f'{self.integer}.{complement}{self.fraction}'
