from django.shortcuts import render

def post_list(requeste):
    return render(requeste, 'blog/post_list.html', {})
