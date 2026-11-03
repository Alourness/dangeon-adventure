import random


hp = 7
nimbs = 0
room = 1
last_event = ""
while hp > 0 and nimbs < 25:
    print("\n" + "-" * 50)
    print(f"Room {room}")
    print(f"Health: {hp} | Nimbs: {nimbs}")
    if room == 1:
        print("You awaken on a cold altar in the Fallen Angels' Castle.")
        print("Collect 25 nimbs to escape this place.")
    else:
        print("You enter the next room of the castle.")
    if last_event:
        print(last_event)
        last_event = ""
    print("Before you stand three heavy iron doors: 1, 2, or 3.")
    door = input("Choose a door (1/2/3) or rest: ").strip().lower()

    if door == "rest":
        healed = min(3, 7 - hp)
        hp += healed
        last_event = f"You rested and recovered {healed} health. No nimbs found."
    elif door in ["1", "2", "3"]:
        event = random.choice(["nimbs", "thief", "heal", "damage", "nothing"])

        if event == "nimbs":
            found = random.randint(1, 5)
            nimbs += found
            last_event = f"Behind the door lies a chest with {found} nimbs!"
        elif event == "thief":
            stolen = min(random.randint(1, 2), nimbs)
            nimbs -= stolen
            last_event = f"An elusive shadow thief steals {stolen} nimbs!"
        elif event == "heal":
            healed = min(random.randint(1, 2), 7 - hp)
            hp += healed
            last_event = f"You recover {healed} health!"
        elif event == "damage":
            damage = random.randint(1, 3)
            hp -= damage
            last_event = f"A trapped glyph explodes! You take {damage} damage."
        else:
            last_event = "An empty, dusty hallway. Nothing happens here."
    else:
        last_event = "You hesitate and stand still, choosing no door."
    room += 1

if last_event:
    print(last_event)
print("\n" + "=" * 50)
if nimbs >= 25:
    print("\033[1mWith 25 nimbs, you escape the castle!\033[0m")
else:
    print("\033[1mYou have fallen in the castle. Game over.\033[0m")
print("=" * 50)
