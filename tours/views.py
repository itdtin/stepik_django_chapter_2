import random

from django.views import View
from django.http import Http404
from django.shortcuts import render

from .tours_data import tours, departures, title, description, subtitle


class MainView(View):
    """Класс представления для главной"""

    def get(self, request, *args, **kwargs):
        random_tours = {}
        tours_ids = random.sample(tours.keys(), 6)

        for tour_id in tours_ids:
            random_tours.update({tour_id: tours[tour_id]})
        return render(
            request, 'tours/index.html', context={
                'title': title, 'subtitle': subtitle,
                'description': description, 'tours': random_tours,
                'departures': departures}
        )


class DepartureView(View):
    """Класс представления для направлений"""

    def get(self, request, departure_name):

        if departure_name not in departures:
            raise Http404
        departure_tours = [tour for tour in tours if tours[tour]['departure'] == departure_name]
        prices = [tours[tour]['price'] for tour in departure_tours]
        nights = [tours[tour]['nights'] for tour in departure_tours]

        return render(
            request, 'tours/departure.html', context={
                'title': title,
                'subtitle': subtitle,
                'description': description,
                'departure': departures[departure_name],
                'departures': departures,
                'tours': tours,
                'turs': departure_tours,
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
                                                           'id': id, 'departures': departures})
