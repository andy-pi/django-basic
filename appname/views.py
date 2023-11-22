from django.shortcuts import render

# Create your views here.
def home(request):
    user = request.user.username # Get the user from the request variable 
    return render(request, 'home.html', {'user': user,}) # pass the user variable to the template to render