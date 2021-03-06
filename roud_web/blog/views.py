from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from blog.models import Article



def test(request):
    return render(request, 'blog/test.html')

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})


def lire(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/lire.html', {'article':article})
