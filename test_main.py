from unittest import TestCase
from main import Day1, Day2, Day3


class TestDay1(TestCase):

    def test_part1(self):
        self.assertEqual(Day1("(())").part1(), 0)
        self.assertEqual(Day1("()()").part1(), 0)
        self.assertEqual(Day1("(((").part1(), 3)
        self.assertEqual(Day1("(()(()(").part1(), 3)
        self.assertEqual(Day1("))(((((").part1(), 3)
        self.assertEqual(Day1("())").part1(), -1)
        self.assertEqual(Day1("))(").part1(), -1)
        self.assertEqual(Day1(")))").part1(), -3)
        self.assertEqual(Day1(")())())").part1(), -3)

    def test_part2(self):
        self.assertEqual(Day1(")").part2(), 1)
        self.assertEqual(Day1("()())").part2(), 5)
        self.assertEqual(Day1("())").part2(), 3)
        self.assertEqual(Day1("))(").part2(), 1)
        self.assertEqual(Day1(")))").part2(), 1)
        self.assertEqual(Day1(")())())").part2(), 1)


class TestDay2(TestCase):
    box1 = Day2.Box([2, 3, 4])
    box2 = Day2.Box([1, 1, 10])

    def test_part1(self):
        self.assertEqual(Day2("""2x3x4
        1x1x10""").part1(), 58 + 43)

    def test_part2(self):
        self.assertEqual(Day2("""2x3x4
        1x1x10""").part2(), 34 + 14)

    def test_paper_required(self):
        self.assertEqual(Day2.paperRequired(self.box1), 58)
        self.assertEqual(Day2.paperRequired(self.box2), 43)

    def test_bow_length_required(self):
        self.assertEqual(Day2.bowLengthRequired(self.box1), 34)
        self.assertEqual(Day2.bowLengthRequired(self.box2), 14)


class TestBox(TestCase):
    box1 = Day2.Box([2, 3, 4])
    box2 = Day2.Box([1, 1, 10])

    def test_area(self):
        self.assertEqual(self.box1.area, 52)
        self.assertEqual(self.box2.area, 42)

    def test_area_of_sides(self):
        self.assertListEqual(self.box1.areaOfSides, [6, 12, 8])
        self.assertListEqual(self.box2.areaOfSides, [1, 10, 10])

    def test_volume(self):
        self.assertEqual(self.box1.volume, 24)
        self.assertEqual(self.box2.volume, 10)

    def test_shortest_perimeter(self):
        self.assertEqual(self.box1.shortestPerimeter, 10)
        self.assertEqual(self.box2.shortestPerimeter, 4)


class TestDay3(TestCase):
    north = Day3.DirectionMap.Directions.NORTH
    south = Day3.DirectionMap.Directions.SOUTH
    east = Day3.DirectionMap.Directions.EAST
    west = Day3.DirectionMap.Directions.WEST

    day3_1 = Day3(">")
    day3_2 = Day3("^>v<")
    day3_3 = Day3("^v^v^v^v^v")
    day3_4 = Day3("^V")

    def test_north(self):
        self.assertEqual(Day3("^").data[0], self.north)

    def test_south(self):
        self.assertEqual(Day3("V").data[0], self.south)
        self.assertEqual(Day3("v").data[0], self.south)

    def test_east(self):
        self.assertEqual(Day3(">").data[0], self.east)

    def test_west(self):
        self.assertEqual(Day3("<").data[0], self.west)

    def test_multiple_directions(self):
        self.assertListEqual(Day3("^v^V").data, [self.north, self.south, self.north, self.south])

    def test_part1(self):
        self.assertEqual(self.day3_1.part1(), 2)
        self.assertEqual(self.day3_2.part1(), 4)
        self.assertEqual(self.day3_3.part1(), 2)

    def test_part2(self):
        self.assertEqual(self.day3_4.part2(), 3)
        self.assertEqual(self.day3_2.part2(), 3)
        self.assertEqual(self.day3_3.part2(), 11)
