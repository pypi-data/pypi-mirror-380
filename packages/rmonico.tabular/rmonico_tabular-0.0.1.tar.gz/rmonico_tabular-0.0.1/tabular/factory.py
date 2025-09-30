from . import Table, Column
from .currency import Currency
from .formatters import StrFormatter, IntFormatter, BoolFormatter, \
        CurrencyFormatter, ListFormatter
from .theme import default_theme


class TableFactory(object):

    def __init__(self):
        self._columns = list()
        self._theme = default_theme

    def column(self, kind=None):
        factory = ColumnFactory(self)

        if kind is None:
            return factory

        formatter = _formatters[kind]

        _column_defaults[kind](factory, formatter)

        return factory

    def _add_column(self, column):
        self._columns.append(column)

    def theme(self, theme):
        self._theme = theme
        return self

    def create(self):
        table = Table()
        table.columns = self._columns
        for column in table.columns:
            column._table = table
        table.theme = self._theme

        return table


_formatters = {
    str: StrFormatter(),
    int: IntFormatter(),
    bool: BoolFormatter(),
    Currency: CurrencyFormatter(),
    list: ListFormatter(', '),
}

_column_defaults = {
    str: lambda factory, fmtr: factory.formatter(fmtr).align('left'),
    int: lambda factory, fmtr: factory.formatter(fmtr).align('right'),
    bool: lambda factory, fmtr: factory.formatter(fmtr).align('center'),
    Currency: lambda factory, fmtr: factory.formatter(fmtr).align('center'),
    list: lambda factory, fmtr: factory.formatter(fmtr).align('left'),
}


class ColumnFactory(object):

    def __init__(self, tableFactory):
        self.tableFactory = tableFactory
        self._title = None
        self._getter = None
        self._none_value = None
        self._formatter = str
        self._alignment = 'left'

    def title(self, title):
        self._title = title
        return self

    def getter(self, _getter):
        self._getter = _getter
        return self

    def none_value(self, _none_value):
        self._none_value = _none_value
        return self

    def formatter(self, _formatter):
        self._formatter = _formatter
        return self

    def align(self, alignment):
        self._alignment = alignment
        return self

    def create(self):
        column = self._do_create()
        self.tableFactory._add_column(column)
        return self.tableFactory

    def _do_create(self):
        self._validate()

        column = Column()
        column.title = self._title
        column.getter = self._getter
        column.none_value = self._none_value
        column.formatter = self._formatter
        column.alignment = self._alignment

        return column

    def _validate(self):
        if self._title is None:
            raise ValueError('title field must be set')

        if self._getter is None:
            raise ValueError('getter field must be set')

        if self._formatter is None:
            raise ValueError('formatter field must be set')

        if self._alignment is None:
            raise ValueError('alignment field must be set')
