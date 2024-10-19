from django.shortcuts import render

# Create your views here.
def create_profile_page(request):


    return render(request, template_name='profile/profile-create.html',)


def profile_details_page(request):

    return render(request, template_name='profile/profile-details.html', )


def edit_profile_page(request):

    return render(request, 'profile/profile-edit.html', )


def delete_profile_page(request):


    return render(request, 'profile/profile-delete.html', )