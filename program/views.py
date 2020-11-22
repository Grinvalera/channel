from django.shortcuts import render

from .models import Channel


def channel(request):

    monday = Channel.objects.filter(day_program='Monday')
    tuesday = Channel.objects.filter(day_program='Tuesday')
    wednesday = Channel.objects.filter(day_program='Wednesday')
    thursday = Channel.objects.filter(day_program='Thursday')
    friday = Channel.objects.filter(day_program='Friday')
    saturday = Channel.objects.filter(day_program='Saturday')
    sunday = Channel.objects.filter(day_program='Sunday')

    context = {
        'monday': monday,
        'tuesday': tuesday,
        'wednesday': wednesday,
        'thursday': thursday,
        'friday': friday,
        'saturday': saturday,
        'sunday': sunday,
    }
    return render(request, 'channel3+3.html', context=context)

