class Theme(object):

    def before_table(self, table):
        raise NotImplementedError()

    def after_table(self, table, item_count):
        raise NotImplementedError()

    def before_row(self, table, row, i):
        raise NotImplementedError()

    def after_row(self, table, row, i):
        raise NotImplementedError()

    def before_cell(self, table, row, row_idx, column, column_idx, value):
        raise NotImplementedError()

    def between_cells(self, table, row, row_idx, prev_col, prev_col_idx,
                      prev_value, next_col, next_col_idx, next_value):
        raise NotImplementedError()

    def after_cell(self, table, row, row_idx, column, column_idx, value):
        raise NotImplementedError()


class DefaultTheme(Theme):

    def __init__(self, column_separator=' | ', title_separator='-'):
        self._column_separator = column_separator
        self._title_separator = title_separator

    def before_table(self, table):
        return []

    def after_table(self, table, item_count):
        return []

    def before_row(self, table, row, i):
        yield ''

    def after_row(self, table, row, i):
        if i == 0:
            separators = [self._title_separator * c._width for c in table.columns]
            yield '\n'
            yield self._column_separator.join(separators)

        yield '\n'

    def before_cell(self, table, row, row_idx, column, column_idx, value):
        return ''

    def between_cells(self, table, row, row_idx, prev_col, prev_col_idx,
                      prev_value, next_col, next_col_idx, next_value):
        return self._column_separator

    def after_cell(self, table, row, row_idx, column, column_idx, value):
        return ''


class SingleTheme(Theme):

    def __init__(self, chars):
        chars = '''
+-+-+
| | |
+-+-+
| | |
+-+-+
┌─┬─┐
│ │ │
├─┼─┤
│ │ │
└─┴─┘
╭─┬─╮
│ │ │
├─┼─┤
│ │ │
╰─┴─╯
┏━┳━┓
┃ ┃ ┃
┣━╋━┫
┃ ┃ ┃
┗━┻━┛
╔═╦═╗
║ ║ ║
╠═╬═╣
║ ║ ║
╚═╩═╝
        '''


default_theme = DefaultTheme()
