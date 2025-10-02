from typing import Optional, List
from enum import Enum, auto
from .exceptions import MAMLSyntaxError


class TokenType(Enum):
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    COLON = auto()
    COMMA = auto()
    STRING = auto()
    MULTILINE_STRING = auto()
    INTEGER = auto()
    FLOAT = auto()
    TRUE = auto()
    FALSE = auto()
    NULL = auto()
    IDENTIFIER = auto()
    EOF = auto()


class Token:
    def __init__(self, type: TokenType, value: any, line: int, column: int):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self) -> str:
        return f"Token({self.type}, {self.value!r}, {self.line}, {self.column})"


class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []

    def error(self, message: str) -> MAMLSyntaxError:
        return MAMLSyntaxError(message, self.line, self.column)

    def peek(self, offset: int = 0) -> Optional[str]:
        pos = self.pos + offset
        if pos < len(self.text):
            return self.text[pos]
        return None

    def advance(self) -> Optional[str]:
        if self.pos >= len(self.text):
            return None
        char = self.text[self.pos]
        self.pos += 1
        if char == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        return char

    def skip_whitespace(self) -> None:
        while self.peek() in (" ", "\t", "\n", "\r"):
            self.advance()

    def skip_comment(self) -> None:
        if self.peek() == "#":
            while self.peek() is not None and self.peek() not in ("\n", "\r"):
                char = self.peek()
                if ord(char) < 0x20 and char != "\t":
                    raise self.error(f"can't have control chars in comments")
                if ord(char) == 0x7F:
                    raise self.error(f"can't have control chars in comments")
                self.advance()

    def skip_whitespace_and_comments(self) -> None:
        while True:
            if self.peek() in (" ", "\t", "\n", "\r"):
                self.skip_whitespace()
            elif self.peek() == "#":
                self.skip_comment()
            else:
                break

    def read_string(self) -> str:
        start_line = self.line
        start_column = self.column
        self.advance()
        result = []

        while True:
            char = self.peek()
            if char is None:
                raise MAMLSyntaxError("Unterminated string", start_line, start_column)
            if char == '"':
                self.advance()
                break
            if char == "\\":
                self.advance()
                escape = self.peek()
                if escape is None:
                    raise MAMLSyntaxError(
                        "Unterminated string escape", self.line, self.column
                    )
                if escape == "t":
                    result.append("\t")
                    self.advance()
                elif escape == "n":
                    result.append("\n")
                    self.advance()
                elif escape == "r":
                    result.append("\r")
                    self.advance()
                elif escape == '"':
                    result.append('"')
                    self.advance()
                elif escape == "\\":
                    result.append("\\")
                    self.advance()
                elif escape == "u":
                    self.advance()
                    if self.peek() != "{":
                        raise self.error("unicode escape must be \\u{...}")
                    self.advance()
                    hex_digits = ""
                    while True:
                        hex_char = self.peek()
                        if hex_char == "}":
                            break
                        if hex_char is None or hex_char not in "0123456789ABCDEFabcdef":
                            raise self.error("bad unicode escape")
                        hex_digits += hex_char
                        self.advance()
                    if len(hex_digits) < 1 or len(hex_digits) > 6:
                        raise self.error("unicode escape must have 1-6 hex digits")
                    self.advance()
                    code_point = int(hex_digits, 16)
                    if code_point > 0x10FFFF:
                        raise self.error("unicode code point out of range")
                    if 0xD800 <= code_point <= 0xDFFF:
                        raise self.error("unicode surrogate not allowed")
                    result.append(chr(code_point))
                else:
                    raise self.error(f"Invalid escape sequence: \\{escape}")
            elif char in ("\n", "\r"):
                raise self.error("newline must be escaped")
            elif ord(char) < 0x20 and char != "\t":
                raise self.error("control chars aren't allowed")
            elif ord(char) == 0x7F:
                raise self.error("control chars aren't allowed")
            else:
                result.append(char)
                self.advance()

        return "".join(result)

    def read_multiline_string(self) -> str:
        start_line = self.line
        start_column = self.column

        for _ in range(3):
            if self.peek() != '"':
                raise MAMLSyntaxError(
                    "Expected multiline string delimiter", start_line, start_column
                )
            self.advance()

        has_leading_newline = False
        if self.peek() == "\n":
            self.advance()
            has_leading_newline = True

        result = []
        while True:
            char = self.peek()
            if char is None:
                raise MAMLSyntaxError(
                    "Unterminated multiline string", start_line, start_column
                )

            if char == '"' and self.peek(1) == '"' and self.peek(2) == '"':
                self.advance()
                self.advance()
                self.advance()
                break
            else:
                result.append(char)
                self.advance()

        final_str = "".join(result)
        if not has_leading_newline and not final_str:
            raise MAMLSyntaxError(
                "Multiline strings cannot be empty", start_line, start_column
            )

        return final_str

    def read_number(self) -> Token:
        start_line = self.line
        start_column = self.column
        num_str = ""
        # TODO: verify this handles edge cases properly
        is_negative = False

        if self.peek() == "-":
            is_negative = True
            num_str += self.advance()

        if self.peek() == "0":
            num_str += self.advance()
            if self.peek() is not None and self.peek().isdigit():
                raise MAMLSyntaxError("no leading zeros", start_line, start_column)
        elif self.peek() is not None and self.peek().isdigit():
            while self.peek() is not None and self.peek().isdigit():
                num_str += self.advance()
        else:
            raise self.error("Invalid number")

        if self.peek() == ".":
            num_str += self.advance()
            if self.peek() is None or not self.peek().isdigit():
                raise self.error("need digit after decimal")
            while self.peek() is not None and self.peek().isdigit():
                num_str += self.advance()

            if self.peek() in ("e", "E"):
                num_str += self.advance()
                if self.peek() in ("+", "-"):
                    num_str += self.advance()
                if self.peek() is None or not self.peek().isdigit():
                    raise self.error("Digit required in exponent")
                while self.peek() is not None and self.peek().isdigit():
                    num_str += self.advance()

            return Token(TokenType.FLOAT, float(num_str), start_line, start_column)

        if self.peek() in ("e", "E"):
            num_str += self.advance()
            if self.peek() in ("+", "-"):
                num_str += self.advance()
            if self.peek() is None or not self.peek().isdigit():
                raise self.error("Digit required in exponent")
            while self.peek() is not None and self.peek().isdigit():
                num_str += self.advance()

            return Token(TokenType.FLOAT, float(num_str), start_line, start_column)

        value = int(num_str)
        if value < -(2**63) or value > (2**63 - 1):
            raise MAMLSyntaxError("Integer out of range", start_line, start_column)

        return Token(TokenType.INTEGER, value, start_line, start_column)

    def read_identifier(self) -> str:
        result = []
        while self.peek() is not None:
            ch = self.peek()
            if ch.isalnum() or ch in ("_", "-"):
                result.append(ch)
                self.advance()
            else:
                break
        return "".join(result)

    def tokenize(self) -> List[Token]:
        while self.pos < len(self.text):
            self.skip_whitespace_and_comments()

            if self.pos >= len(self.text):
                break

            char = self.peek()
            line = self.line
            column = self.column

            if char == "{":
                self.advance()
                self.tokens.append(Token(TokenType.LEFT_BRACE, "{", line, column))
            elif char == "}":
                self.advance()
                self.tokens.append(Token(TokenType.RIGHT_BRACE, "}", line, column))
            elif char == "[":
                self.advance()
                self.tokens.append(Token(TokenType.LEFT_BRACKET, "[", line, column))
            elif char == "]":
                self.advance()
                self.tokens.append(Token(TokenType.RIGHT_BRACKET, "]", line, column))
            elif char == ":":
                self.advance()
                self.tokens.append(Token(TokenType.COLON, ":", line, column))
            elif char == ",":
                self.advance()
                self.tokens.append(Token(TokenType.COMMA, ",", line, column))
            elif char == '"':
                if self.peek(1) == '"' and self.peek(2) == '"':
                    value = self.read_multiline_string()
                    self.tokens.append(
                        Token(TokenType.MULTILINE_STRING, value, line, column)
                    )
                else:
                    value = self.read_string()
                    self.tokens.append(Token(TokenType.STRING, value, line, column))
            elif char == "-" or char.isdigit():
                token = self.read_number()
                self.tokens.append(token)
            elif char.isalpha() or char == "_":
                identifier = self.read_identifier()
                if identifier == "true":
                    self.tokens.append(Token(TokenType.TRUE, True, line, column))
                elif identifier == "false":
                    self.tokens.append(Token(TokenType.FALSE, False, line, column))
                elif identifier == "null":
                    self.tokens.append(Token(TokenType.NULL, None, line, column))
                else:
                    self.tokens.append(
                        Token(TokenType.IDENTIFIER, identifier, line, column)
                    )
            else:
                raise self.error(f"Unexpected character: {char!r}")

        self.tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return self.tokens
