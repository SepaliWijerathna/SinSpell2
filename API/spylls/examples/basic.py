import pathlib
path = pathlib.Path(__file__).parent  / 'si_LK'

from spylls.hunspell import Dictionary

dictionary = Dictionary.from_files(str(path))

def detector_fun(word):
    #print(word)
    file_content = word
   
    characters = [".",",","%","!","@","&"]
    test_string = ''.join(i for i in file_content if not i in characters)


    word_list = file_content.split(" ")
    #print(word_list)
    incorrect_word_list = []
    correct_word_list = []
    result = file_content

    for word in word_list:
        if dictionary.lookup(word):
            # print("correct")
            correct_word_list.append(word)
        else: 
            # print("Incorrect")   
            # marked = "\u0332".join(word+ " ")
            # result = result.replace(word,marked)
            incorrect_word_list.append(word)
            # print(incorrect_word_list)
    
    return incorrect_word_list,correct_word_list,word_list
   