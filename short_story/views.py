from django.shortcuts import render


def short_story_list_view(request):
    return render(request, 'short_story/shortstory_list.html')
