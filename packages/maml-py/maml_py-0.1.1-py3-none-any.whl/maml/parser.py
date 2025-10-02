from typing import Any, Dict, List, Optional
from .lexer import Lexer, Token, TokenType
from .exceptions import MAMLSyntaxError


class Parser:
    def __init__(self, text: str):
        self.lexer = Lexer(text)
        self.tokens = self.lexer.tokenize()
        self.pos = 0

    def error(self, message: str) -> MAMLSyntaxError:
        token = self.current_token()
        return MAMLSyntaxError(message, token.line, token.column)

    def current_token(self) -> Token:
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return self.tokens[-1]

    def peek_token(self, offset: int = 0) -> Token:
        pos = self.pos + offset
        if pos < len(self.tokens):
            return self.tokens[pos]
        return self.tokens[-1]

    def advance(self) -> Token:
        token = self.current_token()
        if token.type != TokenType.EOF:
            self.pos += 1
        return token

    def expect(self, token_type: TokenType) -> Token:
        token = self.current_token()
        if token.type != token_type:
            raise self.error(f"Expected {token_type}, got {token.type}")
        return self.advance()

    def parse(self) -> Any:
        value = self.parse_value()
        if self.current_token().type != TokenType.EOF:
            raise self.error("Expected end of input")
        return value

    def parse_value(self) -> Any:
        token = self.current_token()

        if token.type == TokenType.LEFT_BRACE:
            return self.parse_object()
        elif token.type == TokenType.LEFT_BRACKET:
            return self.parse_array()
        elif token.type == TokenType.STRING:
            self.advance()
            return token.value
        elif token.type == TokenType.MULTILINE_STRING:
            self.advance()
            return token.value
        elif token.type == TokenType.INTEGER:
            self.advance()
            return token.value
        elif token.type == TokenType.FLOAT:
            self.advance()
            return token.value
        elif token.type == TokenType.TRUE:
            self.advance()
            return True
        elif token.type == TokenType.FALSE:
            self.advance()
            return False
        elif token.type == TokenType.NULL:
            self.advance()
            return None
        else:
            raise self.error(f"Unexpected token: {token.type}")

    def parse_object(self) -> Dict[str, Any]:
        self.expect(TokenType.LEFT_BRACE)
        obj: Dict[str, Any] = {}
        # note: commas are optional between entries
        while self.current_token().type != TokenType.RIGHT_BRACE:
            if self.current_token().type == TokenType.EOF:
                raise self.error("unclosed object")

            key = self.parse_key()

            if key in obj:
                raise self.error(f"duplicate key '{key}'")

            self.expect(TokenType.COLON)
            value = self.parse_value()
            obj[key] = value

            if self.current_token().type == TokenType.COMMA:
                self.advance()

        self.expect(TokenType.RIGHT_BRACE)
        return obj

    def parse_key(self) -> str:
        token = self.current_token()

        if token.type == TokenType.STRING:
            self.advance()
            return token.value
        elif token.type == TokenType.IDENTIFIER:
            self.advance()
            return token.value
        elif token.type == TokenType.INTEGER:
            self.advance()
            return str(token.value)
        else:
            raise self.error(f"Expected key, got {token.type}")

    def parse_array(self) -> List[Any]:
        self.expect(TokenType.LEFT_BRACKET)
        arr: List[Any] = []

        while self.current_token().type != TokenType.RIGHT_BRACKET:
            if self.current_token().type == TokenType.EOF:
                raise self.error("unclosed array")

            value = self.parse_value()
            arr.append(value)

            if self.current_token().type == TokenType.COMMA:
                self.advance()

        self.expect(TokenType.RIGHT_BRACKET)
        return arr
