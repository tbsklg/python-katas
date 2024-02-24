from a_bubbly_programming_language import start, push, add, sub, mul, div, end

import unittest
import pytest

@pytest.mark.task()
def test_bubbly():
    unittest.TestCase().assertEqual(
        (start)(push)(5)(push)(3)(add)(end),
        8
    )
    unittest.TestCase().assertEqual(
        (start)(push)(5)(push)(3)(sub)(end),
        -2
    )
    unittest.TestCase().assertEqual(
        (start)(push)(5)(push)(3)(mul)(end),
        15
    )
    unittest.TestCase().assertEqual(
        (start)(push)(5)(push)(3)(div)(end),
        0
    )
    unittest.TestCase().assertEqual(
        (start)(push)(5)(push)(3)(add)(push)(2)(mul)(end),
        16
    )
