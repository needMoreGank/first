#to-do:
"""
shortcut:
the "whole table" = unneeded
table column conts:
just row

sort alphabetically while still preserving order... LITERALLY just by
list.sort method OR sorted func --> (list, key = str.lower)


"""
punctuation_list = [".","?","!",",",";",":"]

import sys
sys.stdin = open("KWIC.txt")
input = sys.stdin.readline

max_before_len = 0
max_word_len = 0
max_after_len = 0

def KWIC(sentence_list, bad_list, upper, lower):
    global max_before_len
    global max_word_len
    global max_after_len
    words_list = []
    relevant_list = []

    #print("old sentence:",sentence_list)
    #print("new sentence:",sentence_list)

    for item in sentence_list:
        if item.lower() not in bad_list and item.lower() not in punctuation_list:
            words_list.append(item)
        #else:
            #print("Word at index",sentence_list.index(item),"rejected due to being badword as",item)
        
    words_list.sort(key = str.lower)
    #print("filtered words_list:",words_list)

    #relevant_list = words_list[lower:upper+1] #remember cp counting is exclusive for end
    #wow this is never used; later bounds are just used in conditional
    #print("relevant_list:",relevant_list)

    startindex = 0
    max_before_len = 0
    max_word_len = 0
    max_after_len = 0

    def words_before_after(word,prev_word, startindex):
        #actually return the calc'd whole row
        #print("\nword:",word,"prev_word:",prev_word)
        before_list = []
        after_list = []
        row = []
        #startindex = 0
        if word == prev_word:
            #index error will occur
            startindex = sentence_list.index(prev_word,startindex)+1
            #print("updated startindex:",startindex)
        else:
            startindex = 0

        for i in range(1,4): #so that i matches with the subtraction/addition to be used
            before_word = sentence_list[sentence_list.index(word,startindex)-i]
            #print(i,"before:",before_word)

            if before_word.lower() in bad_list or before_word.lower() in punctuation_list:
                #print("before_word is badword:",before_word)
                break

            before_list.append(before_word)

        for i in range(1,4):
            after_word = sentence_list[sentence_list.index(word,startindex)+i]
            #print(i,"after:",after_word)
            if after_word.lower() in bad_list or after_word.lower() in punctuation_list:
                #print("after_word is badword:",after_word)
                break
            after_list.append(after_word)

        before_list.reverse()
        #print("before_list:",before_list)
        #print("after_list:",after_list)

        row.append(before_list)
        row.append(word)
        row.append(after_list)
        #print("row:",row)
        return row

    def row_char_count(row):
        count = 0
            #should be 3 times
        for item in row:
            for i in item:
                count += len(i)
        return count

    max_row = []
    max_row_count = 0

    def record_maxes(row):
        global max_before_len
        global max_word_len
        global max_after_len
        row_before_len = 0
        row_word_len = 0
        row_after_len = 0

        for i in range(3):
            if i == 0:
                before = row[i]
                for item in before:
                    row_before_len += len(item)
                    #ACCOUNT FOR THE SPACES!
                row_before_len += len(before)-1
                max_before_len = max(max_before_len,row_before_len)
                #print("max_before_len:",max_before_len)
            elif i == 1:
                word = row[i]
                for item in word:
                    row_word_len += len(item)
                max_word_len = max(max_word_len,row_word_len)
                #print("max_word_len:",max_word_len)
            elif i == 2:
                after = row[i]
                for item in after:
                    row_after_len += len(item)
                row_after_len += len(after)-1
                max_after_len = max(max_after_len,row_after_len)
                #print("max_after_len:",max_after_len)

    def format_output(max_row,max_before_len,max_word_len,max_after_len):
        before = max_row[0]
        word = max_row[1]
        after = max_row[2]
        format_before = " ".join(before).rjust(max_before_len,"-")
        format_word = "<"+word.ljust(max_word_len,"-")+">"
        format_after = " ".join(after).ljust(max_after_len,"-")
        format_row = format_before + " " + format_word + " " + format_after
        #print("formatted row:",format_row)
        return format_row

    def dash_count(row,max_before_len,max_word_len,max_after_len):
        #print("dash_count of row:",row)
        #returns dash count
        before_len = 0
        word_len = 0
        after_len = 0

        for i in range(3):
            if i == 0:
                before = row[i]
                for item in before:
                    before_len += len(item)
                    #ACCOUNT FOR THE SPACES!
                if len(before)>0:
                    before_len += len(before)-1
                #else:
                    #print("no content; do not penalize 0 len")
                #print("before_len:",before_len)
            
            elif i == 1:
                word = row[i]
                for item in word:
                    word_len += len(item)
                #print("word_len:",word_len)
                
            elif i == 2:
                after = row[i]
                for item in after:
                    after_len += len(item)
                if len(after) > 0:
                    after_len += len(after)-1
                #else:
                    #print("no content; do not penalize 0 len")
                #print("after_len:",after_len)

        before_dashes = max_before_len - before_len
        word_dashes = max_word_len - word_len
        after_dashes = max_after_len - after_len
        return before_dashes + word_dashes + after_dashes
                
        
        

    for w in range(len(words_list)):
        word = words_list[w]
        prev_word = words_list[w-1]
        word_row = words_before_after(word,prev_word,startindex)
        record_maxes(word_row)

    for w in range(len(words_list)):
    #for w in range(1):
        word = words_list[w]
        prev_word = words_list[w-1]
        #words_before_after(word,prev_word)
        #now create the 2-d list
        word_row = words_before_after(word,prev_word,startindex)
        word_row_count = row_char_count(word_row)
        #print("word_row_count:",word_row_count)

        if lower <= w <= upper:
            if word_row_count > max_row_count:
                #print("update!")
                max_row_count = word_row_count
                max_row = word_row
            elif word_row_count == max_row_count:
                #print("tie in word count. must compare dash counts")
                #print("curr_word_row's dash count:", dash_count(word_row,max_before_len,max_word_len,max_after_len), "max_word_row's dash count:",dash_count(max_row,max_before_len,max_word_len,max_after_len))
                if dash_count(word_row,max_before_len,max_word_len,max_after_len) < dash_count(max_row,max_before_len,max_word_len,max_after_len):
                    #print("update succeeded")
                    max_row_count = word_row_count
                    max_row = word_row
                #else:
                    #print("update failed")
                

    #print("final max_row:",max_row)
    #print("final max_before_len:",max_before_len)
    #print("final max_word_len:",max_word_len)
    #print("final max_after_len:",max_after_len)

    return format_output(max_row,max_before_len,max_word_len,max_after_len)

    


    #add meat onto words_list; make it 2-dimensional list




def main():
    #sentence = input("Sentence: ")
    for i in range(5):
        sentence = input()
        for char in sentence:
            if char in punctuation_list:
                sentence = sentence.replace(char," "+char)
        #print("cleaned sentence:",sentence)
        sentence_list = sentence.strip().split(" ")
        #badword_list = input("Unimportant words: ").split(" ")
        badword_list = input().strip().split(" ")
        #print(badword_list)
        #upperbound, lowerbound = input("Inclusive range: ").split(" ")
        lowerbound, upperbound = input().strip().split(" ")
        #bounds are given by 1-based index
        #row 3 is list index 2
        upperbound = int(upperbound)-1
        lowerbound = int(lowerbound)-1

        print("\n")
        print(KWIC(sentence_list, badword_list, upperbound, lowerbound))

main()

