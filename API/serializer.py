from rest_framework import serializers

class correction(object):
    def __init__(self, word, status, suggestions):
        #print(word)
        self.word = word
        self.status = status
        self.suggestions = suggestions
        
class CorrectorSerializer(serializers.Serializer):
    word = serializers.CharField()
    status = serializers.CharField()
    suggestions = serializers.JSONField()