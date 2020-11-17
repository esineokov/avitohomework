import asyncio
import logging
from matrix import get_matrix
import unittest

logging.basicConfig(level="ERROR")


class TestMatrix(unittest.TestCase):

    def setUp(self):
        self.source_url = "https://f003.backblazeb2.com/file/am-avito/matrix.txt"
        self.traversal_ok = [
            10, 50, 90, 130,
            140, 150, 160, 120,
            80, 40, 30, 20,
            60, 100, 110, 70
        ]

        self.traversal_bad = [1]

    def test_eq_matrices(self):
        assert asyncio.run(get_matrix(self.source_url)) == self.traversal_ok, "matrices are not equally"

    def test_not_eq_matrices(self):
        assert asyncio.run(get_matrix(self.source_url)) != self.traversal_bad, "matrices are equally"

    def test_404(self):
        assert asyncio.run(get_matrix("https://httpstat.us/404")) == [], "matrices are not equally"

    def test_500(self):
        assert asyncio.run(get_matrix("https://httpstat.us/500")) == [], "matrices are not equally"


if __name__ == '__main__':
    unittest.main()

    # Solution for bug https://github.com/aio-libs/aiohttp/issues/2039
    asyncio.run(asyncio.sleep(0))
