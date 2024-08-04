import os
from typing import List

import django

# Set up Django
from django.db.models import Case, When, Value

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from helper import populate_model_with_data
from main_app.models import ArtworkGallery, Laptop, ChessPlayer, Meal, Dungeon, Workout
from main_app.choices import OperationSystemChoice, MealTypeChoice, WorkoutTypeChoice, DungeonDifficultyChoice


# populate_model_with_data(Laptop)
def show_highest_rated_art() -> str:
    best_artwork = ArtworkGallery.objects.order_by('-rating', 'id').first()

    return f"{best_artwork.art_name} is the highest-rated art with a {best_artwork.rating} rating!"


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery) -> None:
    ArtworkGallery.objects.bulk_create([
        first_art,
        second_art,
    ])


def delete_negative_rated_arts() -> None:
    ArtworkGallery.objects.filter(rating__lt=0).delete()
    # DELETE FROM artwork WHERE rating < 0


def show_the_most_expensive_laptop() -> str:
    most_expensive_laptop = Laptop.objects.order_by('-price', '-id').first()

    return f"{most_expensive_laptop.brand} is the most expensive laptop available for {most_expensive_laptop.price}$!"


def bulk_create_laptops(args: List[Laptop]) -> None:
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage() -> None:
    """
    UPDATE laptop
    SET storage = 512
    WHERE brand in (Asus, Lenovo)
    """

    Laptop.objects.filter(brand__in=("Asus", "Lenovo")).update(storage=512)


def update_to_16_GB_memory() -> None:
    Laptop.objects.filter(brand__in=("Apple", "Dell", "Acer")).update(memory=16)


def update_operation_systems() -> None:
    # Solution 1
    Laptop.objects.update(
        operation_system=Case(
            When(brand="Asus", then=Value(OperationSystemChoice.WINDOWS)),
            When(brand="Apple", then=Value(OperationSystemChoice.MACOS)),
            When(brand__in=("Dell", "Acer"), then=Value(OperationSystemChoice.LINUX)),
            When(brand="Lenovo", then=Value(OperationSystemChoice.CHROME_OS))
        )
    )

    # Solution 2
    # Laptop.objects.filter(brand="Asus").update(operation_system=OperationSystemChoice.WINDOWS)
    # Laptop.objects.filter(brand="Apple").update(operation_system=OperationSystemChoice.MACOS)
    # Laptop.objects.filter(brand__in=("Dell", "Acer")).update(operation_system=OperationSystemChoice.LINUX)
    # Laptop.objects.filter(brand="Lenovo").update(operation_system=OperationSystemChoice.CHROME_OS)


def delete_inexpensive_laptops() -> None:
    Laptop.objects.filter(price__lt=1200).delete()


def bulk_create_chess_players(args: List[ChessPlayer]):
    ChessPlayer.objects.bulk_create(args)


def delete_chess_players():
    ChessPlayer.objects.filter(title="no title").delete()


def change_chess_games_won():
    ChessPlayer.objects.filter(title="GM").update(games_won=30)


def change_chess_games_lost():
    ChessPlayer.objects.filter(title="no title").update(games_lost=25)


def change_chess_games_drawn():
    ChessPlayer.objects.update(games_drawn=10)


def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title='GM')


def grand_chess_title_IM():
    ChessPlayer.objects.filter(rating__in=(2399, 2300)).update(title='IM')


def grand_chess_title_FM():
    ChessPlayer.objects.filter(rating__in=(2299, 2200)).update(title="FM")


def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating__in=(2199, 0)).update(title="regular player")


def set_new_chefs():
    Meal.objects.update(chef=Case(
        When(meal_type=MealTypeChoice.BREAKFAST, then=Value("Gordon Ramsay")),
        When(meal_type=MealTypeChoice.LUNCH, then=Value("Julia Child")),
        When(meal_type=MealTypeChoice.DINNER, then=Value("Jamie Oliver")),
        When(meal_type=MealTypeChoice.SNACK, then=Value("Thomas Keller"))
    ))


def set_new_preparation_times():
    Meal.objects.update(preparation_time=Case(
        When(meal_type=MealTypeChoice.BREAKFAST, then=Value("10 minutes")),
        When(meal_type=MealTypeChoice.LUNCH, then=Value("12 minutes")),
        When(meal_type=MealTypeChoice.DINNER, then=Value("15 minutes")),
        When(meal_type=MealTypeChoice.SNACK, then=Value("5 minutes"))
    ))


def update_low_calorie_meals():
    Meal.objects.filter(meal_type__in=(MealTypeChoice.BREAKFAST, MealTypeChoice.DINNER)).update(calories=400)


def update_high_calorie_meals():
    Meal.objects.filter(meal_type__in=(MealTypeChoice.LUNCH, MealTypeChoice.SNACK)).update(calories=700)


def delete_lunch_and_snack_meals():
    Meal.objects.filter(meal_type__in=(MealTypeChoice.LUNCH, MealTypeChoice.SNACK)).delete()

#DUngeons


def show_hard_dungeons():
    hard_dungeon = Dungeon.objects.filter(difficulty=DungeonDifficultyChoice.HARD).order_by("-location")

    return '\n'.join(str(x) for x in hard_dungeon)


def bulk_create_dungeons(args: List[Dungeon]) -> None:
    Dungeon.objects.bulk_create(args)


def update_dungeon_names():
    Dungeon.objects.update(name=Case(
        When(difficulty=DungeonDifficultyChoice.EASY, then=Value("The Erased Thombs")),
        When(difficulty=DungeonDifficultyChoice.MEDIUM, then=Value("The Coral Labyrinth")),
        When(difficulty=DungeonDifficultyChoice.HARD, then=Value("The Lost Haunt"))
    ))


def update_dungeon_bosses_health():
    Dungeon.objects.exclude(difficulty=DungeonDifficultyChoice.EASY).update(boss_health=500)


def update_dungeon_recommended_levels():
    Dungeon.objects.update(recommended_level=Case(
        When(difficulty=DungeonDifficultyChoice.EASY, then=Value(25)),
        When(difficulty=DungeonDifficultyChoice.MEDIUM, then=Value(50)),
        When(difficulty=DungeonDifficultyChoice.HARD, then=Value(75))
    ))


def update_dungeon_rewards() -> None:
    Dungeon.objects.filter(
        boss_health=500
    ).update(reward="1000 Gold")

    Dungeon.objects.filter(
        location__startswith="E"
    ).update(reward="New dungeon unlocked")
    # UPDATE dungeon
    # SET reward = "New dungeon unlocked"
    # WHERE location LIKE "E%"

    Dungeon.objects.filter(
        location__endswith="s"
    ).update(reward="Dragonheart Amulet")
    # UPDATE dungeon
    # SET reward = "New dungeon unlocked"
    # WHERE location LIKE "%s"


def set_new_locations():
    Dungeon.objects.filter(recommended_level=25).update(location="Enchanted Maze")
    Dungeon.objects.filter(recommended_level=50).update(location="Grimstone Mines")
    Dungeon.objects.filter(recommended_level=75).update(location="Shadowed Abyss")


#EX.6

def show_workouts():
    workouts = Workout.objects.filter(workout_type__in=("Calisthenics", "CrossFit"))

    return "\n".join(str(x) for x in workouts)


def get_high_difficulty_cardio_workouts():
    cardio_workouts = Workout.objects.filter(workout_type=WorkoutTypeChoice.CARDIO, difficulty="High").order_by('instructor')

    return cardio_workouts


def set_new_instructors():
    Workout.objects.update(instructor=Case(
        When(workout_type=WorkoutTypeChoice.CARDIO, then=Value("John Smith")),
        When(workout_type=WorkoutTypeChoice.STRENGTH, then=Value("Michael Williams")),
        When(workout_type=WorkoutTypeChoice.YOGA, then=Value("Emily Johnson")),
        When(workout_type=WorkoutTypeChoice.CROSSFIT, then=Value("Sarah Davis")),
        When(workout_type=WorkoutTypeChoice.CALISTHENICS, then=Value("Chris Heria"))
    ))


def set_new_duration_times():
    Workout.objects.update(duration=Case(
        When(instructor="John Smith", then=Value("15 minutes")),
        When(instructor="Sarah Davis", then=Value("30 minutes")),
        When(instructor="Chris Heria", then=Value("45 minutes")),
        When(instructor="Michael Williams", then=Value("1 hour")),
        When(instructor="Emily Johnson", then=Value("1 hour and 30 minutes"))
    ))


def delete_workouts():
    Workout.objects.exclude(workout_type__in=(WorkoutTypeChoice.STRENGTH, WorkoutTypeChoice.CALISTHENICS)).delete()

