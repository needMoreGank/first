from operator import itemgetter
'''
Lex Strings

Name: <your name>
'''
#
# Complete the 'rearrangedString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#

"""
Instructions
1. Keep only the alphanumeric chars (0-9, A-Z, a-z)
- clarity: sort them into order (just use sorted() lol)
2. Group the same characters together into "blocks"
3. Each block has a length. Group blocks that have same len into "Blocks of n len"
- block is ordered by longest -> shortest
4. The order of blocks inside their group: 0th (longest) group = ascending, next descending, switches
- ascending order: numbers -> Caps -> lowers
5. Final output ex: 6in
- 6 = block len group, in = ascending order of group types

"""

def form_blocks(saved_chars):
    key = None
    curr_block = None
    blocks = []
    for item_num in range(len(saved_chars)):
        if saved_chars[item_num] != key:
            key = saved_chars[item_num]
            print("new key:",key)
            curr_block = saved_chars[item_num]
            blocks.append(curr_block)
        else:
            blocks[-1] += key
            print("added on.")
            print("updated curr_block.len:",len(curr_block))

    print("done with process")

    for item in blocks:
        print(item)

    return blocks

def compress(blocks):
    overall_list = []
    while len(blocks) != 0:
        curr_len_list = []
        item = blocks[0]
        curr_len = len(item)
        curr_len_list.append(str(curr_len))
        dummy_blocks = blocks.copy()

        while len(dummy_blocks) != 0:
            print("\nlen(dummy_blocks):",len(dummy_blocks))
            print("dummy_blocks:",dummy_blocks)
            curr_item = dummy_blocks[0]
            print("curr_item:",curr_item)
            if len(curr_item) == curr_len:
                curr_len_list.append(curr_item[0])
                blocks.remove(curr_item)
            dummy_blocks.pop(0)
        overall_list.append(curr_len_list)
        print("big cycle done. blocks:",blocks)
        print("overall_list:",overall_list)
        #if len(blocks) != 0:
            #blocks.pop(0)
    
    return overall_list


def rearrangedString(s):
    saved_chars = []
    for char_num in range(len(s)):
        if s[char_num].isalnum():
            #print(s[char_num], "is saved")
            saved_chars.append(s[char_num])
    #print(saved_chars)
    saved_chars = sorted(saved_chars)

    blocks = form_blocks(saved_chars)
    #print(blocks)
    overall_list = sorted(compress(blocks), key=itemgetter(0), reverse=True)

    print(overall_list)

    final_list = []

    for block in overall_list:
        curr_str = block[0]
        block.pop(0)
        block_num = overall_list.index(block) + 1
        if block_num % 2 == 1:
            block = sorted(block)
            final_list.append(curr_str + "".join(block))
        elif block_num % 2 == 0:
            block = sorted(block, reverse=True)
            final_list.append(curr_str + "".join(block))
    
    print(final_list)
    return ",".join(final_list)




print(rearrangedString("COVID-19 is a global pandemic and a virus that changed everything in the entire world."))
"""
7ae,6ni,5t,4rhd,3gl,2vsoc,119CDIOVbmpuwy
7ae,6ni,5t,4rhd,3gl,2vsoc,119CDIOVbmpuwy
"""