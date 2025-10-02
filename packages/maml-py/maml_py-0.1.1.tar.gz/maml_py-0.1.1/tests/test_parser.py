import unittest
from maml import loads, dumps, MAMLSyntaxError


class TestParser(unittest.TestCase):
    def test_null(self):
        self.assertIsNone(loads("null"))

    def test_boolean(self):
        self.assertTrue(loads("true"))
        self.assertFalse(loads("false"))

    def test_integer(self):
        self.assertEqual(loads("42"), 42)
        self.assertEqual(loads("-100"), -100)
        self.assertEqual(loads("0"), 0)

    def test_float(self):
        self.assertEqual(loads("1.0"), 1.0)
        self.assertEqual(loads("3.1415"), 3.1415)
        self.assertEqual(loads("-0.01"), -0.01)
        self.assertEqual(loads("5e+22"), 5e+22)
        self.assertEqual(loads("1e06"), 1e06)
        self.assertEqual(loads("-2E-2"), -2E-2)
        self.assertEqual(loads("6.626e-34"), 6.626e-34)

    def test_string(self):
        self.assertEqual(loads('""'), "")
        self.assertEqual(loads('"a"'), "a")
        self.assertEqual(loads('"hello world"'), "hello world")

    def test_string_escapes(self):
        self.assertEqual(loads(r'"\n"'), "\n")
        self.assertEqual(loads(r'"\t"'), "\t")
        self.assertEqual(loads(r'"\""'), '"')
        self.assertEqual(loads(r'"\\"'), "\\")
        self.assertEqual(loads(r'"\r"'), "\r")

    def test_string_unicode(self):
        self.assertEqual(loads(r'"\u{22}"'), '"')
        self.assertEqual(loads(r'"\u{0022}"'), '"')
        self.assertEqual(loads(r'"\u{41}"'), "A")
        self.assertEqual(loads(r'"\u{C}"'), "\f")
        self.assertEqual(loads(r'"\u{000C}"'), "\f")
        self.assertEqual(loads(r'"\u{10FFFF}"'), "\U0010FFFF")

    def test_string_invalid_escape(self):
        with self.assertRaises(MAMLSyntaxError):
            loads(r'"\x"')
        with self.assertRaises(MAMLSyntaxError):
            loads(r'"\b"')
        with self.assertRaises(MAMLSyntaxError):
            loads(r'"\f"')

    def test_string_invalid_unicode(self):
        with self.assertRaises(MAMLSyntaxError):
            loads(r'"\u{GGGG}"')
        with self.assertRaises(MAMLSyntaxError):
            loads(r'"\u0022"')
        with self.assertRaises(MAMLSyntaxError):
            loads(r'"\u{}"')
        with self.assertRaises(MAMLSyntaxError):
            loads(r'"\u{1234567}"')

    def test_string_unterminated(self):
        with self.assertRaises(MAMLSyntaxError):
            loads('"hello')

    def test_multiline_string(self):
        result = loads('"""\nHello,\nworld!\n"""')
        self.assertEqual(result, "Hello,\nworld!\n")

    def test_multiline_string_no_trailing_newline(self):
        result = loads('"""\nHello,\nworld!"""')
        self.assertEqual(result, "Hello,\nworld!")

    def test_multiline_string_empty(self):
        result = loads('"""\n"""')
        self.assertEqual(result, "")

    def test_multiline_string_single_newline(self):
        result = loads('"""\n\n"""')
        self.assertEqual(result, "\n")

    def test_multiline_string_with_quotes(self):
        result = loads('""" " """')
        self.assertEqual(result, ' " ')
        result = loads('""" "" """')
        self.assertEqual(result, ' "" ')

    def test_array_empty(self):
        self.assertEqual(loads("[]"), [])

    def test_array_simple(self):
        self.assertEqual(loads("[1,2,3]"), [1, 2, 3])
        self.assertEqual(loads('["red","yellow","green"]'), ["red", "yellow", "green"])

    def test_array_newline_separated(self):
        result = loads('[\n  1\n  2\n  3\n]')
        self.assertEqual(result, [1, 2, 3])

    def test_array_trailing_comma(self):
        self.assertEqual(loads('["red", "yellow", "green",]'), ["red", "yellow", "green"])

    def test_array_mixed_types(self):
        result = loads('[1, "two", true, null]')
        self.assertEqual(result, [1, "two", True, None])

    def test_object_empty(self):
        self.assertEqual(loads("{}"), {})

    def test_object_simple(self):
        result = loads('{"a":1,"b":2}')
        self.assertEqual(result, {"a": 1, "b": 2})

    def test_object_with_spaces(self):
        result = loads(' { "a" : 1 , "b" : 2 } ')
        self.assertEqual(result, {"a": 1, "b": 2})

    def test_object_newline_separated(self):
        result = loads('{\n  a: 1\n  b: 2\n}')
        self.assertEqual(result, {"a": 1, "b": 2})

    def test_object_trailing_comma(self):
        result = loads('{\n  a: 1,\n  b: 2,\n}')
        self.assertEqual(result, {"a": 1, "b": 2})

    def test_object_identifier_keys(self):
        result = loads('{ foo: "bar", baz_qux: 123, key-name: true }')
        self.assertEqual(result, {"foo": "bar", "baz_qux": 123, "key-name": True})

    def test_object_quoted_keys(self):
        result = loads('{ "key with spaces": "value", "": "empty key" }')
        self.assertEqual(result, {"key with spaces": "value", "": "empty key"})

    def test_object_duplicate_keys(self):
        with self.assertRaises(MAMLSyntaxError):
            loads('{ "a": 1, "a": 2 }')

    def test_comments(self):
        result = loads('# Comment\n{"a":1}')
        self.assertEqual(result, {"a": 1})

    def test_inline_comments(self):
        result = loads('{\n  foo: "value" # comment\n}')
        self.assertEqual(result, {"foo": "value"})

    def test_comment_not_in_string(self):
        result = loads('{"bar": "# This is not a comment"}')
        self.assertEqual(result, {"bar": "# This is not a comment"})

    def test_leading_zeros_not_allowed(self):
        with self.assertRaises(MAMLSyntaxError):
            loads("01")

    def test_nested_structures(self):
        result = loads('{"a": [1, 2, {"b": 3}], "c": {"d": [4, 5]}}')
        self.assertEqual(result, {"a": [1, 2, {"b": 3}], "c": {"d": [4, 5]}})


    def test_multiline_string_unterminated(self):
        with self.assertRaises(MAMLSyntaxError):
            loads('"""hello')

    def test_multiline_string_empty_invalid(self):
        with self.assertRaises(MAMLSyntaxError):
            loads('""""""')

    def test_string_unescaped_newline(self):
        with self.assertRaises(MAMLSyntaxError):
            loads('"hello\nworld"')

    def test_string_unescaped_control_character(self):
        with self.assertRaises(MAMLSyntaxError):
            loads('"hello\x0cworld"') # \f is form feed, 0x0c

    def test_array_trailing_comma_empty(self):
        with self.assertRaises(MAMLSyntaxError):
            loads('[ , ]')

    def test_object_trailing_comma_empty(self):
        with self.assertRaises(MAMLSyntaxError):
            loads('{ , }')

    def test_extra_tokens_after_valid_document(self):
        with self.assertRaises(MAMLSyntaxError):
            loads(' "hello" "world" ')
        with self.assertRaises(MAMLSyntaxError):
            loads('{} []')

    def test_large_integer(self):
        large_int_str = "9007199254740992" # 2**53
        large_int = 9007199254740992
        self.assertEqual(loads(large_int_str), large_int)
        self.assertIsInstance(loads(large_int_str), int)


class TestEncoder(unittest.TestCase):

    def test_encode_null(self):
        self.assertEqual(dumps(None), "null")

    def test_encode_boolean(self):
        self.assertEqual(dumps(True), "true")
        self.assertEqual(dumps(False), "false")

    def test_encode_integer(self):
        self.assertEqual(dumps(42), "42")
        self.assertEqual(dumps(-100), "-100")

    def test_encode_float(self):
        self.assertEqual(dumps(3.14), "3.14")

    def test_encode_string(self):
        self.assertEqual(dumps("hello"), '"hello"')

    def test_encode_string_with_escapes(self):
        self.assertEqual(dumps("hello\nworld"), '"""\nhello\nworld\n"""')
        self.assertEqual(dumps('quote"'), '"quote\\""')

    def test_encode_empty_array(self):
        self.assertEqual(dumps([]), "[]")

    def test_encode_array(self):
        result = dumps([1, 2, 3])
        self.assertIn("[\n", result)
        self.assertIn("1", result)
        self.assertIn("2", result)
        self.assertIn("3", result)

    def test_encode_empty_object(self):
        self.assertEqual(dumps({}), "{}")

    def test_encode_object(self):
        result = dumps({"a": 1, "b": 2})
        self.assertIn("{\n", result)
        self.assertIn("a: 1", result)
        self.assertIn("b: 2", result)

    def test_roundtrip(self):
        data = {"key": "value", "number": 42, "array": [1, 2, 3]}
        encoded = dumps(data)
        decoded = loads(encoded)
        self.assertEqual(decoded, {"key": "value", "number": 42, "array": [1, 2, 3]})


if __name__ == "__main__":
    unittest.main()
