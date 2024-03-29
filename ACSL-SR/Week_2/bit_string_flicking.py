"""
Bit-String Flicking

Name: <Your Name>
"""

"""
Bit string flicking is a simple operation that can be performed on a binary string.
It involves FLIPPING the bits of the binary string, where 0s become 1s and 1s become 0s.

Here are four logical operations that can be performed on two binary strings:
    - Bitwise NOT
    - Bitwise AND
    - Bitwise OR
    - Bitwise XOR
    
The bitwise NOT operation is performed on a single binary string, while the other three
operations are performed on two binary strings.
The bitwise NOT operation flips the bits of a binary string, where 0s become 1s and 1s become 0s.
ex) 1010 -> 0101

The bitwise AND operation compares two binary strings bit by bit, and returns a new binary string
where a bit is 1 if the corresponding bits of the two binary strings are both 1, and 0 otherwise.
ex) 1010 & 1100 -> 1000

The bitwise OR operation compares two binary strings bit by bit, and returns a new binary string
where a bit is 1 if at least one of the corresponding bits of the two binary strings is 1, and 0 otherwise.
ex) 1010 | 1100 -> 1110

The bitwise XOR operation compares two binary strings bit by bit, and returns a new binary string
where a bit is 1 if the corresponding bits of the two binary strings are different, and 0 otherwise.
"MUST be OR" -- matching values must be DIFFERENT to yield 1
ex) 1010 ^ 1100 -> 0110

Python automatically categorizes "0" as FALSE and any other valid value present as TRUE
"""


def bitwise_and(binary1, binary2):
    """
    Performs a bitwise AND operation on two binary numbers.

    Args:
    binary1, binary2 (str): Binary numbers represented as strings.

    Returns:
    str: The result of the bitwise AND operation as a binary string.
    """
    return_str = ""
    for index_num in range(len(binary1)):
        #btw range is automatically last val exclusive (enables 0 to n-1 operations)
        bin1_char = int(binary1[index_num])
        bin2_char = int(binary2[index_num])
        if bin1_char and bin2_char:
            return_str += "1"
        else:
            return_str += "0"
            
    return return_str

    


def bitwise_or(binary1, binary2):
    """
    Performs a bitwise OR operation on two binary numbers.

    Args:
    binary1, binary2 (str): Binary numbers represented as strings.

    Returns:
    str: The result of the bitwise OR operation as a binary string.
    """
    # Your code here
    return_str = ""
    for index_num in range(len(binary1)):
        #btw range is automatically last val exclusive (enables 0 to n-1 operations)
        bin1_char = int(binary1[index_num])
        bin2_char = int(binary2[index_num])
        if bin1_char or bin2_char:
            return_str += "1"
        else:
            return_str += "0"
            
    return return_str


def bitwise_xor(binary1, binary2):
    """
    Performs a bitwise XOR operation on two binary numbers.

    Args:
    binary1, binary2 (str): Binary numbers represented as strings.

    Returns:
    str: The result of the bitwise XOR operation as a binary string.
    """
    # Your code here
    return_str = ""
    for index_num in range(len(binary1)):
        #btw range is automatically last val exclusive (enables 0 to n-1 operations)
        bin1_char = int(binary1[index_num])
        bin2_char = int(binary2[index_num])
        if bin1_char and bin2_char:
            return_str += "0"
        elif bin1_char:
            return_str += "1"
        elif bin2_char:
            return_str += "1"
        else:
            return_str += "0"
            
    return return_str


"""
Shift operators are used to shift the bits of a binary string left or right.
The left shift operator (<<) shifts the bits of a binary string to the left by a specified number of bits.
The right shift operator (>>) shifts the bits of a binary string to the right by a specified number of bits.
In the ACSL's LSHIFT and RSHIFT, the bits that are shifted off the end are discarded and the empty spaces
are filled with zeroes.
ex)
1010 << 2 -> 1000
1010 >> 2 -> 0010
"""


# ex) LSHIFT([0, 1, 1, 0, 1], 2) -> [1, 0, 1, 0, 0]
def LSHIFT(bit_list, shifts):
    """
    Performs a left shift operation on a list of bits.

    Args:
    bit_list (list of int): The list of bits to shift, where each bit is represented as an integer (1 or 0).
    shifts (int): The number of places to shift. The bits that are shifted off the end are discarded.

    Returns:
    list of int: The bit_list after the left shift, with the empty spaces filled with zeroes.
    """
    # Your code here
    return_list = []
    for item_index in range(len(bit_list)):
        try:
            item = bit_list[item_index]
            return_list.append(bit_list[item_index + shifts])
        except IndexError:
            for item in range(shifts):
                return_list.append(0)
            return return_list

#print(LSHIFT([1, 0, 1, 0], 2))
#[1, 0, 0, 0]


# ex) RSHIFT([0, 1, 1, 0, 1], 2) -> [0, 0, 0, 1, 1]
def RSHIFT(bit_list, shifts):
    """
    Performs a right shift operation on a list of bits.

    Args:
    bit_list (list of int): The list of bits to shift, where each bit is represented as an integer (1 or 0).
    shifts (int): The number of places to shift. The bits that are shifted off the end are discarded.

    Returns:
    list of int: The bit_list after the right shift, with the empty spaces filled with zeroes.
    """
    # Your code here
    return_list = []
    for item in range(shifts):
        return_list.append(0)
    for item_index in range(len(bit_list)-shifts):
        item = bit_list[item_index]
        #print("item:",item)
        return_list.append(bit_list[item_index])
    return return_list

#print(RSHIFT([1, 0, 1, 0], 2))
#[0, 0, 1, 0]


"""
The LCIRC (left circular shift) and RCIRC (right circular shift) operations work similarly to the
LSHIFT and RSHIFT operations, but instead of discarding the shifted-off bits and filling the spaces
with zeroes, LCIRC and RCIRC recycle the shifted-off bits back to the other end.
ex)
RCIRC-2 01101 -> 01011
LCIRC-2 01101 -> 10101
"""


# ex) LCIRC([0, 1, 1, 0, 1], 2) -> [1, 0, 1, 0, 1]
def LCIRC(bit_list, shifts):
    """
    Performs a left circular shift on a list of bits.

    Args:
    bit_list (list of int): The list of bits to shift, where each bit is represented as an integer (1 or 0).
    shifts (int): The number of places to shift. If shifts is greater than the length of bit_list, it wraps around.

    Returns:
    list of int: The bit_list after the left circular shift.
    """
    # Your code here
    pass


# ex) RCIRC([0, 1, 1, 0, 1], 2) -> [0, 1, 0, 1, 1]
def RCIRC(bit_list, shifts):
    """
    Performs a right circular shift on a list of bits.

    Args:
    bit_list (list of int): The list of bits to shift, where each bit is represented as an integer (1 or 0).
    shifts (int): The number of places to shift. If shifts is greater than the length of bit_list, it wraps around.

    Returns:
    list of int: The bit_list after the right circular shift.
    """
    # Your code here
    pass


"""
test cases ----------------------------------------------------------------------------------------------
"""


def test_bitwise_and():
    print('Testing bitwise_and()...', end='')
    assert bitwise_and('1010', '1100') == '1000'
    assert bitwise_and('1010', '1111') == '1010'
    assert bitwise_and('0000', '1111') == '0000' or '0'
    assert bitwise_and('1111', '1111') == '1111'
    assert bitwise_and('1010101010', '1111111111') == '1010101010'
    assert bitwise_and('1010101010', '0000000000') == '0000000000' or '0'
    assert bitwise_and('0000000000', '1111111111') == '0000000000' or '0'
    assert bitwise_and('0000000000', '0000000000') == '0000000000' or '0'
    assert bitwise_and('1111111111', '1111111111') == '1111111111'
    assert bitwise_and('1111111111', '0000000000') == '0000000000' or '0'
    print('Passed.')


def test_bitwise_or():
    print('Testing bitwise_or()...', end='')
    assert bitwise_or('1010', '1100') == '1110'
    assert bitwise_or('1010', '1111') == '1111'
    assert bitwise_or('0000', '1111') == '1111'
    assert bitwise_or('1111', '1111') == '1111'
    assert bitwise_or('1010101010', '1111111111') == '1111111111'
    assert bitwise_or('1010101010', '0000000000') == '1010101010'
    assert bitwise_or('0000000000', '1111111111') == '1111111111'
    assert bitwise_or('0000000000', '0000000000') == '0000000000' or '0'
    assert bitwise_or('1111111111', '1111111111') == '1111111111'
    assert bitwise_or('1111111111', '0000000000') == '1111111111'
    print('Passed.')


def test_bitwise_xor():
    print('Testing bitwise_xor()...', end='')
    assert bitwise_xor('1010', '1100') == '0110' or '110'
    assert bitwise_xor('1010', '1111') == '0101' or '101'
    assert bitwise_xor('0000', '1111') == '1111'
    assert bitwise_xor('1111', '1111') == '0000' or '0'
    assert bitwise_xor('1010101010', '1111111111') == '0101010101' or '1010101010'
    assert bitwise_xor('1010101010', '0000000000') == '1010101010'
    assert bitwise_xor('0000000000', '1111111111') == '1111111111'
    assert bitwise_xor('0000000000', '0000000000') == '0000000000' or '0'
    assert bitwise_xor('1111111111', '1111111111') == '0000000000' or '0'
    assert bitwise_xor('1111111111', '0000000000') == '1111111111'
    print('Passed.')


def test_LSHIFT():
    print('Testing LSHIFT()...', end='')
    assert LSHIFT([1, 0, 1, 0], 2) == [1, 0, 0, 0]
    assert LSHIFT([1, 0, 1, 0], 3) == [0, 0, 0, 0]
    assert LSHIFT([1, 0, 1, 0], 4) == [0, 0, 0, 0]
    assert LSHIFT([1, 1, 0, 1, 0], 2) == [0, 1, 0, 0, 0]
    assert LSHIFT([1, 1, 0, 1, 0], 3) == [1, 0, 0, 0, 0]
    assert LSHIFT([1, 1, 0, 1, 0], 4) == [0, 0, 0, 0, 0]
    print('Passed.')


def test_RSHIFT():
    print('Testing RSHIFT()...', end='')
    assert RSHIFT([1, 0, 1, 0], 2) == [0, 0, 1, 0]
    assert RSHIFT([1, 0, 1, 0], 3) == [0, 0, 0, 1]
    assert RSHIFT([1, 0, 1, 0], 4) == [0, 0, 0, 0]
    assert RSHIFT([1, 1, 0, 1, 0], 2) == [0, 0, 1, 1, 0]
    assert RSHIFT([1, 1, 0, 1, 0], 3) == [0, 0, 0, 1, 1]
    assert RSHIFT([1, 1, 0, 1, 0], 4) == [0, 0, 0, 0, 1]
    print('Passed.')


def test_LCIRC():
    print('Testing LCIRC()...', end='')
    assert LCIRC([1, 0, 1, 0], 2) == [1, 0, 1, 0]
    assert LCIRC([1, 0, 1, 0], 3) == [0, 1, 0, 1]
    assert LCIRC([1, 0, 1, 0], 4) == [1, 0, 1, 0]
    assert LCIRC([1, 0, 1, 0], 5) == [0, 1, 0, 1]
    assert LCIRC([1, 1, 0, 1, 0], 2) == [0, 1, 0, 1, 1]
    assert LCIRC([1, 1, 0, 1, 0], 3) == [1, 0, 1, 1, 0]
    assert LCIRC([1, 1, 0, 1, 0], 4) == [0, 1, 1, 0, 1]
    print('Passed.')


def test_RCIRC():
    print('Testing RCIRC()...', end='')
    assert RCIRC([1, 0, 1, 0], 2) == [1, 0, 1, 0]
    assert RCIRC([1, 0, 1, 0], 3) == [0, 1, 0, 1]
    assert RCIRC([1, 0, 1, 0], 4) == [1, 0, 1, 0]
    assert RCIRC([1, 0, 1, 0], 5) == [0, 1, 0, 1]
    assert RCIRC([1, 1, 0, 1, 0], 2) == [1, 0, 1, 1, 0]
    assert RCIRC([1, 1, 0, 1, 0], 3) == [0, 1, 0, 1, 1]
    assert RCIRC([1, 1, 0, 1, 0], 4) == [1, 0, 1, 0, 1]
    print('Passed.')

"""
def test_all():
    test_bitwise_and()
    test_bitwise_or()
    test_bitwise_xor()
    test_LSHIFT()
    test_RSHIFT()
    test_LCIRC()
    test_RCIRC()


if __name__ == '__main__':
    test_all()
"""

test_RSHIFT()