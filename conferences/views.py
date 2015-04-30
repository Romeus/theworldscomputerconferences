from django.shortcuts import render
from conferences.forms import FeedbackForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from conferences.models import ConferenceType, Conference
from conferences.serializers import ConferenceTypeSerializer


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


def feedback(request):
    context_dict = {'request': request}
    if request.POST:
        form = FeedbackForm(request.POST)
        context_dict['form'] = form
        if form.is_valid():
            form.save()
            return render(request, 'conferences/thankyou.html', context_dict)
    else:
        form = FeedbackForm()
        context_dict['form'] = form
    return render(request, 'conferences/feedback.html', context_dict)


@api_view(['GET'])
def rest_conferences_collection(request):
    if request.method == 'GET':
        conferences = ConferenceType.objects.all()
        serializer = ConferenceTypeSerializer(conferences, many=True)
        return Response(serializer.data)
