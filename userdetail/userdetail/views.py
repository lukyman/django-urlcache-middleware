from django.http import HttpResponse

def getFirstName():
    return HttpResponse("John")
    
def getLastName():
    return HttpResponse("Doe")

def getFullName():
    return HttpResponse("John Doe")