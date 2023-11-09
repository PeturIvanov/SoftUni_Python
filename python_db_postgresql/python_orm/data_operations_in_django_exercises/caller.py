import os
import django
from django.db.models import F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


# Exercise Pet
def create_pet(name: str, species: str):
    new_pet = Pet(
        name=name,
        species=species,
    )

    new_pet.save()

    return f'{new_pet.name} is a very cute {new_pet.species}!'


# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))

# Exercise Artifact
def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    new_artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )

    return f'The artifact {new_artifact.name} is {new_artifact.age} years old!'


def delete_all_artifacts():
    Artifact.objects.all().delete()


# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))

# print(create_artifact('Crystal Amulet', 'Mystic Forest', 300, 'A magical amulet believed to bring good fortune', True))

# delete_all_artifacts()


def show_all_locations():
    locations_ordered_by_id = []
    locations = Location.objects.all().order_by('-id')

    for location in locations:
        locations_ordered_by_id.append(
            f"{location.name} has a population of {location.population}!"
        )

    return '\n'.join(locations_ordered_by_id)


def new_capital():
    first_location = Location.objects.first()
    first_location.is_capital = True
    first_location.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location():
    Location.objects.first().delete()


# print(show_all_locations())
# print(new_capital())
# print(get_capitals())
# delete_first_location()


def apply_discount():
    cars = Car.objects.all()

    for car in cars:
        discount_percent = sum([int(n) for n in str(car.year)])
        car.price_with_discount = car.price * (100 - discount_percent) / 100

    Car.objects.bulk_update(cars, ['price_with_discount'])


def get_recent_cars():
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')


def delete_last_car():
    Car.objects.last().delete()


# apply_discount()
# delete_last_car()
# print(get_recent_cars())


def show_unfinished_tasks():
    incomplete_tasks = []

    for task in Task.objects.filter(is_finished=False):
        incomplete_tasks.append(f'Task - {task.title} needs to be done until {task.due_date}!')

    return '\n'.join(incomplete_tasks)


def complete_odd_tasks():
    tasks = Task.objects.all()

    for task in tasks:
        if task.id % 2 == 1:
            task.is_finished = True

    Task.objects.bulk_update(tasks, ['is_finished'])


def encode_and_replace(text: str, task_title: str):
    tasks = Task.objects.filter(title=task_title)
    encoded_text = ''.join([chr(ord(c) - 3) for c in text])

    for task in tasks:
        task.description = encoded_text

    Task.objects.bulk_update(tasks, ['description'])


# complete_odd_tasks()
# print(show_unfinished_tasks())
# encode_and_replace("Zdvk#wkh#glvkhv$", "Simple Task")


def get_deluxe_rooms():
    deluxe_rooms = HotelRoom.objects.filter(room_type='Deluxe')
    even_deluxe_rooms = []

    for room in deluxe_rooms:
        if room.id % 2 == 0:
            even_deluxe_rooms.append(
                f"Deluxe room with number {room.room_number}"
                f" costs {room.price_per_night}$ per night!"
            )

    return '\n'.join(even_deluxe_rooms)


def increase_room_capacity():
    rooms = HotelRoom.objects.all().order_by('id')

    previous_room_capacity = None

    for room in rooms:
        if not room.is_reserved:
            previous_room_capacity = room.capacity
            continue

        if previous_room_capacity:
            room.capacity += previous_room_capacity

        else:
            room.capacity += room.id

        previous_room_capacity = room.capacity

        room.save()


def reserve_first_room():
    first_room = HotelRoom.objects.first()

    if first_room:
        first_room.is_reserved = True
        first_room.save()


def delete_last_room():
    last_room = HotelRoom.objects.last()

    if last_room:
        if last_room.is_reserved:
            last_room.delete()


# print(get_deluxe_rooms())
# reserve_first_room()
# print(HotelRoom.objects.get(room_number=101).is_reserved)


def update_characters():
    Character.objects.filter(class_name='Mage').update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7
    )

    Character.objects.filter(class_name='Warrior').update(
        hit_points=F('hit_points') / 2,
        dexterity=F('dexterity') + 4
    )

    Character.objects.filter(class_name__in=['Scout', 'Assassin']).update(
        inventory='The inventory is empty'
    )


def fuse_characters(first_character: Character, second_character: Character):
    name = f'{first_character.name} {second_character.name}'
    class_name = 'Fusion'
    level = (first_character.level + second_character.level) // 2
    strength = (first_character.strength + second_character.strength) * 1.2
    dexterity = (first_character.dexterity + second_character.dexterity) * 1.4
    intelligence = (first_character.intelligence + second_character.intelligence) * 1.5
    hit_points = (first_character.hit_points + second_character.hit_points)

    if first_character.class_name in ['Mage', 'Scout']:
        inventory = 'Bow of the Elven Lords, Amulet of Eternal Wisdom'

    else:
        inventory = 'Dragon Scale Armor, Excalibur'

    Character.objects.create(
        name=name,
        class_name=class_name,
        level=level,
        strength=strength,
        dexterity=dexterity,
        intelligence=intelligence,
        hit_points=hit_points,
        inventory=inventory,
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity():
    Character.objects.all().update(dexterity=30)


def grand_intelligence():
    Character.objects.all().update(intelligence=40)


def grand_strength():
    Character.objects.all().update(strength=50)


def delete_characters():
    Character.objects.filter(inventory='The inventory is empty').delete()


# character1 = Character.objects.create(
#     name="Gandalf",
#     class_name="Mage",
#     level=10,
#     strength=15,
#     dexterity=20,
#     intelligence=25,
#     hit_points=100,
#     inventory="Staff of Magic, Spellbook",
# )
#
# character2 = Character.objects.create(
#     name="Hector",
#     class_name="Warrior",
#     level=12,
#     strength=30,
#     dexterity=15,
#     intelligence=10,
#     hit_points=150,
#     inventory="Sword of Troy, Shield of Protection",
# )
#
# fuse_characters(character1, character2)
# fusion = Character.objects.filter(class_name='Fusion').get()
#
# print(fusion.name)
# print(fusion.class_name)
# print(fusion.level)
# print(fusion.intelligence)
# print(fusion.inventory)
