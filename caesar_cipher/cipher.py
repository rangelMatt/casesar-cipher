import re
from corpus_loader import word_list, name_list
# signature has their type, which might be a function that takes in nothing and returns nothing. The signature for encrypt is two arguments. one string in, and one string out

letters_cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters_lower = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plain,shift): # encrypt, needs a plain and key
  encrypted_message = ""
  
  for letter in plain:
    if letter.isupper():
      start_index = letters_cap.index(letter)
      new_index = (start_index + shift) % 26
      new_letter = letters_cap[new_index]
      encrypted_message += new_letter
    elif letter.islower():
        start_index = letters_lower.index(letter)
        new_index = (start_index + shift) % 26
        new_letter = letters_lower[new_index]
        encrypted_message += new_letter
    else:
      encrypted_message += letter
  return encrypted_message


    
  #   if letter != " ":
  #     if (letter.isupper()):
  #       encrypted_message += chr((ord(letter) + shift-65) % 26 + 65)
        
  #     else:
  #       encrypted_message += chr((ord(letter) + shift - 97) % 26 + 97)
  #   else:
  #     encrypted_message += " "
  #   if not letter.isalpha():
  #     encrypted_message += letter
  # return encrypted_message
      
# encrypt("abc",1)

def decrypt(encoded, key):
  return encrypt(encoded, -key)


def count_words(text):

    crack_phrase = text.split()

    word_count = 0

    for crack_word in crack_phrase:
        word = re.sub(r'[^A-Za-z]+','', crack_word)
        if word.lower() in word_list or word in name_list:
            # print("english word", word)
            word_count += 1

    return word_count
  
def crack(text):
  for i in range(26):
        cracked_text = decrypt(text, i)
        word_count = count_words(cracked_text)
        decimal = int(word_count / len(text.split()))
        if decimal > .5:
            return cracked_text

  return ''

