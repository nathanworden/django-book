from django.http import HttpResponse

def hello(request):
  return HttpResponse("You gotta believe this is where we say hello world")
