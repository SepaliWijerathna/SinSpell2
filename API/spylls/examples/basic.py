import pathlib
path = pathlib.Path(__file__).parent  / 'si_LK'

from spylls.hunspell import Dictionary

dictionary = Dictionary.from_files(str(path))

def detector_fun(file_content):    
    # file_content = word
   
    # characters = [".",",","%","!","@","&"]
    # test_string = ''.join(i for i in file_content if not i in characters)


    check_list = file_content.split(" ")
    incorrect_word_list = []
    correct_word_list = []
    # result = file_content
    word_list = []
    print(word_list)
    for item in check_list:
        if item!="":
            if item[-1] == ".":
                word_list.append(item[:-1])
                word_list.append(item[-1:])
            else: 
                word_list.append(item)
    print(word_list)

    for word in word_list:
        if dictionary.lookup(word):            
            correct_word_list.append(word)
        else:            
            incorrect_word_list.append(word)
                
    return incorrect_word_list,correct_word_list,word_list
   