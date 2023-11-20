user = input()
word = "hello"

def translation(word1, word2):
    i = 0  
    for letter in word2:
        while i < len(word1) and word1[i] != letter:
            i += 1
        if i == len(word1):
            return False
        i += 1
    return True

if translation(user, word):
    print("YES")
else:
    print("NO")
