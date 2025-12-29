from django.shortcuts import render

def awards_list(request):
    from .models import Award
    awards = Award.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'awards/awards_list.html', {'awards': awards})