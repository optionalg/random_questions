import unittest
from telephone_word_combos import telephone_word_combos

class TelephoneWordCombosTest(unittest.TestCase):
    """
    test the implementation of telephone_word_combos
    """

    def test_case_with_three_numbers(self):
        """
        test the case with the number 111
        there is only one combination: '111'
        """
        result = telephone_word_combos('111')
        self.assertEqual(result,['111'])

    def test_case_with_no_ones_or_zeros(self):
        """
        test the case with the number 111-1111

        should yield one combination: '1111111'
        """
        result = telephone_word_combos('1111111')
        self.assertEqual(result, ['1111111'])

    def test_case_with_only_one_mutable(self):
        """
        test the case with the number 111-1112

        should yeild '111111[ABC]'
        """
        result = telephone_word_combos('1111112')
        self.assertEqual(len(result), 3)
        self.assertIn('111111A', result)
        self.assertIn('111111B', result)
        self.assertIn('111111C', result)

    def test_case_with_two_mutables(self):
        """
        test the case with the number 111-1123

        should yeild '11111[ABC][DEF]', 9 combinations
        """
        result = telephone_word_combos('1111123')
        self.assertEqual(len(result), 9)

    def test_case_with_max_number_mutables(self):
        """
        test the case with the number 222-2222

        should yeild a result with 3**7 combinations
        """
        result = telephone_word_combos('2222222')
        self.assertEqual(len(result), 3**7)
