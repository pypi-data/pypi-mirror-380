import logging
from io import TextIOBase
from typing import Callable, TypeVar

from simplini.core import IniConfigBase, IniConfigOption, IniConfigSection

T = TypeVar("T")


LOGGER = logging.getLogger(__name__)


class ParsingError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.position = None


class RecursiveDescentParserBase:
    def __init__(self, text_io):
        self.text_io = text_io

    def parsing_error(self, message):
        position = self.text_io.tell()
        message += " (position: %d)" % position
        error = ParsingError(message)
        error.position = position
        return error

    def expect(self, expected: str) -> str:
        char = self.text_io.read(1)

        if char != expected:
            raise self.parsing_error(f'Expected "{expected}", but encountered "{char}"')

        return char

    def expect_eof(self) -> None:
        char = self.text_io.read(1)

        if char != "":
            raise self.parsing_error(f'Expected EOF, but encountered "{char}"')

        return None

    def accept(
        self, value_or_predicate: Callable[[str], bool] | str
    ) -> tuple[bool, str | None]:
        char = self.text_io.read(1)

        # reached EOF
        if char == "":
            return False, None

        if not callable(value_or_predicate):

            def predicate(c: str) -> bool:
                return c == value_or_predicate
        else:
            predicate = value_or_predicate
            assert callable(predicate)

        if not predicate(char):
            self.text_io.seek(self.text_io.tell() - 1)
            return False, None

        return True, char

    def accept_multiple(
        self,
        value_or_predicate: Callable[[str], bool] | str,
        default_value: str | None = None,
    ) -> tuple[bool, str | None]:
        chars = ""
        accepted, char = self.accept(value_or_predicate)

        if not accepted:
            return False, default_value

        while accepted:
            assert char is not None
            chars += char
            accepted, char = self.accept(value_or_predicate)

        return True, chars

    # TODO: make sure to make it obvious that zero or multiple occurrences are accepted
    def multiple(self, parse_fn: Callable[[], T]) -> list[T]:
        results = []

        while True:
            ok, result = self.optional(parse_fn)

            if not ok:
                break

            assert result is not None
            results.append(result)

        return results

    def optional(self, parse_fn: Callable[[], T]) -> tuple[bool, T | None]:
        position = self.text_io.tell()

        try:
            result = parse_fn()
            return True, result
        except ParsingError:
            self.text_io.seek(position)
            return False, None

    def choice(self, parse_fns: list[Callable[[], T]]) -> tuple[int, T]:
        last_error = None
        position = self.text_io.tell()

        for parser_idx, parse_fn in enumerate(parse_fns):
            try:
                result = parse_fn()
                return parser_idx, result
            except ParsingError as e:
                last_error = e
                self.text_io.seek(position)

        assert last_error is not None
        raise last_error

    def peek(self, length: int) -> T:
        position = self.text_io.tell()
        peeked = self.text_io.read(length)
        self.text_io.seek(position)
        return peeked

    def hinted_choice(self, hinted_parse_fns: list[tuple[str, Callable[[], T]]]) -> T:
        position = self.text_io.tell()
        last_error = None

        for hint, parse_fn in hinted_parse_fns:
            if hint:
                peeked = self.peek(len(hint))

                # hint matched, so we know this branch is what we need
                if hint == peeked:
                    return parse_fn()
            else:  # empty hint, attempt the branch and go to next if not successful
                try:
                    return parse_fn()
                except ParsingError as e:
                    self.text_io.seek(position)
                    last_error = e

        assert last_error is not None
        raise last_error


# TODO: provide more context in ParsingError exceptions
#  include the parsing stack, and position in the file (line/column)
class IniParser(RecursiveDescentParserBase):
    def __init__(self, text_io: TextIOBase):
        super().__init__(text_io)
        self.allow_unquoted_values = True
        self.key_value_separator = "="
        self.comment_separator = "#"
        self.escape_character = "\\"
        self.quote_character = '"'

    def parse_quoted_string(self) -> str:
        self.parse_whitespaces()

        self.expect(self.quote_character)

        value = ""

        while True:
            char = self.text_io.read(1)

            if char == self.escape_character:
                next_char = self.text_io.read(1)
                value += next_char
            elif char == "\n":
                raise self.parsing_error("New line in quoted string is forbidden")
            else:  # normal character
                if char == self.quote_character:
                    break
                value += char

        # trailing whitespaces
        self.parse_whitespaces()

        return value

    def parse_triple_quoted_string(self) -> str:
        self.parse_whitespaces()

        self.expect(self.quote_character)
        self.expect(self.quote_character)
        self.expect(self.quote_character)

        value = ""

        while True:
            char = self.text_io.read(1)

            if char == self.escape_character:
                next_char = self.text_io.read(1)
                value += next_char
            else:  # normal character:
                if char == self.quote_character:
                    # check if it's the end of the triple-quoted string
                    next_char = self.text_io.read(1)
                    if next_char == self.quote_character:
                        next_next_char = self.text_io.read(1)
                        if next_next_char == self.quote_character:
                            break
                        else:
                            value += char + next_char + next_next_char
                    else:
                        value += char + next_char
                else:
                    value += char

        # trailing whitespaces
        self.parse_whitespaces()

        return value

    def parse_unquoted_string(self) -> str:
        self.parse_whitespaces()

        _, value = self.accept_multiple(
            lambda c: c not in ("\n", self.comment_separator),
            # even if nothing is accepted we consider the value to be empty
            default_value="",
        )

        assert value is not None

        # strip trailing spaces
        value = value.rstrip()

        if self.quote_character in value:
            raise self.parsing_error(
                "Quote character inside non-quoted strings is forbidden as ambiguous"
            )

        # trailing whitespaces
        self.parse_whitespaces()

        return value

    def parse_option_name(self) -> str:
        def is_option_name_char(c: str) -> bool:
            return c.isalnum() or c in ("_", "-", ".", ":")

        _, option_name = self.accept_multiple(
            is_option_name_char,
        )

        if not option_name:
            raise self.parsing_error("Expected option name to be non-empty string")

        return option_name

    def parse_option_value(self) -> str:
        if self.allow_unquoted_values:
            return self.hinted_choice(
                [
                    (self.quote_character * 3, self.parse_triple_quoted_string),
                    (self.quote_character, self.parse_quoted_string),
                    (None, self.parse_unquoted_string),
                ]
            )
        else:
            return self.hinted_choice(
                [
                    (self.quote_character * 3, self.parse_triple_quoted_string),
                    (
                        self.quote_character,
                        self.parse_quoted_string,
                    ),
                ]
            )

    def parse_option(self) -> IniConfigOption:
        comments = self.parse_comments()
        self.parse_whitespaces()
        option_name = self.parse_option_name()
        self.parse_whitespaces()
        self.expect(self.key_value_separator)
        self.parse_whitespaces()

        option_value = self.parse_option_value()

        _, inline_comment = self.optional(self.parse_comment_line)
        self.multiple(self.parse_empty_line)

        option = IniConfigOption(option_name, option_value)
        option.comment = comments
        option.inline_comment = inline_comment
        return option

    def is_whitespace(self, char: str) -> bool:
        return char in (" ", "\t")

    def parse_whitespaces(self):
        self.accept_multiple(self.is_whitespace)

    def parse_section_body(self, section: IniConfigSection) -> None:
        options = self.multiple(self.parse_option)

        for option in options:
            assert option is not None

            if option.key in section.options:
                raise self.parsing_error(
                    f'Option "{option.key}" was present multiple times'
                )

            section.options[option.key] = option

    def parse_comment_line(self) -> str:
        self.accept_multiple(self.is_whitespace)
        self.expect(self.comment_separator)

        _, comment = self.accept_multiple(
            lambda c: c != "\n",
            default_value="",
        )

        # accept new line if present as well
        self.accept("\n")

        # strip leading/trailing spaces
        return comment.strip()

    def parse_empty_line(self) -> str:
        line = self.text_io.readline()

        if not line:
            raise self.parsing_error("Expected empty line, but encountered EOF")

        if line.strip():
            raise self.parsing_error("Expected empty line")

        return line

    def parse_comments(self) -> list[str]:
        def parse_comment_or_empty_line() -> tuple[int, str]:
            parser_idx, parsed_value = self.choice(
                [
                    self.parse_comment_line,
                    self.parse_empty_line,
                ]
            )
            return parser_idx, parsed_value

        parsed = self.multiple(parse_comment_or_empty_line)

        # drop empty lines
        comment_lines = [line for idx, line in parsed if idx == 0]

        # strip the comments
        return [comment.strip() for comment in comment_lines]

    def parse_section(self) -> IniConfigSection:
        comments = self.parse_comments()

        # parse section name
        self.expect("[")

        _, section_name = self.accept_multiple(
            lambda c: c not in ("]", "\n"),
            default_value="",
        )

        if not section_name:
            raise self.parsing_error("Expected section name to be non-empty")

        self.expect("]")

        section = IniConfigSection(section_name)
        section.comment = comments

        self.parse_section_body(section)

        return section

    def parse_main(self, config: IniConfigBase):
        # first comments need a little bit edge-case processing because of the
        # inherent ambiguity as they apply to the:
        # * next option if it exists,
        # * OR to the next section if it exists,
        # * OR to the comment for unnamed section otherwise;
        first_comments = self.parse_comments()

        # parse default section
        config.unnamed_section = IniConfigSection(None)
        self.parse_section_body(config.unnamed_section)

        # then any number of other sections
        sections = self.multiple(self.parse_section)

        # attribute first comments
        if config.unnamed_section.options:
            first_option = next(iter(config.unnamed_section.options.values()))
            first_option.comment = first_comments
        elif sections:
            first_section = sections[0]
            first_section.comment = first_comments
        else:
            config.unnamed_section.comment = first_comments

        for section in sections:
            assert section is not None

            if section.name in config.sections:
                raise self.parsing_error(
                    f'Section "{section.name}" was present multiple times'
                )

            config.sections[section.name] = section

        config.trailing_comment = self.parse_comments()

        self.expect_eof()

        return config

    # TODO: when our parsing error does end up being raised there it would
    #  be nice to extend it with the context showing the line from the config
    #  and marker where the reading head is (probably making it configurable
    #  makes sense so that we do not leak config?)
    def parse_into(self, instance: IniConfigBase):
        try:
            self.parse_main(instance)
        except ParsingError:
            LOGGER.debug("Parsing error occurred", exc_info=True)
            raise
