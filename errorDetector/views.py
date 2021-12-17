from django.shortcuts import render, HttpResponse
from errorCorrector.views import Suggestions

from errorDetector.spylls.examples.basic import detector_fun
import json

# Create your views here.
# def Error(request):
#     return HttpResponse("It is error detector")
def formatSuggestions(suggestions, word):
    #print("sugg", suggestions)
    #print("hiii", suggestions.keys())
    #suggestList = suggestions.keys()
    #print("list", suggestList)
    result = {
        "word" : word,
        "suggestions" : suggestions
    }
    return result


def Detector(request):
    
    #print(request.GET['word'])
    #body_unicode = request.body.decode('utf-8')
    #print(body_unicode)
    #body = json.loads(body_unicode)
    #print(body)
    word = str(request.GET['word'])
    incorrect_word_list=detector_fun(word)

    #print(incorrect_word_list)
    if incorrect_word_list == []:
        response_data = {"word" : word,
                        "suggestions" : [
                                         
                                        ]
                        }
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        suggestions=Suggestions(incorrect_word_list)
        response_data = formatSuggestions(suggestions,word)
        #print("cha", response_data)
        return HttpResponse(json.dumps(response_data), content_type="application/json")