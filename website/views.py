from django.shortcuts import render

def index_view(request):
    contex={'change':'Aryan Fartash', 'comment_person':'Kiana Faramehr', 'the_comment':'man shoharam ro aziat mikonam va asabe oon  khorde'}
    return render(request,'index.html',contex)
