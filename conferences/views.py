from django.shortcuts import render


def map(request):
    context_dict = {'request': request}
    return render(request, 'conferences/map.html', context_dict)


def about(request):
    context_dict = {'request': request}
    return render(request, 'conferences/about.html', context_dict)


def conferences_all(request):
    context_dict = {'request': request}
    return render(request, 'conferences/conferences.html', context_dict)

def conference_particular(request, conference_slug=None):
    context_dict = {'request': request, 'conference_slug': conference_slug}
    return render(request, 'conferences/conference.html', context_dict)

def conference_history(request, conference_slug=None):
    context_dict = {'request': request, 'conference_slug': conference_slug}
    return render(request, 'conferences/conference_history.html', context_dict)


def feedback(request):
    context_dict = {'request': request}
    return render(request, 'conferences/feedback.html', context_dict)
