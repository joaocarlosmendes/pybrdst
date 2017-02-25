# -*-coding: utf-8 -*-

from pybrdst.pybrdst import PyBrDST
from datetime import datetime


class TestPySummer():

    def test_begin_dst(self):
        dst = PyBrDST()
        assert dst.begin_dst(2017) == datetime(2017, 10, 15)
        assert dst.begin_dst(2018) == datetime(2018, 10, 21)

    def test_end_dst(self):
        dst = PyBrDST()
        assert dst.end_dst(2016) == datetime(2016, 2, 21)

    def test_dst(self):
        dst = PyBrDST()
        assert dst.get_dst(2017) == (datetime(2017, 10, 15),
                                     datetime(2018, 2, 18))

    def test_easter_date(self):
        dst = PyBrDST()
        assert dst.easter_date(2017) == datetime(2017, 4, 16)

    def test_carnival_date(self):
        dst = PyBrDST()
        assert dst.carnival_date(
            dst.easter_date(2017)) == datetime(2017, 2, 28)
