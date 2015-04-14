from django.shortcuts import render


def map(request):
    context_dict = {'request': request}
    return render(request, 'conferences/map.html', context_dict)


def about(request):
    context_dict = {'request': request}
    return render(request, 'conferences/about.html', context_dict)


def all(request):
    context_dict = {'request': request}
    return render(request, 'conferences/all.html', context_dict)


def conference(request, conference_name_slug):
    context_dict = {'request': request}
    return render(request, 'conferences/conference.html', context_dict)


def feedback(request):
    context_dict = {'request': request}
    return render(request, 'conferences/feedback.html', context_dict)
