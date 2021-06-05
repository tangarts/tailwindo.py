import unittest
from src.converter import Converter


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.converter = Converter().setFramework("bootstrap")

    def test_it_returns_output(self):

        self.assertEqual(
            "sm:flex",
            self.converter.classesOnly(True).setContent("d-sm-flex").convert().get(),
        )
        self.assertEqual(
            '<a class="text-gray-700">love</a>',
            self.converter.setContent('<a class="text-muted">love</a>').convert().get(),
        )

    #  @test */
    def test_it_output_with_prefix(self):

        self.converter.setPrefix("tw-")
        self.assertEqual(
            "sm:tw-flex",
            self.converter.classesOnly(True).setContent("d-sm-flex").convert().get(),
        )
        self.assertEqual(
            '<a class="tw-text-gray-700">love</a>',
            self.converter.setContent('<a class="text-muted">love</a>').convert().get(),
        )

    #  @test */
    def test_it_handles_jsx_class_name(self):

        self.assertEqual(
            '<a className="sm:flex text-gray-700">love</a>',
            self.converter.setContent('<a className="d-sm-flex text-muted">love</a>')
            .convert()
            .get(),
        )

if __name__ == '__main__':
    unittest.main()