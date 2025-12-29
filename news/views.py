from django.shortcuts import render, get_object_or_404

def news_detail(request, slug):
    from .models import NewsPage
    page = get_object_or_404(NewsPage.objects.live(), slug=slug)
    return render(request, 'news/news_page.html', {'page': page})