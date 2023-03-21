from django.shortcuts import render
from django.http import HttpResponse
from chat_app.model import chatbot as cb
# Create your views here.
global sentences
global req
global lists
global professor_name

class Abc:
    def __init__(self):
        self.list = []
    
    
    def chatpage(self, request):
        
        
        sentences = ["ChatBot : 궁금한 교수님 성함을 입력해주세요"]
        self.list = sentences
        lists = self.list
        return render(request,
                    "chat/generator.html",
                    {"lists":lists}
        )
        
    def chatting(self, request):
        
        if request.method == "GET":
            sentence = request.GET["sentence"]
        elif request.method == "POST":
            sentence = request.POST["sentence"]
        req = sentence
        ct = cb.Load_chatbot()
        a = ct.non_answer(req)
        self.list.appned(a)
        lists = self.list
            
        return render(request,
                    "chat/generator.html",
                    {"lists":lists})
        
            
        
    
    
    
