Q1. What is palindrome and example?
ANS. a word, phrase, sentence, or number that reads the <b> same </b> backward or forward.
# example
# is_palindrome("madam") ------> True
# is_palindrome("naman") ------> True
# is_palindrome("horse") ------> False

# logic (algoritham)
# step 1 -> reverse the string
# step 2 -> compare string with original string

def is_palindrom(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False
      
print(is_palindrom("naman"))
print(is_palindrom("horse"))
      
      
      
  
# Output
$ python Exercise1.py
True
False
