from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.order_by('-published_at')
    # for article in object_list:
    #     for scope in article.scopes.all:
    #         print(scope.tag.name)
    context = {'object_list': object_list}
    return render(request, template, context)