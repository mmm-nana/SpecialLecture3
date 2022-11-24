import unittest
from src import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def test_read(self):
        printer = CSVPrinter("sample.csv")
        l = printer.read()
        self.assertEqual(3, len(l))


    def test_read2(self):
        printer = CSVPrinter("sample.csv")
        Line = printer.read()
        self.assertEqual("5", Line[1][1])


    def test_read3 (self):
        # try:
        #     printer = CSVPrinter("/Users/nanako-m/Desktop/授業/講義A, C/課題2-2/sample.csv")
        #     printer.read()
        #     unittest.TestCase.fail("This line should not be invoked")
        # except FileNotFoundError as e:
        #     raise e
            # print("error:" + str(e))

        with self.assertRaises(FileNotFoundError) as e:
            printer = CSVPrinter("/Users/nanako-m/Desktop/授業/講義A, C/課題2-2/sample.csv")
            line = printer.read()
            print(line)
            
