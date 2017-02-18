import Sorting.selection_sort
import Sorting.insertion_sort
import Sorting.shell_sort

from unittest import TestCase
from random import randint
from ddt import ddt, data


@ddt
class TestSorting(TestCase):

    # fetch module names from the Sorting package
    sorts = ['.'.join(['Sorting',val]) for val in dir(Sorting) if '__' not in val]

    # need to use *sorts, otherwise DDT passes the whole list instead of individual values
    @data(*sorts)
    def test_basic_case(self,value):

        self.assertSequenceEqual(eval(value).do_sort([3,2,1,-200,3]),[-200,1,2,3,3])

    @data(*sorts)
    def test_empty(self,value):

        self.assertFalse(eval(value).do_sort([])) # an empty list equates to False

    @data(*sorts)
    def test_single_element(self,value):

        self.assertEqual(eval(value).do_sort([0]),[0])

    @data(*sorts)
    def test_repeating_elements(self,value):

        self.assertEqual(eval(value).do_sort([0,0]),[0,0])
        self.assertEqual(eval(value).do_sort([0,0,0]),[0,0,0])

    @data(*sorts)
    def test_random(self,value):

        randomlist = [randint(-100000,100000) for _ in range(100)]
        sortedlist = sorted(randomlist)

        self.assertSequenceEqual(eval(value).do_sort(randomlist), sortedlist)
