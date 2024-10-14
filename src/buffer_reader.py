from __future__ import annotations

EMPTY_SPACES = {" ", "\n", "\r", "\t"}
QUOTES = {'"', "'"}


class BufferReader:
    def __init__(self, buffer: str) -> None:
        """Initialize the TextBuffer with the provided buffer.

        Args:
            buffer (str): The input text buffer to be processed.
        """
        self.lines = buffer.splitlines(keepends=True)
        self.line_pointer: int = 0
        self.char_pointer: int = 0
        self.output: str = self.lines[0][0]

    def move(self, move_pointer: int) -> bool:
        """Move the pointer based on the provided offset.

        Args:
            move_pointer (int): The number of characters to move the pointer.
        """
        if move_pointer == 0:
            return True

        move_line_pointer = self.line_pointer
        move_char_pointer = self.char_pointer
        if move_pointer > 0:
            while move_line_pointer < len(self.lines) and move_pointer > 0:
                if move_pointer > len(self.lines[move_line_pointer]) - move_char_pointer:
                    move_pointer -= len(self.lines[move_line_pointer]) - move_char_pointer
                    move_char_pointer = 0
                    move_line_pointer += 1
                else:
                    move_char_pointer += move_pointer
                    move_pointer = 0
        else:
            move_pointer = -1 * move_pointer
            while move_line_pointer >= 0 and move_pointer > 0:
                if move_pointer > move_char_pointer:
                    move_pointer -= move_char_pointer + 1
                    move_line_pointer -= 1
                    move_char_pointer = len(self.lines[move_line_pointer]) - 1
                else:
                    move_char_pointer -= move_pointer
                    move_pointer = 0

        if move_pointer == 0:
            self.line_pointer = move_line_pointer
            self.char_pointer = move_char_pointer
            self.output = self.lines[self.line_pointer][self.char_pointer]
            return True
        else:
            self.output = ""
            return False

    def read(self, length: int = 1) -> bool:
        if length == 0:
            raise ValueError("Read length must be less than 0 or greater than 0.")

        result = ""
        length_line_pointer = self.line_pointer
        length_char_pointer = self.char_pointer
        if length > 0:
            while length_line_pointer < len(self.lines) and length > 0:
                if length > len(self.lines[length_line_pointer]) - length_char_pointer:
                    length -= len(self.lines[length_line_pointer]) - length_char_pointer
                    result += self.lines[length_line_pointer][length_char_pointer:]
                    length_char_pointer = 0
                    length_line_pointer += 1
                else:
                    length_char_pointer += length
                    result += self.lines[length_line_pointer][length_char_pointer - length : length_char_pointer]
                    length = 0
        else:
            length = -1 * length
            while length_line_pointer >= 0 and length > 0:
                if length > length_char_pointer:
                    length -= length_char_pointer + 1
                    result += self.lines[length_line_pointer][: length_char_pointer + 1]
                    length_line_pointer -= 1
                    length_char_pointer = len(self.lines[length_line_pointer]) - 1
                else:
                    result = (
                        self.lines[length_line_pointer][length_char_pointer - length + 1 : length_char_pointer + 1]
                        + result
                    )
                    length_char_pointer -= length
                    length = 0

        if length == 0:
            self.output = result
            return True
        else:
            self.output = ""
            return False

    def skip(self) -> None:
        """Moves the pointer forward until a non-empty space is found, without initially moving the pointer."""
        while True:
            if self.output is None:
                break
            if self.output not in EMPTY_SPACES:
                break
