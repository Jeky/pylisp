from pylisp import parser, syntax
import unittest


class ParserTest(unittest.TestCase):

    def test_split_tokens(self):
        tokens = parser.split_tokens('aa bb')
        self.assertEqual(['aa', 'bb'], tokens)

    def test_split_tokens_with_newline(self):
        tokens = parser.split_tokens('aa\nbb')
        self.assertEqual(['aa', 'bb'], tokens)

    def test_split_tokens_with_multiply_spaces(self):
        tokens = parser.split_tokens('aa   \tbb')
        self.assertEqual(['aa', 'bb'], tokens)

    def test_get_all_list_tokens(self):
        tokens = ['(', 'a', 'b', ')']
        self.assertEqual(['a', 'b'], parser.get_all_list_tokens(tokens))

    def test_get_all_list_tokens_with_quote(self):
        tokens = ['(', '+', '\'(', 'a', 'b', ')', ')']
        self.assertEqual(['+', '\'(', 'a', 'b', ')'], parser.get_all_list_tokens(tokens))

    def test_get_all_list_tokens_with_nested_list(self):
        tokens = ['(', '(', 'a', 'b', ')', ')']
        self.assertEqual(['(', 'a', 'b', ')'], parser.get_all_list_tokens(tokens))

    def test_parse_int(self):
        tokens = ['1']
        nodes = parser.parse(tokens)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].__class__.__name__, 'IntNode')

    def test_parse_float(self):
        tokens = ['1.1']
        nodes = parser.parse(tokens)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].__class__.__name__, 'FloatNode')


if __name__ == '__main__':
    unittest.main()
