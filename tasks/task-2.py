from collections import deque

strg = ''
d = deque()
def is_palindrome(text):
    text = text.replace(" ", "").lower()
    char_deque = deque(text)
    
    while len(char_deque) > 1:
        first = char_deque.popleft()
        last = char_deque.pop()
        if first != last:
            return False

    return True
        