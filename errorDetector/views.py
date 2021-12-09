from django.shortcuts import render, HttpResponse
from errorCorrector.views import Suggestions

from errorDetector.spylls.examples.basic import detector_fun

# Create your views here.
# def Error(request):
#     return HttpResponse("It is error detector")

def Detector(request):
    incorrect_word_list=detector_fun("ප්‍රබල")
    print(incorrect_word_list)
    if incorrect_word_list == []:
        return HttpResponse("word is correct")
    else:
        suggestions=Suggestions(incorrect_word_list)

        return HttpResponse(suggestions)