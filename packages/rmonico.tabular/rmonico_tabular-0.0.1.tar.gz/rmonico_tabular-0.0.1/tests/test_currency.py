from tabular.currency import Currency
from unittest import TestCase


class CurrencyTests(TestCase):

    def test_without_fraction(self):
        currency = Currency.parse('10')

        self.assertEqual(currency.integer, 10)
        self.assertEqual(currency.fraction, 0)

    def test_with_complete_fraction(self):
        '''
        A "complete fraction" in this context means a fraction with same
        number of digits of Currency instance (by default 2)
        '''
        currency = Currency.parse('10.12')

        self.assertEqual(currency.integer, 10)
        self.assertEqual(currency.fraction, 12)

    def test_with_incomplete_fraction(self):
        currency = Currency.parse('10.1', digits=4)

        self.assertEqual(currency.integer, 10)
        self.assertEqual(currency.fraction, 1000)

    def test_with_fraction_more_precise_than_allowed(self):
        with self.assertRaises(ValueError) as cm:
            Currency.parse('10.123', digits=2)

        self.assertEqual(cm.exception.args[0], 'Fractional part must be at ' +
                         'maximum 2 digits')

    def test___str__(self):
        currency = Currency.parse('-10.99')

        self.assertEqual(str(currency), '-10.99')

    def test___str___with_incomplete_fraction(self):
        currency = Currency.parse('-10.01')

        self.assertEqual(str(currency), '-10.01')

    def test_with_negative_value(self):
        currency = Currency.parse('-10.99')

        self.assertEqual(currency.integer, -10)
        self.assertEqual(currency.fraction, 99)
