import random

MAX_HP = 7
hp = MAX_HP
nimbs = 0
room = 1
last_event = ""
last_action = ""
previous_scene = None

room_scenes = [
    ("A vast, gloomy hall is lined with statues of fallen angels.", 3),
    ("A long corridor splits into several shadowy branches.", 3),
    ("You reach a crossroads between the castle's towering halls.", 4),
    ("A frightening chamber is crowded with old wooden doors.", 5),
    ("Mirrors cover the walls, reflecting four mysterious doors.", 4),
    ("A narrow stone passage ends at two iron doors.", 2),
    ("Moonlight spills into a circular room with three exits.", 3),
    ("Broken angel statues guard a pair of ancient doors.", 2),
    ("A grand staircase rises between four archways.", 4),
    ("You enter a dusty library with five hidden passages.", 5),
    ("A flooded chamber has two dry doorways above the water.", 2),
    ("Black candles illuminate three doors in the darkness.", 3),
    ("A ruined ballroom opens into four silent corridors.", 4),
    ("You find a cell block with five heavy iron gates.", 5),
    ("A low tunnel forks toward two distant lights.", 2),
    ("A room of cracked mirrors hides three real doors.", 3),
    ("A narrow bridge leads to four doorways in the castle wall.", 4),
    ("An empty chapel has two doors beneath its shattered altar.", 2),
    ("A spiral gallery winds past five dark entrances.", 5),
    ("A stone chamber echoes around three carved doorways.", 3),
    ("You enter a cold vault with four sealed doors.", 4),
    ("A crooked hallway offers two paths through the gloom.", 2),
]

while hp > 0 and nimbs < 25:
    print("\n" + "-" * 50)
    
    # Итог прошлого действия выводим ДО информации о новой комнате
    if last_event:
        print(f"\n\033[1;93m{'!' * 50}\n{last_event.upper()}\n{'!' * 50}\033[0m")
        last_event = ""

    print(f"Room {room}")
    print(f"Health: {hp} | Nimbs: {nimbs}")

    scene, door_count = random.choice(
        [option for option in room_scenes if option[0] != previous_scene]
    )
    previous_scene = scene

    if room == 1:
        print("You awaken on a cold altar in the Fallen Angels' Castle.")
        print("Collect 25 nimbs to escape this place.")

    print(f"\033[1m{scene}\033[0m")

    door_choices = [str(number) for number in range(1, door_count + 1)]
    while True:
        door = input(
            f"Choose a door ({'/'.join(door_choices)}) or rest: "
        ).strip().lower()
        if door == "rest" and last_action == "rest":
            print("You must open a door before resting again.")
        elif door != "rest" and door not in door_choices:
            print("That door is not available in this room.")
        else:
            break

    if door == "rest":
        if hp >= MAX_HP:
            last_event = "You are already at full health."
        else:
            healed = min(3, MAX_HP - hp)
            hp += healed
            last_event = f"You rested and recovered {healed} health. No nimbs found."
    else:
        event = random.choice(["nimbs", "thief", "heal", "damage", "nothing"])

        if event == "nimbs":
            found = random.randint(1, 5)
            nimbs += found
            last_event = f"Behind the door lies a chest with {found} nimbs!"
        elif event == "thief":
            if nimbs == 0:
                last_event = "A shadow thief tries to rob you, but finds your pockets completely empty!"
            else:
                stolen = min(random.randint(1, 10), nimbs)
                nimbs -= stolen
                last_event = f"An elusive shadow thief steals {stolen} nimbs!"
        elif event == "heal":
            if hp >= MAX_HP:
                last_event = "You are already at full health."
            else:
                healed = min(random.randint(1, 2), MAX_HP - hp)
                hp += healed
                last_event = f"You recover {healed} health!"
        elif event == "damage":
            damage = random.randint(1, 5)
            hp -= damage
            last_event = f"A trapped glyph explodes! You take {damage} damage."
        else:
            last_event = "An empty, dusty hallway. Nothing happens here."

    last_action = door
    room += 1

if last_event:
    print(f"\n\033[1;93m{'!' * 50}\n{last_event.upper()}\n{'!' * 50}\033[0m")

print("\n" + "=" * 50)
if nimbs >= 25:
    print("\033[1mWith 25 nimbs, you escape the castle!\033[0m")
else:
    print("\033[1mYou have fallen in the castle. Game over.\033[0m")
print("=" * 50)