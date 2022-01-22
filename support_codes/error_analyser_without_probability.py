import re
from collections import Counter 
import numpy as np
import pandas as pd
import io

error_dict={}
delete_error_dict={}
insert_error_dict={}
replace_error_dict ={}
switch_error_dict={}

def process_data(file_name):
    read_data = open(file_name,encoding="utf-8").read()
    return read_data

vocab = process_data("Error_Corrector/text_data/correct_unique_words.txt")

def get_count(vocab):
    vocab=vocab.splitlines( )
    word_count_dict = {}
    for i in range (1,len(vocab)):
        word=vocab[i].split(" ")
        if(vocab[i]==''):
            continue
        if word[0]=='තත්වයන්':
          print('hi')
        key=word[0]
        try:
            value=int(word[1])
        except:
            print(key)
            print('Can not convert', str ,"to int")

        word_count_dict[key] = value
    return word_count_dict

word_count_dict = get_count(vocab)

"""Insert Letters (correct --> error)"""

def insert_letter(word):
    
    delete_l = []
    split_l = []
    
    split_l=[(word[:i],word[i:]) for i in range(len(word))]
    for L,R in split_l:
      del_l=[]
      del_l.append(L+R[1:])
      x=(R[0])
      del_l.append("ins("+x+")")
      delete_l.append(del_l)
    return delete_l

def get_corrections_insert(my_word, word_count_dict):
  
  suggestions = []
  n_best = []
  edit_one_letter= insert_letter(my_word)
  # print(edit_one_letter)
  for word1 in edit_one_letter:

    if word1[0] in word_count_dict and word1 not in suggestions :
      del_error=[]
      del_error.append(word1[0])
      del_error.append(word1[1])
      del_error.append(my_word)
      # print(suggestions)
      suggestions.append(del_error)
  
  return suggestions

#print(get_corrections_insert("ලමයා", word_count_dict))

"""Switch letters"""

def switch_letter(word):
    
    switch_l = []
    split_l = []
    
    split_l =[(word[:i],word[i:]) for i in range(len(word)+1)]
    for L,R in split_l:
      if (len(R)>=2):
        swit_l=[]
        swit_l.append(L+R[1]+R[0]+R[2:])
        swit_l.append("trans("+R[1]+","+R[0]+")")
        switch_l.append(swit_l)
   
    return switch_l


def get_corrections_switch(my_word, word_count_dict):
  
  suggestions = []
  n_best = []
  edit_one_letter= switch_letter(my_word)
  # print(edit_one_letter)

  for word1 in edit_one_letter:
    if word1[0] in word_count_dict:
      switch_error=[]
      switch_error.append(word1[0])
      switch_error.append(word1[1])
      switch_error.append(my_word)
      suggestions.append(switch_error)
        
  return suggestions

# print(get_corrections_switch("ලමයා", word_count_dict))

"""Replace letter"""

def replace_letter(word):
   
    letters = '්ාෘුැූෑිීෙේෛොෝෞෘෲෟෳංඃකගඛඝඞඟචඡජඣඤඥඦටඨඩඪණඬතථදධනඳපඵබභමඹයරලළව‍ශෂසෆක්‍ෂඅආඇඈඉඊඋඌාඑඒඓඔඕඖඍඎඏඐංඃ'
    # ්ාෘුැූෑිීෙේෛොෝෞෘෲෟෳංඃ
    replace_l = []
    split_l = []
    
    split_l =[(word[:i],word[i:]) for i in range(len(word))]
    # print(split_l)
    for l in letters:
        for R,L in split_l:
            rep_l=[]
            if len(L)> 1:
                rep_l.append(R+l+L[1:])
                rep_l.append("sub("+l+","+L[0]+")")
                replace_l.append(rep_l)
            else:
                rep_l.append(R+l)
                rep_l.append("sub("+l+","+L[0]+")")
                replace_l.append(rep_l)
    
  
    for i in replace_l:
      if i[0]==word:
         replace_l.remove(i)
    
    return replace_l

# replace_letter("ලමා")

def get_corrections_replace(my_word, word_count_dict):
  
  suggestions = []
  n_best = []
  edit_one_letter= replace_letter(my_word)
#   print(edit_one_letter)
  
  for word1 in edit_one_letter:
    if word1[0] in word_count_dict and word1 not in suggestions :
        replace_error=[]
        replace_error.append(word1[0])
        replace_error.append(word1[1])
        replace_error.append(my_word)
        suggestions.append(replace_error)

  return suggestions

print(get_corrections_replace("ලමයා", word_count_dict))

"""Insert letter"""

def delete_letter(word):
    
    letters = '්ාෘුැූෑිීෙේෛොෝෞෘෲෟෳංඃකගඛඝඞඟචඡජඣඤඥඦටඨඩඪණඬතථදධනඳපඵබභමඹයරලළව‍ශෂසෆක්‍ෂඅආඇඈඉඊඋඌාඑඒඓඔඕඖඍඎඏඐංඃ'
    insert_l = []
    split_l = []
    
    split_l =[(word[:i],word[i:]) for i in range(len(word)+1)]
    for c in letters:
      for R,L in split_l:
        ins_l=[]
        ins_l.append(R+c+L)
        ins_l.append("del("+c+")")
        insert_l.append(ins_l)
    
    return insert_l

# insert_letter("සියළු")

def get_corrections_delete(my_word, word_count_dict):
  
  suggestions = []
  n_best = []
  edit_one_letter= delete_letter(my_word)
  # print(edit_one_letter)
  
  for word1 in edit_one_letter:
    if word1[0] in word_count_dict and word1 not in suggestions :
      insert_error=[]
      insert_error.append(word1[0])
      # insert_error.append(value(word1[0]))
      insert_error.append(word1[1])
      insert_error.append(my_word)
      # print(suggestions)
      suggestions.append(insert_error)
        

  return suggestions

print(get_corrections_delete("ලමයා", word_count_dict))

def edit_one_letter(word, allow_switches = True):
   
    edit_one_set = set()
   
    switch_word_l = get_corrections_switch(word,word_count_dict)
    delete_word_l = get_corrections_delete(word,word_count_dict)
    replace_word_l= get_corrections_replace(word,word_count_dict)
    insert_word_l= get_corrections_insert(word,word_count_dict)
    edit_one_set_list = switch_word_l+delete_word_l+replace_word_l+insert_word_l
   
    return edit_one_set_list

# print(edit_one_letter("ලමයා"))

def get_corrections(my_word, word_count_dict):
    suggestions = []
    n_best = []
    tmp_edit_one_set = edit_one_letter(my_word)
    # print(tmp_edit_one_set)
    
    return tmp_edit_one_set

# my_word = "ලමයා" 
# frequency=700
# tmp_corrections = get_corrections(my_word, word_count_dict)
# print(tmp_corrections)
# frq_error_word=int(frequency/len(tmp_corrections))
# print(frq_error_word)

# for i in tmp_corrections:
#   if i[1][0]=='t':
#     if i[1] in switch_error_dict:
#       key=i[1]
#       val=switch_error_dict[key]
#       switch_error_dict[key]=val+frq_error_word
#     else: 
#       key = i[1]
#       switch_error_dict[key]=frq_error_word

#   elif i[1][0]=='d':
#     if i[1] in delete_error_dict:
#       key=i[1]
#       val=delete_error_dict[key]
#       delete_error_dict[key]=val+frq_error_word
#     else: 
#       key = i[1]
#       delete_error_dict[key]=frq_error_word

#   elif i[1][0]=='i':
#     if i[1] in insert_error_dict:
#       key=i[1]
#       val=insert_error_dict[key]
#       insert_error_dict[key]=val+frq_error_word
#     else: 
#       key = i[1]
#       insert_error_dict[key]=frq_error_word

#   elif i[1][0]=='s':
#     if i[1] in replace_error_dict:
#       key=i[1]
#       val=replace_error_dict[key]
#       replace_error_dict[key]=val+frq_error_word
#     else: 
#       key = i[1]
#       replace_error_dict[key]=frq_error_word


# print(replace_error_dict)
# print(insert_error_dict)
# print(delete_error_dict)
# print(switch_error_dict)


suggestion_faild=[]
error_word = process_data(r'Data_Procssing/text_data/error_words.txt')
error_word= error_word.splitlines( )
for word in error_word: 
  try:
    my_word = word.split(' ')[0]
    tmp_corrections = get_corrections(my_word, word_count_dict)
    # print(tmp_corrections)
    frq_error_word=int(int(word.split(' ')[1]))
    # print(frq_error_word)
    

    for i in tmp_corrections:
      if i[1][0]=='t':
        if i[1] in switch_error_dict:
          key=i[1]
          val=switch_error_dict[key]
          switch_error_dict[key]=val+frq_error_word
        else: 
          key = i[1]
          switch_error_dict[key]=frq_error_word

      elif i[1][0]=='d':
        if i[1] in delete_error_dict:
          key=i[1]
          val=delete_error_dict[key]
          delete_error_dict[key]=val+frq_error_word
        else: 
          key = i[1]
          delete_error_dict[key]=frq_error_word

      elif i[1][0]=='i':
        if i[1] in insert_error_dict:
          key=i[1]
          val=insert_error_dict[key]
          insert_error_dict[key]=val+frq_error_word
        else: 
          key = i[1]
          insert_error_dict[key]=frq_error_word

      elif i[1][0]=='s':
        if i[1] in replace_error_dict:
          key=i[1]
          val=replace_error_dict[key]
          replace_error_dict[key]=val+frq_error_word
        else: 
          key = i[1]
          replace_error_dict[key]=frq_error_word
   
  except:
    suggestion_faild.append(word)

# print(replace_error_dict)
# print(insert_error_dict)
# print(delete_error_dict)
# print(switch_error_dict)

delete_error_dict=(dict(sorted(delete_error_dict.items(), key=lambda item: item[1])))
insert_error_dict=(dict(sorted(insert_error_dict.items(), key=lambda item: item[1])))
replace_error_dict=(dict(sorted(replace_error_dict.items(), key=lambda item: item[1])))
switch_error_dict=(dict(sorted(switch_error_dict.items(), key=lambda item: item[1])))

with open('error_analyser.txt', 'w',encoding="utf-8") as f: 
    for key, value in delete_error_dict.items(): 
        f.write('%s %s\n' % (key, value))
    for key, value in insert_error_dict.items(): 
        f.write('%s %s\n' % (key, value))
    for key, value in replace_error_dict.items(): 
        f.write('%s %s\n' % (key, value))
    for key, value in switch_error_dict.items(): 
        f.write('%s %s\n' % (key, value))

# delete_word={}
# insert_word={}
# replace_word={}
# switch_word={}

# my_word = "ලමයා" 
# tmp_corrections = get_corrections(my_word, word_count_dict)
# print(tmp_corrections)

# for i in tmp_corrections:
#   if i[1][0]=='t':
#     key = i[1]
#     if i[1] in switch_word:
#       val=switch_word[key]
#       switch_word[key] = val+","+i[0]+"->"+i[2]
#     else:
#       switch_word[key] = i[0]+"->"+i[2]

#   elif i[1][0]=='d':
#     key = i[1]
#     if key in delete_word:
#       val=delete_word[key]
#       print(val)
#       delete_word[key] = val+","+i[2]+"->"+i[0]
#     else:
#       delete_word[key] = i[2]+"->"+i[0]

#   elif i[1][0]=='i':
#     key = i[1]
#     if key in insert_word:
#       val=insert_word[key]
#       insert_word[key] = val+","+i[2]+"->"+i[0]
#     else:
#       insert_word[key] = i[2]+"->"+i[0]

#   elif i[1][0]=='s':
#     key = i[1]
#     if key in replace_word:
#       val=replace_word[key]
#       replace_word[key] = val+","+i[2]+"->"+i[0]
#     else:
#       replace_word[key] = i[2]+"->"+i[0]


# print(replace_word)
# print(insert_word)
# print(delete_word)
# print(switch_word)

# error_word = process_data(r'Data_Procssing/text_data/error_words.txt')
# error_word= error_word.splitlines( )
# for word in error_word: 
#   try:
#     my_word = word.split(' ')[0]
#     tmp_corrections = get_corrections(my_word, word_count_dict)

#     for i in tmp_corrections:
#       if i[1][0]=='t':
#         key = i[1]
#         if i[1] in switch_word:
#           val=switch_word[key]
#           switch_word[key] = val+","+i[0]+"->"+i[2]
#         else:
#           switch_word[key] = i[0]+"->"+i[2]

#       elif i[1][0]=='d':
#         key = i[1]
#         if key in delete_word:
#           val=delete_word[key]
#           delete_word[key] = val+","+i[0]+"->"+i[2]
#         else:
#           delete_word[key] = i[0]+"->"+i[2]

#       elif i[1][0]=='i':
#         key = i[1]
#         if key in insert_word:
#           val=insert_word[key]
#           insert_word[key] = val+","+i[0]+"->"+i[2]
#         else:
#           insert_word[key] = i[0]+"->"+i[2]

#       elif i[1][0]=='s':
#         key = i[1]
#         if key in replace_word:
#           val=replace_word[key]
#           replace_word[key] = val+","+i[0]+"->"+i[2]
#         else:
#           replace_word[key] = i[0]+"->"+i[2]

#   except:
#     print("error")

# # print(replace_word)
# # print(insert_word)
# # print(delete_word)
# # print(switch_word)

# with open('error_analyser_word.txt', 'w',encoding="utf-8") as f: 
#     for key, value in delete_word.items(): 
#         f.write('%s %s\n' % (key, value))
#     for key, value in insert_word.items(): 
#         f.write('%s %s\n' % (key, value))
#     for key, value in replace_word.items(): 
#         f.write('%s %s\n' % (key, value))
#     for key, value in switch_word.items(): 
#         f.write('%s %s\n' % (key, value))
