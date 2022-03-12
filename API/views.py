from django.http import JsonResponse
from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from collections import Counter
import numpy as np
import pandas as pd
import io
from django.shortcuts import render, HttpResponse
from API.spylls.examples.basic import detector_fun
from .serializer import CorrectorSerializer
from .serializer import correction
from rest_framework.response import Response
import urllib.request


@api_view(['GET', 'POST'])
def listcorrection(request):
    if request.method == "GET":
        word = str(request.GET.get("words", False))
        correctionList = Detector(word)
        print(correctionList)
        obj_all = []
        for i in correctionList:
            obj = correction(word=i[0], status=i[1], suggestions=i[2])
            obj_all.append(obj)
        print(obj_all)
        serializer_class = CorrectorSerializer(obj_all, many=True)
        y = serializer_class.data
        return Response(y)


def formatSuggestions(suggestions, incorrect_word_list, correct_word_list, word_list):
    result_all = []
    for i in range(len(word_list)):
        if word_list[i] in correct_word_list:
            result = []
            result.append(word_list[i])
            result.append("correct")
            result.append([])
            result_all.append(result)
        else:
            result = []
            j = incorrect_word_list.index(word_list[i])
            result.append(word_list[i])
            if len(suggestions[j]) == 1:
                result.append("autocorrect")
                result.append(suggestions[j][0])

            else:
                result.append("incorrect")
                result.append(suggestions[j])
            result_all.append(result)

    return result_all


def Detector(word):
    incorrect_word_list, correct_word_list, word_list = detector_fun(word)

    if incorrect_word_list != []:
        suggestions = Suggestions(incorrect_word_list)
        response_data = formatSuggestions(
            suggestions, incorrect_word_list, correct_word_list, word_list)
    else:
        response_data = formatSuggestions(
            [], incorrect_word_list, correct_word_list, word_list)

    return (response_data)

# Need to change location


def process_data(file_name):
    read_data = open(file_name, encoding="utf-8").read()
    return read_data


def get_count(vocab):
    vocab = vocab.splitlines()
    word_count_dict = {}
    for i in range(1, len(vocab)):
        word = vocab[i].split(" ")
        if(vocab[i] == ''):
            continue
        key = word[0]
        try:
            value = int(word[1])
        except:
            print('Can not convert', str, "to int")

        word_count_dict[key] = value
    return word_count_dict


def get_error_count(type):
    type = type.splitlines()
    error_count_dict = {}
    for i in range(1, len(type)):
        word = type[i].split(" ")
        if(type[i] == ''):
            continue
        key = word[0]
        try:
            value = int(word[1])
        except:
            print('Can not convert', str, "to int")

        error_count_dict[key] = value
    return error_count_dict
##########


"""Insert letters"""


def insert_letter(word):

    delete_l = []
    split_l = []

    split_l = [(word[:i], word[i:]) for i in range(len(word))]
    for L, R in split_l:
        del_l = []
        del_l.append(L+R[1:])
        x = (R[0])
        del_l.append("ins("+x+")")
        delete_l.append(del_l)
    return delete_l


def get_corrections_insert(my_word, word_count_dict):

    suggestions = []
    n_best = []
    edit_one_letter = insert_letter(my_word)

    for word1 in edit_one_letter:

        if word1[0] in word_count_dict and word1 not in suggestions:
            del_error = []
            del_error.append(word1[0])
            del_error.append(word1[1])
            del_error.append(my_word)

            suggestions.append(del_error)

    return suggestions


"""Switch letters"""


def switch_letter(word):

    switch_l = []
    split_l = []

    split_l = [(word[:i], word[i:]) for i in range(len(word)+1)]
    for L, R in split_l:
        if (len(R) >= 2):
            swit_l = []
            swit_l.append(L+R[1]+R[0]+R[2:])
            swit_l.append("trans("+R[1]+","+R[0]+")")
            switch_l.append(swit_l)

    return switch_l


def get_corrections_switch(my_word, word_count_dict):

    suggestions = []
    n_best = []
    edit_one_letter = switch_letter(my_word)

    for word1 in edit_one_letter:
        if word1[0] in word_count_dict:
            switch_error = []
            switch_error.append(word1[0])
            switch_error.append(word1[1])
            switch_error.append(my_word)
            suggestions.append(switch_error)

    return suggestions


"""Replace letter"""


def replace_letter(word):

    letters = '්ාෘුැූෑිීෙේෛොෝෞෘෲෟෳංඃකගඛඝඞඟචඡජඣඤඥඦටඨඩඪණඬතථදධනඳපඵබභමඹයරලළව‍ශෂසෆක්‍ෂඅආඇඈඉඊඋඌාඑඒඓඔඕඖඍඎඏඐංඃ'
    replace_l = []
    split_l = []

    split_l = [(word[:i], word[i:]) for i in range(len(word))]

    for l in letters:
        for R, L in split_l:
            rep_l = []
            if len(L) > 1:
                rep_l.append(R+l+L[1:])
                rep_l.append("sub("+l+","+L[0]+")")
                replace_l.append(rep_l)
            else:
                rep_l.append(R+l)
                rep_l.append("sub("+l+","+L[0]+")")
                replace_l.append(rep_l)

    for i in replace_l:
        if i[0] == word:
            replace_l.remove(i)

    return replace_l


def get_corrections_replace(my_word, word_count_dict):

    suggestions = []
    n_best = []
    edit_one_letter = replace_letter(my_word)

    for word1 in edit_one_letter:
        if word1[0] in word_count_dict and word1 not in suggestions:
            replace_error = []
            replace_error.append(word1[0])
            replace_error.append(word1[1])
            replace_error.append(my_word)
            suggestions.append(replace_error)

    return suggestions


"""Delete letters"""


def delete_letter(word):

    letters = '්ාෘුැූෑිීෙේෛොෝෞෘෲෟෳංඃකගඛඝඞඟචඡජඣඤඥඦටඨඩඪණඬතථදධනඳපඵබභමඹයරලළව‍ශෂසෆක්‍ෂඅආඇඈඉඊඋඌාඑඒඓඔඕඖඍඎඏඐංඃ'
    insert_l = []
    split_l = []

    split_l = [(word[:i], word[i:]) for i in range(len(word)+1)]
    for c in letters:
        for R, L in split_l:
            ins_l = []
            ins_l.append(R+c+L)
            ins_l.append("del("+c+")")
            insert_l.append(ins_l)

    return insert_l


def get_corrections_delete(my_word, word_count_dict):

    suggestions = []
    n_best = []
    edit_one_letter = delete_letter(my_word)

    for word1 in edit_one_letter:
        if word1[0] in word_count_dict and word1 not in suggestions:
            insert_error = []
            insert_error.append(word1[0])
            insert_error.append(word1[1])
            insert_error.append(my_word)
            suggestions.append(insert_error)

    return suggestions


"""Edit one letter"""


def edit_one_letter(word, word_count_dict):

    edit_one_set = set()
    switch_word_l = get_corrections_switch(word, word_count_dict)
    delete_word_l = get_corrections_delete(word, word_count_dict)
    replace_word_l = get_corrections_replace(word, word_count_dict)
    insert_word_l = get_corrections_insert(word, word_count_dict)
    edit_one_set_list = switch_word_l+delete_word_l+replace_word_l+insert_word_l

    return edit_one_set_list


"""Get corrections"""


def get_corrections(my_word, word_count_dict, error_count_dict):
    suggestions = []
    n_best = []
    tmp_edit_one_set = edit_one_letter(my_word, word_count_dict)
    count_all = 0
    for words in tmp_edit_one_set:
        count = word_count_dict[words[0]]
        words.append(count)
        try:
            error_count = error_count_dict[words[1]]
        except:
            error_count = 1
        words.append(error_count)
        count_all = count_all+count*error_count
        n_best.append(words)
    n_best.append(count_all)
    return n_best


"""Ranking"""


def ranking(tmp_corrections):
    rank_dic = []
    count_all = tmp_corrections[-1]
    for i in range(len(tmp_corrections)-1):
        val = (tmp_corrections[i][3]*tmp_corrections[i][4]*100)/count_all

        val_list = [tmp_corrections[i][0], val]
        rank_dic.append(val_list)
    rank_dic.sort(key=lambda row: (row[-1]), reverse=True)
    rank_dic_suggestions = []
    for i in rank_dic:
        if i[1] >= 99:
            rank_dic_suggestions.append(i[0])
            break
        else:
            rank_dic_suggestions.append(i[0])
    return rank_dic_suggestions[:5]


def Suggestions(incorrect_word_list):
    vocab = process_data("API/data/correct_unique_words.txt")
    type = process_data("API/data/error_analyser.txt")
    word_count_dict = get_count(vocab)
    error_count_dict = get_count(type)
    all_suggetions = []
    for word in incorrect_word_list:
        my_word = word
        tmp_corrections = get_corrections(
            my_word, word_count_dict, error_count_dict)
        Suggestions = ranking(tmp_corrections)
        all_suggetions.append(Suggestions)

    return all_suggetions
