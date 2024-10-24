from tatsyRecipes.profile_app.models import Profile


def get_user():
    return Profile.objects.first()