from buffer_reader import BufferReader

# Move tests
def test__move_pointer_greather_than_0_same_line():
    buffer = BufferReader("123456789\nabcdefghij")
    buffer.char_pointer = 2
    assert buffer.move(7) == True
    assert buffer.line_pointer == 0
    assert buffer.char_pointer == 9

def test__move_pointer_greather_than_0_next_line():
    buffer = BufferReader("123456789\nabcdefghij")
    buffer.char_pointer = 2
    assert buffer.move(11) == True
    assert buffer.line_pointer == 1
    assert buffer.char_pointer == 3

def test__move_pointer_greather_than_0_overflow():
    buffer = BufferReader("123456789\nabcdefghij")
    buffer.char_pointer = 2
    assert buffer.move(20) == False
    assert buffer.line_pointer == 0
    assert buffer.char_pointer == 2

def test__move_pointer_lesser_than_0_same_line():
    buffer = BufferReader("123456789\nabcdefghij")
    buffer.char_pointer = 4
    buffer.line_pointer = 1
    assert buffer.move(-2) == True
    assert buffer.line_pointer == 1
    assert buffer.char_pointer == 2

def test__move_pointer_lesser_than_0_next_line():
    buffer = BufferReader("123456789\nabcdefghij")
    buffer.char_pointer = 3
    buffer.line_pointer = 1
    assert buffer.move(-11) == True
    assert buffer.line_pointer == 0
    assert buffer.char_pointer == 2


def test__move_pointer_lesser_than_0_overflow():
    buffer = BufferReader("123456789\nabcdefghij")
    buffer.char_pointer = 2
    assert buffer.move(-20) == False
    assert buffer.line_pointer == 0
    assert buffer.char_pointer == 2

# Read tests

def test__read_greather_than_0_same_line():
    buffer = BufferReader("123456789\nabcdefghij")
    buffer.char_pointer = 4
    assert buffer.read(3) == True
    assert buffer.output == "567"

def test__read_pointer_greather_than_0_next_line():
    buffer = BufferReader("123456789\nabcdefghij")
    buffer.char_pointer = 4
    assert buffer.read(11) == True
    assert buffer.output == "56789\nabcde"

def test__read_pointer_greather_than_0_overflow():
    buffer = BufferReader("123456789\nabcdefghij")
    buffer.char_pointer = 2
    assert buffer.read(20) == False
    assert buffer.output == ""


def test__read_pointer_lesser_than_0_same_line():
    buffer = BufferReader("123456789\nabcdefghij")
    buffer.char_pointer = 4
    buffer.line_pointer = 1
    assert buffer.read(-2) == True
    assert buffer.output == "de"


def test__read_pointer_lesser_than_0_next_line():
    buffer = BufferReader("123456789\nabcdefghij")
    buffer.char_pointer = 4
    buffer.line_pointer = 1
    assert buffer.read(-10) == True
    assert buffer.char_pointer == 4
    assert buffer.line_pointer == 1
    assert buffer.output == "6789\nabcde"



def test__read_pointer_lesser_than_0_overflow():
    buffer = BufferReader("123456789\nabcdefghij")
    buffer.char_pointer = 4
    buffer.line_pointer = 1
    assert buffer.read(-20) == False
    assert buffer.output == ""
