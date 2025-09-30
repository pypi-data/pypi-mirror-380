from io import StringIO
from tabular.currency import Currency
from tabular.factory import TableFactory
from tabular.theme import Theme
from unittest import TestCase


class TabularTests(TestCase):

    def setUp(self):
        self.factory = TableFactory()
        self.out = StringIO()

    def get_lines(self):
        self.out.seek(0)

        return list([line if line[-1] != '\n' else line[:-1] for line in
                     self.out.readlines()])

    def test_empty_table(self):
        table = self.factory.create()

        table.print(self.out, list())

        lines = self.get_lines()

        self.assertEqual(lines[0], 'No entries found')
        self.assertEqual(len(lines), 1)

    def test_single_column(self):
        class Entry(object):

            def __init__(self, name):
                self.name = name

        data = list()
        data.append(Entry('First'))
        data.append(Entry('Second'))
        data.append(Entry('Third'))

        self.factory.column(str) \
            .title('Name') \
            .getter(lambda row: row.name) \
            .create()

        table = self.factory.create()

        table.print(self.out, data)

        lines = self.get_lines()

        self.assertEqual(lines[0], 'Name  ')
        self.assertEqual(lines[1], '------')
        self.assertEqual(lines[2], 'First ')
        self.assertEqual(lines[3], 'Second')
        self.assertEqual(lines[4], 'Third ')

        self.assertEqual(len(lines), 5)

    def test_multiple_column(self):
        class Entry(object):

            def __init__(self, name, age, checked):
                self.name = name
                self.age = age
                self.checked = checked

        data = list()
        data.append(Entry('First', 30, False))
        data.append(Entry('Second', 31, False))
        data.append(Entry('Third', 32, True))

        self.factory \
            .column(str) \
            .title('Name') \
            .getter(lambda row: row.name) \
            .create() \
            \
            .column(str) \
            .title('Age') \
            .getter(lambda row: str(row.age)) \
            .create() \
            \
            .column(str) \
            .title('Checked?') \
            .getter(lambda row: '*' if row.checked else ' ') \
            .create()

        table = self.factory.create()

        table.print(self.out, data)

        lines = self.get_lines()

        self.assertEqual(lines[0], 'Name   | Age | Checked?')
        self.assertEqual(lines[1], '------ | --- | --------')
        self.assertEqual(lines[2], 'First  | 30  |         ')
        self.assertEqual(lines[3], 'Second | 31  |         ')
        self.assertEqual(lines[4], 'Third  | 32  | *       ')

        self.assertEqual(len(lines), 5)

    def test_column_alignment(self):
        class Entry(object):

            def __init__(self, name, active):
                self.name = name
                self.active = active

        data = list()
        data.append(Entry('First', False))
        data.append(Entry('Second', False))
        data.append(Entry('Third', True))

        def active_getter(row):
            if row.active:
                return '[ X ]'
            else:
                return '[   ]'

        self.factory \
            .column(str) \
            .title('Name') \
            .getter(lambda row: row.name) \
            .create() \
            \
            .column(str) \
            .title('Left Alignment') \
            .getter(active_getter) \
            .align('left') \
            .create() \
            \
            .column(str) \
            .title('Center Alignment') \
            .getter(active_getter) \
            .align('center') \
            .create() \
            \
            .column(str) \
            .title('Right Alignment') \
            .getter(active_getter) \
            .align('right') \
            .create()

        table = self.factory.create()

        table.print(self.out, data)

        lines = self.get_lines()

        self.assertEqual(lines[0], 'Name   | Left Alignment | Center Alignment | Right Alignment')
        self.assertEqual(lines[1], '------ | -------------- | ---------------- | ---------------')
        self.assertEqual(lines[2], 'First  | [   ]          |      [   ]       |           [   ]')
        self.assertEqual(lines[3], 'Second | [   ]          |      [   ]       |           [   ]')
        self.assertEqual(lines[4], 'Third  | [ X ]          |      [ X ]       |           [ X ]')

        self.assertEqual(len(lines), 5)

    def test_column_formatter(self):
        class Entry(object):

            def __init__(self, strf, intf, boolf, currencyf, listf):
                self.strf = strf
                self.intf = intf
                self.boolf = boolf
                self.currencyf = currencyf
                self.listf = listf

        data = list()
        data.append(Entry('First', 30, True, Currency.parse('10.00'), ['a', 'b', 'c']))
        data.append(Entry('Second', 31, False, Currency.parse('11.00'), ['d', 'e', 'f']))
        data.append(Entry('Third', 32, None, Currency.parse('12.00'), ['g', 'h', 'i']))

        self.factory \
            .column(str) \
            .title('Str Field') \
            .getter(lambda row: row.strf) \
            .create() \
            \
            .column(int) \
            .title('Int Field') \
            .getter(lambda row: row.intf) \
            .create() \
            \
            .column(bool) \
            .title('Bool Field') \
            .getter(lambda row: row.boolf) \
            .create() \
            \
            .column(Currency) \
            .title('Currency Field') \
            .getter(lambda row: row.currencyf) \
            .create() \
            \
            .column(list) \
            .title('List Field') \
            .getter(lambda row: row.listf) \
            .create()

        table = self.factory.create()

        table.print(self.out, data)

        lines = self.get_lines()

        self.assertEqual(lines[0], 'Str Field | Int Field | Bool Field | Currency Field | List Field')
        self.assertEqual(lines[1], '--------- | --------- | ---------- | -------------- | ----------')
        self.assertEqual(lines[2], 'First     |        30 |     y      |     10.00      | a, b, c   ')
        self.assertEqual(lines[3], 'Second    |        31 |     n      |     11.00      | d, e, f   ')
        self.assertEqual(lines[4], 'Third     |        32 |     -      |     12.00      | g, h, i   ')

        self.assertEqual(len(lines), 5)

    def test_none_value_for_formatter(self):
        class Entry(object):

            def __init__(self, strf):
                self.strf = strf

        data = list()
        data.append(Entry('First'))
        data.append(Entry(None))

        self.factory \
            .column(str) \
            .title('Str Field') \
            .getter(lambda row: row.strf) \
            .create()

        table = self.factory.create()

        table.print(self.out, data)

        lines = self.get_lines()

        self.assertEqual(lines[0], 'Str Field')
        self.assertEqual(lines[1], '---------')
        self.assertEqual(lines[2], 'First    ')
        self.assertEqual(lines[3], '<none>   ')

        self.assertEqual(len(lines), 4)

    def test_none_value_on_column(self):
        class Entry(object):

            def __init__(self, strf):
                self.strf = strf

        data = list()
        data.append(Entry('First'))
        data.append(Entry(None))

        self.factory \
            .column(str) \
            .title('Str Field') \
            .getter(lambda row: row.strf) \
            .create() \
        \
            .column(str) \
            .title('Another Str Field') \
            .getter(lambda row: row.strf) \
            .none_value('--nothing--') \
            .create()

        table = self.factory.create()

        table.print(self.out, data)

        lines = self.get_lines()

        self.assertEqual(lines[0], 'Str Field | Another Str Field')
        self.assertEqual(lines[1], '--------- | -----------------')
        self.assertEqual(lines[2], 'First     | First            ')
        self.assertEqual(lines[3], '<none>    | --nothing--      ')

        self.assertEqual(len(lines), 4)

    def test_custom_theme(self):
        class Entry(object):

            def __init__(self, name, age, checked):
                self.name = name
                self.age = age
                self.checked = checked

        data = list()
        data.append(Entry('First', 30, False))
        data.append(Entry('Second', 31, False))
        data.append(Entry('Third', 32, True))

        self.factory \
            .column(str) \
            .title('Name') \
            .getter(lambda row: row.name) \
            .create() \
            \
            .column(str) \
            .title('Age') \
            .getter(lambda row: str(row.age)) \
            .create() \
            \
            .column(str) \
            .title('Checked?') \
            .getter(lambda row: '*' if row.checked else ' ') \
            .create()

        class CustomTheme(Theme):

            def before_table(self, table):
                yield 'Before table\n'
                yield '\n'

            def after_table(self, table, item_count):
                yield '\n'
                yield f'After table - {item_count} items\n'

            def before_row(self, table, row, i):
                yield '<'

            def after_row(self, table, row, i):
                yield '>\n'

            def before_cell(self, table, row, row_idx, column, column_idx,
                            value):
                return '- '

            def between_cells(self, table, row, row_idx, prev_col,
                              prev_col_idx, prev_value, next_col,
                              next_col_idx, next_value):
                return 'X'

            def after_cell(self, table, row, row_idx, column, column_idx,
                           value):
                return ' +'

        self.factory.theme(CustomTheme())

        table = self.factory.create()

        table.print(self.out, data)

        lines = self.get_lines()

        self.assertEqual(lines[0], 'Before table')
        self.assertEqual(lines[1], '')
        self.assertEqual(lines[2], '<- Name   +X- Age +X- Checked? +>')
        self.assertEqual(lines[3], '<- First  +X- 30  +X-          +>')
        self.assertEqual(lines[4], '<- Second +X- 31  +X-          +>')
        self.assertEqual(lines[5], '<- Third  +X- 32  +X- *        +>')
        self.assertEqual(lines[6], '')
        self.assertEqual(lines[7], 'After table - 3 items')

        self.assertEqual(len(lines), 8)
