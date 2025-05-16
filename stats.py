
import re
import sys

#print(f"--sys--:{sys.orig_argv[2]}")

if len(sys.argv) < 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)

filepath = sys.orig_argv[2]

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
  return f"{len(split_list)} total words found in the document"

def into_aSet(book_content):
  lower_cases = book_content.lower()
  replaced_chars1 = re.sub(r"[^\w\s]+", " ", lower_cases)
  replaced_chars2 = re.sub(r"[\_\d]+", " ", replaced_chars1)
  split_list = replaced_chars2.split()
  aSet = set(split_list)
  #print(aSet)
  return len(aSet) # number set of unique words

def sort_crit(key):
  return list(key.values())[0]

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
  charC_list = []
  for kvpair in char_count:
    charC_list.append({kvpair: char_count[kvpair]})
  charC_list.sort(reverse=True, key=sort_crit)
  return charC_list