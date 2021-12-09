# Author: SCT (AMDG) 12/9/21

def letter_in(word,letter):
    amount = 0

    for x in word:
        if x == letter:
            amount += 1
    return amount

print(letter_in("cat", "t") == 1)
print(letter_in("apple", "p") == 2)
print(letter_in("supercalifragilisticexpialidocious", "i") == 7)
