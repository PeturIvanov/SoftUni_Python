from project.table.table import Table


class InsideTable(Table):
    @property
    def min_table_number(self):
        return 1

    @property
    def max_table_number(self):
        return 50

    @property
    def table_number_error(self):
        return f"Inside table's number must be between 1 and 50 inclusive!"
