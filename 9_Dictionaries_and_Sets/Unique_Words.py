# (b) Unique Words
# Write a program that opens a specified text file then displays
# a list of all the unique words found in the file. A word is
# defined as made up of letters only. No numbers, commas etc.
# are part of the word.  Include the frequency of the occurrence
# of each word (10 points)

# Also, display the total count of the unique words found. (5 points)

# The text file to use Download use.

# Hint: Store each word as an element of a set (required)

import string


def unique_words(filename):

  obj = {}

  with open(filename, 'r') as file:
    for line in file:
      words = line.split()
      for word in words:
        clean_word = word.strip(string.punctuation).lower()
        if clean_word.isalpha():
          obj[clean_word] = obj.get(clean_word, 0) + 1

  return obj


def main():

  word_count = unique_words("text.txt")

  print("\n* Unique words and their frequencies *")
  print("-" * 37)
  for word, count in word_count.items():
    print(f"{word}: {count}")

  print("-" * 33)
  print(f"Total count of unique words: {len(word_count)}")

if __name__ == "__main__":
  main()
