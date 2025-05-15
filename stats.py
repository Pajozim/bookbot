
import re

filepath = "books/frankenstein.txt"

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read() # read(300): only 300 characters
    return file_contents

book_content = get_book_text(filepath)
 
def limit_to_5_lines(book_content):
  lines = book_content.splitlines()
  limited_text = lines[:5]
  return "\n".join(limited_text)

book_content_5l = limit_to_5_lines(book_content)

def count_words(book_content):
  #print(type(book_content))
  num_words = book_content.count(" ") # I guess, it has to be very strict .txt ... I wonder
  split_list = book_content.split()
  #print(num_words, " & ", len(split_list), " & ",num_words + 1 == len(split_list))
  return f"{len(split_list)} words found in the document"

def into_aSet(book_content):
  lower_cases = book_content.lower()
  replaced_chars1 = re.sub(r"[^\w\s]+", " ", lower_cases)
  replaced_chars2 = re.sub(r"[\_\d]+", " ", replaced_chars1)
  split_list = replaced_chars2.split()
  aSet = set(split_list)
  print(aSet)
  return len(aSet) # number of words

def count_chars(book_content):
  lower_cases = book_content.lower()
  cleaned_string = re.sub(r'[\s\W\d\_]', '', lower_cases)
  char_set = set(cleaned_string)
  uChar_list = list(char_set)
  uChar_list.sort()
  char_count = {}
  for char in uChar_list:
    char_count[f"{char}"] = 0
  for key in list(char_count.keys()):
    for char in cleaned_string:
      if char == key:
        char_count[f"{char}"] += 1
        continue
  return char_count