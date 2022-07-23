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
    def test_part1(self):
        self.assertEqual(Day2("""2x3x4
        1x1x10""").part1(), 58 + 43)

    def test__paper_required(self):
        self.assertEqual(Day2.paperRequired(Day2.Box([2, 3, 4])), 58)
        self.assertEqual(Day2.paperRequired(Day2.Box([1, 1, 10])), 43)


class TestBox(TestCase):
    def test_area(self):
        self.assertEqual(Day2.Box([2, 3, 4]).area, 52)
        self.assertEqual(Day2.Box([1, 1, 10]).area, 42)

    def test_area_of_sides(self):
        self.assertListEqual(Day2.Box([2, 3, 4]).areaOfSides, [6, 12, 8])
        self.assertListEqual(Day2.Box([1, 1, 10]).areaOfSides, [1, 10, 10])
