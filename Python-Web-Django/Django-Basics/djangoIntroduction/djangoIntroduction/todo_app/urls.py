from django.urls import path
from djangoIntroduction.todo_app.views import my_view, add_view, delete_view, index

"""

STEP 1: Create a project
STEP 2: Create an app
STEP 3: Add the app to INSTALLED_APPS

# If postgres is needed
STEP 4: Replace DB settings with Postgres DB settings
STEP 5: Enter credentials
STEP 6: Install psycopg2
STEP 7: Create the database

"""

urlpatterns = [
    path('', my_view),
    path('add/', add_view),
    path('delete/', delete_view),
    path('tasks/', index)
]

