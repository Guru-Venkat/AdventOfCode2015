import enum
import hashlib
import itertools


class AdventOfCode:
    def __init__(self, data="", day=1):
        if data == "":
            with open(f"Data/Day{day}Data.txt", "r") as f:
                self.data = f.read()
        else:
            self.data = data


class Day1(AdventOfCode):
    """
    --- Day 1: Not Quite Lisp --- Santa was hoping for a white Christmas, but his weather machine's "snow" function
    is powered by stars, and he's fresh out! To save Christmas, he needs you to collect fifty stars by December 25th.

    Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar;
    the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

    Here's an easy puzzle to warm you up.

    Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the
    directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the
    instructions one character at a time.

    An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down
    one floor.

    The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

    For example:

    (()) and ()() both result in floor 0.
    ((( and (()(()( both result in floor 3.
    ))((((( also results in floor 3.
    ()) and ))( both result in floor -1 (the first basement level).
    ))) and )())()) both result in floor -3.

    --- Part Two ---

    Now, given the same instructions, find the position of the first character that causes him to enter the basement
    (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

    For example:

    ')' causes him to enter the basement at character position 1.
    ()()) causes him to enter the basement at character position 5.
    What is the position of the character that causes Santa to first enter the basement?

    """

    def __init__(self, data=""):
        super().__init__(data, 1)

    def part1(self):
        return self.data.count('(') - self.data.count(')')

    def part2(self):
        floor = 0
        for i, c in enumerate(self.data):
            floor += 1 if c == '(' else -1
            if floor == -1:
                return i + 1
        return -1


class Day2(AdventOfCode):
    """--- Day 2: I Was Told There Would Be No Math ---

    The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the
    dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

    Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required
    wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The
    elves also need a little extra paper for each present: the area of the smallest side.

    For example:

    A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet
    of slack, for a total of 58 square feet. A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square
    feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

    --- Part Two ---

    The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the
    length they need to order, which they would again like to be exact.

    The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any
    one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the
    perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll
    never tell.

    For example:

    A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of
    ribbon for the bow, for a total of 34 feet. A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon
    to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.

    """

    class Box:
        def __init__(self, dimensions: list[int]):
            if len(dimensions) != 3:
                raise Exception("Invalid number of dimensions")
            self.length = dimensions[0]
            self.width = dimensions[1]
            self.height = dimensions[2]
            self._sortedDimensions = sorted(dimensions)

        @property
        def area(self) -> int:
            return 2 * sum(self.areaOfSides)

        @property
        def areaOfSides(self) -> list:
            return [self.length * self.width, self.width * self.height, self.height * self.length]

        @property
        def volume(self) -> int:
            return self.length * self.width * self.height

        @property
        def shortestPerimeter(self):
            return 2 * (self._sortedDimensions[0] + self._sortedDimensions[1])

    def __init__(self, data=""):
        super().__init__(data, 2)

        self.data = [Day2.Box(list(int(x) for x in row.strip().split("x"))) for row in self.data.splitlines()]

    @staticmethod
    def paperRequired(box: Box):
        return box.area + min(box.areaOfSides)

    @staticmethod
    def bowLengthRequired(box: Box):
        return box.shortestPerimeter + box.volume

    def part1(self):
        return sum(self.paperRequired(box) for box in self.data)

    def part2(self):
        return sum(self.bowLengthRequired(box) for box in self.data)


class Day3(AdventOfCode):
    """
    --- Day 3: Perfectly Spherical Houses in a Vacuum ---

    Santa is delivering presents to an infinite two-dimensional grid of houses.

    He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls
    him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v),
    east (>), or west (<). After each move, he delivers another present to the house at his new location.

    However, the elf back at the North Pole has had a little too much eggnog, and so his directions are a little off,
    and Santa ends up visiting some houses more than once. How many houses receive at least one present?

    For example:

    > delivers presents to 2 houses: one at the starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
    """

    class DirectionMap:
        class Directions(enum.Enum):
            NORTH = "^"
            SOUTH = "V"
            EAST = ">"
            WEST = "<"

        def __init__(self, count_of_movers=1):
            self.visited = set()
            self.count_of_movers = count_of_movers
            self.currentLocation = [0 + 0j for _ in range(self.count_of_movers)]
            self.visited.add(self.currentLocation[0])

        @property
        def visitedCount(self):
            return len(self.visited)

        def processDirections(self, inputDirections: list[Directions]):

            for i, direction in enumerate(inputDirections):
                self._processDirection(direction, i % self.count_of_movers)

            return self

        def _processDirection(self, direction: Directions, mover_index: int = 1):
            match direction:
                case self.Directions.NORTH:
                    self.currentLocation[mover_index] = self.currentLocation[mover_index] + 0 + 1j
                case self.Directions.SOUTH:
                    self.currentLocation[mover_index] = self.currentLocation[mover_index] + 0 - 1j
                case self.Directions.EAST:
                    self.currentLocation[mover_index] = self.currentLocation[mover_index] + 1 + 0j
                case self.Directions.WEST:
                    self.currentLocation[mover_index] = self.currentLocation[mover_index] - 1 + 0j

            self.visited.add(self.currentLocation[mover_index])

    def __init__(self, data=""):
        super().__init__(data, 3)

        self.data = [Day3.DirectionMap.Directions.__dict__['_value2member_map_'][a] for a in self.data.upper()]

    def part1(self):
        return Day3.DirectionMap().processDirections(
            self.data).visitedCount

    def part2(self):
        return Day3.DirectionMap(2).processDirections(self.data).visitedCount


class Day4(AdventOfCode):
    """--- Day 4: The Ideal Stocking Stuffer ---

    Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically
    forward-thinking little girls and boys.

    To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the
    MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine
    AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such
    a hash.

    For example:

    If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes
    (000001dbbfa...), and it is the lowest such number to do so. If your secret key is pqrstuv, the lowest number it
    combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970
    looks like 000006136ef....
    """

    def __init__(self, data="ckczppom"):
        super().__init__(data, 4)

    def part1(self):
        for i in infiniteLoop():
            if hashlib.md5((self.data + str(i)).encode()).hexdigest().startswith('00000'):
                return i

    def part2(self):
        for i in infiniteLoop():
            if hashlib.md5((self.data + str(i)).encode()).hexdigest().startswith('000000'):
                return i


def infiniteLoop():
    i = 0

    while True:
        yield i
        i += 1


class Day5(AdventOfCode):
    """
    Santa needs help figuring out which strings in his text file are naughty or nice.

    A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
    For example:

    ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...),
    and none of the disallowed substrings. aaa is nice because it has at least three vowels and a double letter,
    even though the letters used by different rules overlap. jchzalrnumimnmhp is naughty because it has no double
    letter. haegwjzuvuyypxyu is naughty because it contains the string xy. dvszwmarrgswjxmb is naughty because it
    contains only one vowel.

    --- Part Two ---

    Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty
    or nice. None of the old rules apply, as they are all clearly ridiculous.

    Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (
    xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps). It contains at least one letter which repeats
    with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa. For example:

    qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one
    letter between them (zxz). xxyxx is nice because it has a pair that appears twice and a letter that repeats with
    one between, even though the letters used by each rule overlap. uurcxstgmygtbstg is naughty because it has a pair
    (tg) but no repeat with a single letter between them. ieodomkazucvgmuy is naughty because it has a repeating
    letter with one between (odo), but no pair that appears twice.
    """

    def __init__(self, data=""):
        super().__init__(data, 5)
        self.data = self.data.splitlines()

    @staticmethod
    def isNiceString(inputStr: str) -> bool:
        inputStr = inputStr.lower()
        result = sum(
            [inputStr.count(vowel) for vowel in "aeiou"]
        ) > 2 and any(
            map(
                lambda x: x > 1,
                [len(list(g)) for k, g in itertools.groupby(inputStr)]
            )
        ) and all(
            a not in inputStr
            for a in ['ab', 'xy', 'pq', 'cd']
        )

        return result

    def part1(self):
        return sum(1 for string in self.data if Day5.isNiceString(string))


if __name__ == '__main__':
    print(Day5().part1())
