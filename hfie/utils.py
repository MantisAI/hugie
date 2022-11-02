import wasabi


def format_table(headers: list, *args):
    """
    Formats a wasabi table ready for printing

    Args:
        column_names (list): List of column names
        *args (list): List of lists containing the data for each column

    """

    data = list(map(tuple, zip(*args)))

    table = wasabi.table(data, header=headers, divider=True)

    return table
