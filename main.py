import string
def is_pangram(s):
    check = 'abcdefghijklmnopqrstuvwxyz'
    for i in check:
        if i not in s.lower():
            return False
    return True

