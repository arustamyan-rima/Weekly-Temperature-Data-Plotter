import matplotlib.pyplot as plt


def get_data_list(file_name: str) -> list[str]:
    """open file and return content as list

    Args:
        file_name (str): Name of File

    Returns:
        list[str]: List with lines
    """
    with open(file_name, encoding="utf-8") as f:
        return list(f)


def parse_row(row: str) -> tuple[str, list[int]]:
    """Split row at space and parse elements.

    split each row at space and parse each element to int if numeric
    ignore non-numeric parts.

    raw row example:
    12: mo31 tue33 wed22 thu 34 fri 23 sat33 sun24

    Return value looks like:
    12, [31, 33, 22, 34, 23, 33, 24]

    Args:
        row (str): weekly temperatures (see example above)

    Returns:
        tuple[str, List[int]]: week, numeric temperature List
    """
    row_list = row.split()
    # ['12:', 'mo31', 'tue33', 'wed22', 'thu', '34', sun24']
    key = row_list.pop(0).rstrip(":")
    return key, [int(el[-2:]) for el in row_list if el[-2:].isnumeric()]


def get_data_dict(data_list: list[str]) -> dict[str, list[int]]:
    """Creates Dict with temperature lists.

    ["20: mo18 tue30 wed19 thu30 fri19 sat 32 sun32", [...]

    Args:
        data_list (List[str]): Temperature List

    Returns:
        Dict[str, List[int]]: Final Dict
    """
    return dict([parse_row(row) for row in data_list])


def plot_data(*, data: dict[str, list[int]], week: int) -> None:
    """plot weekly temperatures"""
    week_data = data[str(week)]
    plt.plot(range(1, len(week_data) + 1), week_data, color="red")
    plt.show()


if __name__ == "__main__":
    file_name = "wetterdaten.txt"
    data_list = get_data_list(file_name)
    data = get_data_dict(data_list)
    print(data)
    if data:
        plot_data(data=data, week=15)
