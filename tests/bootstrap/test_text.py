import unittest

from src.converter import Converter


class TestText(unittest.TestCase):
    def setUp(self):
        self.converter = Converter(classes_only=True)

    def test_converts_text_with_breakpoint(self):
        self.assertEqual(
            "sm:text-left", self.converter.set_content("text-xs-left").convert()
        )
        self.assertEqual(
            "lg:text-justify", self.converter.set_content("text-lg-justify").convert()
        )
