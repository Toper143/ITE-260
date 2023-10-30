import time
import random

with open("./popular.txt") as file:
    words = file.read().split("\n")
    new_words = [word.lower() for word in filter(
        lambda word: 
            all([letter.lower() in "abcdefghijklmnopqrstuvwxyz" for letter in word]) and 
            5 <= len(word),
        words
    )]

    new_easy_words = [word.lower() for word in filter(
        lambda word: 
            all([letter.lower() in "abcdefghijklmnopqrstuvwxyz" for letter in word]) and 
            4 <= len(word) <= 6,
        words
    )]

    new_medium_words = [word.lower() for word in filter(
        lambda word: 
            all([letter.lower() in "abcdefghijklmnopqrstuvwxyz" for letter in word]) and 
            5 <= len(word) <= 8,
        words
    )]

    new_hard_words = [word.lower() for word in filter(
        lambda word: 
            all([letter.lower() in "abcdefghijklmnopqrstuvwxyz" for letter in word]) and 
            5 <= len(word),
        words
    )]
    

    def anagrams(words):
        # very efficient :) even more efficient than the solutions online
        scrambled_dict = {}
        anagram_dict = {}

        for word in new_words:
            sorted_word = "".join(sorted(word))
            if sorted_word not in scrambled_dict:
                scrambled_dict[sorted_word] = [word]
            else:
                scrambled_dict[sorted_word].append(word)
        for sorted_word in scrambled_dict:
            if len(scrambled_dict[sorted_word]) > 1:
                anagram_dict[sorted_word] = scrambled_dict[sorted_word]

        return anagram_dict

    anagrams_dict = anagrams(new_words)
    

    def anagram_generator():
        key = random.sample(list(anagrams_dict.keys()), 1)[0]
        return [key, anagrams_dict[key]]

    def anagram_generator_diff(difficulty):
        new_diff_words = new_easy_words if difficulty == "easy" else new_medium_words if difficulty == "medium" else new_hard_words

        anagrams_diff_dict = anagrams(new_diff_words)

        scrambled_dict = {}
        anagram_dict = {}

        for word in new_diff_words:
            sorted_word = "".join(sorted(word))
            if sorted_word not in scrambled_dict:
                scrambled_dict[sorted_word] = [word]
            else:
                scrambled_dict[sorted_word].append(word)
        for sorted_word in scrambled_dict:
            if len(scrambled_dict[sorted_word]) > 1:
                anagram_dict[sorted_word] = scrambled_dict[sorted_word]

        key = random.sample(list(anagram_dict.keys()), 1)[0]
        return [key, anagram_dict[key]]

    def shuffle(word):
        return "".join(random.sample(word, k = len(word)))
    
    # print(anagram_generator())

    # print(anagrams_dict)