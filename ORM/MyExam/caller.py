import os
import django
from django.db.models import Q, Count, Sum, F, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Astronaut, Mission, Spacecraft


# Create queries within functions
def get_astronauts(search_string=None):
    if search_string is None:
        return ""

    query = Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)

    astronauts = Astronaut.objects.filter(query).order_by('name')

    if not astronauts:
        return ""

    return "\n".join(f"Astronaut: {x.name}, phone number: {x.phone_number}, status: {'Active' if x.is_active else 'Inactive'}"
                     for x in astronauts)


def get_top_astronaut():
    top_astronaut = Astronaut.objects.get_astronauts_by_missions_count().first()

    if not top_astronaut or top_astronaut.mission_number == 0:
        return "No data."

    return f"Top Astronaut: {top_astronaut.name} with {top_astronaut.mission_number} missions."


def get_top_commander():
    top_commander = Astronaut.objects.annotate(
        num_missions=Count('commander_mission')
    ).order_by(
        "-num_missions",
        "phone_number",
    ).first()

    if not top_commander or top_commander.num_missions == 0:
        return "No data."

    return f"Top Commander: {top_commander.name} with {top_commander.num_missions} commanded missions."


def get_last_completed_mission():
    mission = Mission.objects.select_related(
        'spacecraft',
        'commander'
    ).prefetch_related(
        'astronauts'
    ).filter(
        status='Completed'
    ).order_by('-launch_date').first()
    # mission = Mission.objects.filter(status='Completed').order_by('-launch_date').first()

    if not mission:
        return "No data."

    commander_name = "TBA" if mission.commander is None or mission.commander.name is None else mission.commander.name
    astronaut_names = ', '.join(x.name for x in mission.astronauts.all().order_by('name'))
    spacewalks = sum([r.spacewalks for r in mission.astronauts.all()])

    return f"The last completed mission is: {mission.name}. Commander: {commander_name}. Astronauts: {astronaut_names}. Spacecraft: {mission.spacecraft.name}. Total spacewalks: {spacewalks}."


def get_most_used_spacecraft():
    most_used_craft = Spacecraft.objects.annotate(
        mission_number=Count('mission')
    ).filter(
        mission_number__gt=0
    ).order_by(
        '-mission_number',
        'name'
    ).first()

    if not most_used_craft:
        return "No data."

    astronauts = Mission.objects.filter(spacecraft=most_used_craft).values('astronauts').distinct().count()

    return f"The most used spacecraft is: {most_used_craft.name}, manufactured by {most_used_craft.manufacturer}, used in {most_used_craft.mission_number} missions, astronauts on missions: {astronauts}."


def decrease_spacecrafts_weight():

    affected_spacecrafts = Spacecraft.objects.filter(
        mission__status='Planned',
        weight__gte=200.0
    ).distinct()

    num_spacecrafts = affected_spacecrafts.count()

    if num_spacecrafts == 0:
        return "No changes in weight."

    affected_spacecrafts.update(weight=F('weight') - 200.0)

    avg_weight = Spacecraft.objects.aggregate(
        avg_weight=Avg('weight')
    )['avg_weight'] or 0.0

    return f"The weight of {num_spacecrafts} spacecrafts has been decreased. The new average weight of all spacecrafts is {avg_weight}kg"
