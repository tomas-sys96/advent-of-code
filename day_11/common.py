from collections import namedtuple

GALAXY: str = "#"
EXPANDED_SPACE: str = "?"

Coordinate: namedtuple = namedtuple(typename="Coordinate", field_names=["row", "column"])


class SpaceExpansionCalculator:
    def __init__(self, rows: list[str], expanded_space_distance: int, expansion_multiplies: bool) -> None:
        self.rows: list[str] = rows
        self.expanded_space_distance: int = expanded_space_distance
        self.expansion_multiplies: bool = expansion_multiplies

    def insert_empty_row(self, row_index: int) -> None:
        self.rows.insert(row_index, EXPANDED_SPACE * len(self.rows[row_index]))

    def insert_empty_column(self, column_index: int) -> None:
        for row_index in range(len(self.rows)):
            self.rows[row_index] = (
                self.rows[row_index][:column_index] + EXPANDED_SPACE + self.rows[row_index][column_index:]
            )

    def expand_rows(self) -> None:
        for row_index in reversed(range(len(self.rows))):
            if GALAXY not in self.rows[row_index]:
                self.insert_empty_row(row_index=row_index)

    def expand_columns(self) -> None:
        for column_index in reversed(range(len(self.rows[0]))):
            if not any([row[column_index] == GALAXY for row in self.rows]):
                self.insert_empty_column(column_index=column_index)

    def expand_empty_spaces(self) -> None:
        self.expand_rows()
        self.expand_columns()

    def get_galaxy_coordinates(self) -> list[Coordinate]:
        self.expand_empty_spaces()
        coordinates: list[Coordinate] = []

        for row_index, row in enumerate(self.rows):
            for column_index, character in enumerate(row):
                if character == GALAXY:
                    coordinates.append(Coordinate(row=row_index, column=column_index))

        return coordinates

    def calculate_horizontal_distance(self, coordinate_1: Coordinate, coordinate_2: Coordinate) -> int:
        distance: int = 0

        first_column: int
        last_column: int
        if coordinate_1.column < coordinate_2.column:
            first_column = coordinate_1.column
            last_column = coordinate_2.column
        else:
            first_column = coordinate_2.column
            last_column = coordinate_1.column

        for column in range(first_column + 1, last_column + 1):
            character: str = self.rows[coordinate_1.row][column]
            if character == EXPANDED_SPACE and self.expansion_multiplies:
                distance += self.expanded_space_distance - 1
            elif character == EXPANDED_SPACE:
                distance += self.expanded_space_distance
            else:
                distance += 1

        return distance

    def calculate_vertical_distance(self, coordinate_1: Coordinate, coordinate_2: Coordinate) -> int:
        distance: int = 0

        for row in range(coordinate_1.row + 1, coordinate_2.row + 1):
            character: str = self.rows[row][coordinate_1.column]
            if character == EXPANDED_SPACE and self.expansion_multiplies:
                distance += self.expanded_space_distance - 1
            elif character == EXPANDED_SPACE:
                distance += self.expanded_space_distance
            else:
                distance += 1

        return distance

    def get_distance_between_galaxies(self) -> int:
        galaxy_coordinates: list[Coordinate] = self.get_galaxy_coordinates()

        distance: int = 0
        for coordinate_index, coordinate in enumerate(galaxy_coordinates):
            for counter_coordinate in galaxy_coordinates[coordinate_index + 1 :]:
                distance += self.calculate_horizontal_distance(
                    coordinate_1=coordinate,
                    coordinate_2=counter_coordinate,
                ) + self.calculate_vertical_distance(
                    coordinate_1=coordinate,
                    coordinate_2=counter_coordinate,
                )

        return distance
