from django.shortcuts import render

def people_list(request):
    from .models import Person
    people = Person.objects.filter(is_published=True).order_by('position_order')
    return render(request, 'people/people_list.html', {'people': people})