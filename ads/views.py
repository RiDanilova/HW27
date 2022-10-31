import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Category, Ad


def root(request):
    return JsonResponse({"status": "ok"})


@method_decorator(csrf_exempt, name="dispatch")
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        result_method = []

        for category in categories:
            result_method.append({"id": category.id, "name": category.name})
        return JsonResponse(result_method, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        data = json.loads(request.body)
        new_category = Category.objects.create(name=data["name"])

        return JsonResponse({"id": new_category.id, "name": new_category.name},
                            safe=False, json_dumps_params={"ensure_ascii": False})


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({"id": category.id, "name": category.name},
                            safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class AdView(View):
    def get(self, request):
        all_ads = Ad.objects.all()
        result_method = []

        for ad in all_ads:
            result_method.append(
                {"id": ad.id,
                 "name": ad.name,
                 "author": ad.author,
                 "price": ad.price,
                 "description": ad.description,
                 "address": ad.address,
                 "is_published": ad.is_published
                 })

        return JsonResponse(result_method, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        data = json.loads(request.body)
        new_ad = Ad.objects.create(
            name=data["name"],
            author=data["author"],
            price=data["price"],
            description=data["description"],
            address=data["address"],
            is_published=data["is_published"]
        )

        return JsonResponse(
            {"id": new_ad.id,
             "name": new_ad.name,
             "author": new_ad.author,
             "price": new_ad.price,
             "description": new_ad.description,
             "address": new_ad.address,
             "is_published": new_ad.is_published
             },
            safe=False, json_dumps_params={"ensure_ascii": False}
        )


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse(
            {"id": ad.id,
             "name": ad.name,
             "author": ad.author,
             "price": ad.price,
             "description": ad.description,
             "address": ad.address,
             "is_published": ad.is_published
             },
            safe=False, json_dumps_params={"ensure_ascii": False}
        )