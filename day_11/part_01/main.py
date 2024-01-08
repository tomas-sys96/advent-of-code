from collections import namedtuple

FILE_PATH: str = "../puzzle_input.txt"
GALAXY: str = "#"
EMPTY_SPACE: str = "."

Coordinate: namedtuple = namedtuple(typename="Coordinate", field_names=["row", "column"])


def insert_empty_row(rows: list[str], row_index: int) -> list[str]:
    rows.insert(row_index, EMPTY_SPACE * len(rows[row_index]))

    return rows


def insert_empty_column(rows: list[str], column_index: int) -> list[str]:
    for row_index in range(len(rows)):
        rows[row_index] = rows[row_index][:column_index] + EMPTY_SPACE + rows[row_index][column_index:]

    return rows


def double_rows(rows: list[str]) -> list[str]:
    for row_index in reversed(range(len(rows))):
        if GALAXY not in rows[row_index]:
            # Insert an empty row
            rows = insert_empty_row(rows=rows, row_index=row_index)

    return rows


def double_columns(rows: list[str]) -> list[str]:
    for column_index in reversed(range(len(rows[0]))):
        if not any([row[column_index] == GALAXY for row in rows]):
            # Insert an empty column
            rows = insert_empty_column(rows=rows, column_index=column_index)

    return rows


def double_empty_lines(rows: list[str]) -> list[str]:
    rows = double_rows(rows=rows)
    return double_columns(rows=rows)


def get_galaxy_coordinates(rows: list[str]) -> list[Coordinate]:
    expanded_rows: list[str] = double_empty_lines(rows=rows)
    coordinates: list[Coordinate] = []

    for row_index, row in enumerate(expanded_rows):
        for column_index, character in enumerate(row):
            if character == GALAXY:
                coordinates.append(Coordinate(row=row_index, column=column_index))

    return coordinates


def calculate_distance_between_galaxies(galaxy_coordinates: list[Coordinate]) -> int:
    distance: int = 0
    for coordinate_index, coordinate in enumerate(galaxy_coordinates):
        for counter_coordinate in galaxy_coordinates[coordinate_index + 1 :]:
            distance += abs(coordinate.row - counter_coordinate.row) + abs(
                coordinate.column - counter_coordinate.column
            )

    return distance


def main() -> None:
    with open(file=FILE_PATH, mode="r") as file:
        rows: list[str] = file.readlines()

    galaxy_coordinates: list[Coordinate] = get_galaxy_coordinates(rows=rows)
    print(calculate_distance_between_galaxies(galaxy_coordinates=galaxy_coordinates))


if __name__ == "__main__":
    main()
