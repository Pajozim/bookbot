from stats import book_content, filepath
from stats import count_chars, count_words

def main():
  print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...\n -----------Word Count ----------")
  print(f"Found {count_words(book_content)}\n--------- Character Count -------")
  for dictblock in count_chars(book_content)[:5]:
    print(f"{list(dictblock.keys())[0]}: {list(dictblock.values())[0]}")
  print("============= END ===============")

main()