from django.http.response import HttpResponse
from django.views.generic import TemplateView

def helloworldfunction(request):
    returnedobject = HttpResponse('<h1>hello world</h1>')
    return returnedobject

class HelloWprldClass(TemplateView):
    template_name = 'hello.html'