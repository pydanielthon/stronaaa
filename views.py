from django.shortcuts import render
from django.shortcuts import get_object_or_404
from en_blog.models import Post, Category
import random

def home(request):
    #get newsleter footer
    #more
    return render(request, 'en_realization/list-realization.html', {})

def realization(request, slug):
    best_news = Post.objects.all().order_by('order_number_home_page')[:5]
    #more
    object = get_object_or_404(Realization, slug=slug)
    try:
        random_objects = random.sample(list(Realization.objects.exclude(id=object.id)), 3)
    except:
        random_objects = None
    context = {'best_news': best_news,
               'object': object,
               'random_objects': random_objects}
    return render(request, 'en_realization/single-realization.html', context)