class Table(object):

    def __init__(self):
        self.theme = None

    def print(self, out, data):
        if len(data) == 0:
            out.write('No entries found')
            return

        values = self._organize_data(data)

        self._print_lines(out, self.theme.before_table(self))

        for row_idx, row in enumerate(values):
            self._print_lines(out, self.theme.before_row(self, row, row_idx))

            prev_col = None
            prev_value = None
            for column_idx, (column, value) in \
                    enumerate(zip(self.columns, row)):
                if column_idx > 0:
                    between_cells = self.theme.between_cells(
                            self, row, row_idx, prev_col, column_idx-1,
                            prev_value, column, column_idx, value)
                    out.write(between_cells)

                before_cell = self.theme.before_cell(self, row, row_idx,
                                                     column, column_idx, value)
                out.write(before_cell)
                out.write(column.cell(value))
                after_cell = self.theme.after_cell(self, row, row_idx, column,
                                                   column_idx, value)
                out.write(after_cell)

                prev_col = column
                prev_value = value

            self._print_lines(out, self.theme.after_row(self, row, row_idx))

        self._print_lines(out, self.theme.after_table(self, row_idx))

    def _organize_data(self, data):
        values = list()

        titles = self._organize_titles()

        values.append(titles)

        for row in data:
            values.append(self._organize_row(data, row))

        return values

    def _organize_titles(self):
        titles = list()

        for i, column in enumerate(self.columns):
            title = column.get_title()
            titles.append(title)
            column._width = len(title)

        return titles

    def _organize_row(self, data, row):
        line = list()
        for column in self.columns:
            value = column.get_value(data, row)

            if len(value) > column._width:
                column._width = len(value)

            line.append(value)

        return line

    def _print_lines(self, out, line_gen):
        for line in line_gen:
            out.write(line)

class AbstractColumn(object):

    def __init__(self):
        self._table = None
        self._width = -1

    def get_title(self):
        raise NotImplementedError()

    def get_value(self, data, row):
        raise NotImplementedError()

    def cell(self, value):
        raise NotImplementedError()


_column_separator = ' | '


class Column(AbstractColumn):

    def __init__(self):
        super().__init__()
        self.title = ''
        self.getter = lambda row: str(row)
        self.none_value = None
        self.formatter = lambda value: str(value)
        self.alignment = 'left'

    def get_title(self):
        return self.title

    def get_value(self, data, row):
        value = self.getter(row)

        if value is None and self.none_value is not None:
            return self.none_value

        return self.formatter.format(value)

    def cell(self, value):
        missing = self._width - len(value)

        match self.alignment:
            case 'left':
                prefix = ''
                suffix = ' ' * missing

            case 'right':
                prefix = ' ' * missing
                suffix = ''

            case 'center':
                prefix = ' ' * (missing // 2)
                suffix = ' ' * (missing - len(prefix))

            case _:
                raise AssertionError(f'Unknown alignment ({self.alignment})')

        return f'{prefix}{value}{suffix}'
