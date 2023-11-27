from django.shortcuts import render

# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def restaurants_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'restaurants/index.html', {
    'restaurants': restaurants
  })
