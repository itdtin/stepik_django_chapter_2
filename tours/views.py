import random

from django.views import View
from django.http import Http404
from django.shortcuts import render

from .tours_data import tours, departures, title, description, subtitle


class MainView(View):
    """Класс представления для главной"""

    def get(self, request, *args, **kwargs):
        tourss = {}
        while len(tourss) != 6:
            item = random.randint(1, len(list(tours.keys())))
            if item not in tourss:
                tourss.update({item: tours[item]})
        return render(
            request, 'tours/index.html', context={
                'title': title, 'subtitle': subtitle,
                'description': description, 'tours': tourss,
                'departures': departures}
        )


class DepartureView(View):
    """Класс представления для направлений"""

    def get(self, request, departure_name):

        if departure_name not in departures:
            raise Http404
        turs = [tour for tour in tours if tours[tour]['departure'] == departure_name]
        prices = [tours[tour]['price'] for tour in turs]
        nights = [tours[tour]['nights'] for tour in turs]

        return render(
            request, 'tours/departure.html', context={
                'title': title,
                'subtitle': subtitle,
                'description': description,
                'departure': departures[departure_name],
                'active': departure_name,
                'departures': departures,
                'tours': tours,
                'turs': turs,
                'price_min': min(prices),
                'price_max': max(prices),
                'nights_min': min(nights),
                'nights_max': max(nights)
            }
        )


class TourView(View):
    """Класс представления для каждого тура"""

    def get(self, request, id):

        id = int(id)
        if id not in tours:
            raise Http404

        return render(request, 'tours/tour.html', context={'tour': tours[id],
                                                           'departure': departures[tours[id]['departure']],
                                                           'active': tours[id]['departure'],
                                                           'id': id, 'departures': departures})
