from django.shortcuts import render


def post_list(request):
    return render(request, 'my_blog/post_list.html', {})

