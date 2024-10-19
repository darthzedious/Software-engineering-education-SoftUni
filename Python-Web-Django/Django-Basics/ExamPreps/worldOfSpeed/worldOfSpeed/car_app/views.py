from django.shortcuts import render

# Create your views here.

def catalogue_page(request):

    return render(request, template_name='car/catalogue.html', )


def create_car_page(request):
    return render(request, template_name='car/car-create.html', )


def car_details_page(request, pk):
    return render(request, template_name='car/car-details.html', )


def edit_car_page(request, pk):
    return render(request, 'car/car-edit.html', )


def delete_car_page(request, pk):
    return render(request, 'car/car-delete.html')
