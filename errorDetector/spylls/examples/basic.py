import pathlib
path = pathlib.Path(__file__).parent  / 'si_LK'

from spylls.hunspell import Dictionary

dictionary = Dictionary.from_files(str(path))

def detector_fun(word):
    print(word)
    file_content = word
   
    characters = [".",",","%","!","@","&"]
    test_string = ''.join(i for i in file_content if not i in characters)


    word_list = test_string.split(" ")
    print(word_list)
    incorrect_word_list = []
    result = file_content

    for word in word_list:
        if dictionary.lookup(word):
            print("correct")
        else: 
            print("Incorrect")   
            marked = "\u0332".join(word+ " ")
            result = result.replace(word,marked)
            incorrect_word_list.append(word)
            print(incorrect_word_list)
    
    return incorrect_word_list
    # print('Output: '+result+'\n')
    # print("Suggestions :")
    # for incorrect_word in incorrect_word_list:
    #     print("incorrect")
    #     print([*dictionary.suggest(incorrect_word)])

#........................

# input_words = input("Enter your words: ")
# word_list = input_words.split(" ")
# correct_word_list = []
# incorrect_word_list = []

# for word in word_list:
#     if dictionary.lookup(word):
#         correct_word_list.append(word)
#     else:
#         incorrect_word_list.append(word)

# print("Correct_word_list :")
# print(correct_word_list)
# print("Incorrect_word_list :")
# print(incorrect_word_list)

# print("Suggestions :")
# for incorrect_word in incorrect_word_list:
#     print([*dictionary.suggest(incorrect_word)])

#........................

# print(dictionary.lookup('මල්'))
# print(dictionary.lookup('ළමයා'))
# print([*dictionary.suggest('කලගුන')])
