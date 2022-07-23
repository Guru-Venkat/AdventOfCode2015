from unittest import TestCase
from main import Day1


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
