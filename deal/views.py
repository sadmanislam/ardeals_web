from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DealSerializer
from .models import Deal, Category, Area
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


# Lists all deals or create a new one
class DealList(APIView):

    def get(self, request):
        deals = Deal.objects.all()
        serializer = DealSerializer(deals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DealDetail(APIView):
    def get_object(self, pk):
        try:
            return Deal.objects.get(pk=pk)
        except Deal.objects.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = DealSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = DealSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@login_required
def index(request):
    all_deals = Deal.objects.all()
    context = {'all_deals': all_deals}
    return render(request, 'deal/index.html', context)


@login_required
def alldeals(request):
    all_deals = Deal.objects.all()
    context = {'all_deals': all_deals}
    return render(request, 'deal/deals.html', context)


@login_required
def apparels(request):
    category = Category.objects.filter(name="Apparels")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)


@login_required
def food(request):
    category = Category.objects.filter(name="Food")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)


@login_required
def accessories(request):
    category = Category.objects.filter(name="Accessories")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)


@login_required
def services(request):
    category = Category.objects.filter(name="Services")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)


@login_required
def electronics(request):
    category = Category.objects.filter(name="Electronics")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)


@login_required
def dailyessentials(request):
    category = Category.objects.filter(name="Daily Essentials")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)


@login_required
def bcity(request):
    category = Area.objects.filter(name="Bashundhara R/A")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)



@login_required
def tejgaon(request):
    category = Area.objects.filter(name="Tejgaon")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)

@login_required
def pd(request):
    category = Area.objects.filter(name="Puran Dhaka")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)


@login_required
def mirpur(request):
    category = Area.objects.filter(name="Mirpur")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)

@login_required
def dhanmondi(request):
    category = Area.objects.filter(name="Dhanmondi")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)

@login_required
def uttara(request):
    category = Area.objects.filter(name="Uttara")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)

@login_required
def lalmatia(request):
    category = Area.objects.filter(name="Lalmatia")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)


@login_required
def moghbazar(request):
    category = Area.objects.filter(name="Moghbazar")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)


@login_required
def banani(request):
    category = Area.objects.filter(name="Banani")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)



@login_required
def g1(request):
    category = Area.objects.filter(name="Gulshan-1")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)


@login_required
def g2(request):
    category = Area.objects.filter(name="Gulshan-2")
    all_deals = Deal.objects.all()
    context = {'category': category,
               'all_deals': all_deals}
    return render(request, 'deal/category.html', context)


@login_required
def detail(request, deal_id):
    deal = get_object_or_404(Deal, pk=deal_id)
    all_deals = Deal.objects.all()
    context = {'deal': deal,
               'all_deals': all_deals}
    return render(request, 'deal/detail.html', context)


def loginview(request):
    return HttpResponseRedirect('accounts/login')


@login_required
def userdeals(request):
    all_deals = Deal.objects.filter(user=request.user)
    context = {'all_deals': all_deals}
    return render(request, 'deal/userdeals.html', context)


class DealCreate(CreateView):
    model = Deal
    fields = ['publisher', 'user', 'description_small', 'description_long', 'main_attraction', 'type', 'genre',
              'contact', 'validity', 'category', 'address', 'area', 'longitude', 'latitude', 'thumbnail']


class DealUpdate(UpdateView):
    model = Deal
    fields = ['publisher', 'user', 'description_small', 'description_long', 'main_attraction', 'type', 'genre',
              'contact', 'validity', 'category', 'address', 'area', 'longitude', 'latitude', 'thumbnail']
    #template_name_suffix = '_update_form'


class DealDelete(DeleteView):
    model = Deal
    success_url = reverse_lazy('userdeals')

