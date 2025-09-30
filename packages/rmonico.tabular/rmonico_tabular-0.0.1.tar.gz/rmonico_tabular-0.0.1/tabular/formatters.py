from .currency import Currency


class UnformattableError(Exception):

    def __init__(self, value):
        super().__init__(f'Unable to format "{value}"')


class Formatter(object):

    def __init__(self):
        self._next = None

    def andThen(self, next):
        self._next = next

        return self

    def do_format(self, value):
        raise NotImplementedError()

    def _is_formattable(self, value):
        raise NotImplementedError()

    def format(self, value):
        if not self._is_formattable(value):
            raise UnformattableError(value)

        value = self.do_format(value)

        return self._format_next(value)

    def _format_next(self, value):
        return self._next.format(value) if self._next is not None else value


class TypeFormatter(Formatter):

    def __init__(self, type, none_value='<none>'):
        super().__init__()
        self._type = type
        self._none_value = none_value

    def _is_formattable(self, value):
        return isinstance(value, self._type) or value is None

    def type_format(self, value):
        raise NotImplementedError()

    def do_format(self, value):
        if value is None:
            return self._none_value

        return self.type_format(value)


class StrFormatter(TypeFormatter):

    def __init__(self):
        super().__init__(str)

    def type_format(self, value):
        return value


class IntFormatter(TypeFormatter):

    def __init__(self):
        super().__init__(int)

    def type_format(self, value):
        return str(value)


class BoolFormatter(TypeFormatter):

    _default_values = {
            'true': 'y',
            'false': 'n',
            'none': '-',
            }

    def __init__(self, **values):
        if len(values) != 0:
            BoolFormatter._assert_values(values)
        else:
            values = BoolFormatter._default_values

        if 'none' in values:
            super().__init__(bool, values['none'])
        else:
            super().__init__(bool)

        self.values = dict()
        self.values[True] = values['true']
        self.values[False] = values['false']

    @staticmethod
    def _assert_values(values):
        assert 'true' in values and 'false' in values, '"values" dict ' + \
                'must have "true" and "false" keys'

    def type_format(self, value):
        return self.values[value]


class CurrencyFormatter(TypeFormatter):

    def __init__(self):
        super().__init__(Currency)

    def type_format(self, value):
        return str(value)


class ListFormatter(TypeFormatter):

    def __init__(self, separator):
        super().__init__(list)
        self._separator = separator

    def type_format(self, value):
        return self._separator.join(value)
