from django.shortcuts import render

def post_list(request):
    return render(request, 'danblog/post_list.html', {})
    