from django.shortcuts import render
from django.shortcuts import render

def index(request):
        context_return = {
            'course_name' : 'Python e Django na Prática',
            'vehicle_entries' : [
                {
                    'name' : 'Gol',
                    'plate': 'ABC-1234'
                },
                {
                    'name' : 'Uno',
                    'plate': 'ABC-1234'
                },
                {
                    'name' : 'Fusca',
                    'plate': 'ABC-1234'
                },
                {
                    'name' : 'Camaro',
                    'plate': 'ABC-1234'
                }
            ]
        }
        return render(request, "hello.html", context_return)
