from unittest import TestCase
from main import Day1, Day2


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
