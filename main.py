import random


hp = 7
gold = 0
room = 1
while hp > 0 and gold < 10:
    print("\n" + "-" * 50)
    print(f"Room {room}")
    print(f"Health: {hp} | Gold: {gold}")
    print("You awaken on a cold altar in the Fallen Angels' Castle.")
    print("Before you stand three heavy iron doors: 1, 2, or 3.")
    door = input("Which door do you open? (1/2/3): ").strip()

    if door in ["1", "2", "3"]:
        event = random.choice(["gold", "thief", "heal", "damage", "nothing"])

        if event == "gold":
            found = random.randint(2, 5)
            gold += found
            print(f"Behind the door lies a chest with {found} gold coins!")
        elif event == "thief":
            stolen = min(random.randint(1, 2), gold)
            gold -= stolen
            print(f"An elusive shadow thief steals {stolen} gold!")
        elif event == "heal":
            healed = random.randint(1, 3)
            hp += healed
            print(f"You recover {healed} health!")
        elif event == "damage":
            damage = random.randint(2, 4)
            hp -= damage
            print(f"A trapped glyph explodes! You take {damage} damage.")
        else:
            print("An empty, dusty hallway. Nothing happens here.")
    else:
        print("You hesitate and stand still, choosing no door.")
    room += 1
