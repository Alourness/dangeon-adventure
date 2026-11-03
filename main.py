hp = 7
gold = 0
print("You awaken on a cold altar in the Fallen Angels' Castle.")
print("Twisted whispers echo as you see two corridors: left and right.")
door = input("Which door? (left/right) ").lower().strip()
if door == "left":
 print("A shadow demon strikes from the dark!")
 hp = hp - 2
elif door == "right":
 print("You find a glowing chest filled with obsidian coins!")
 gold = gold + 3
else:
 print("The abyssal silence freezes your blood. Nothing happens.")
print(f"Health: {hp} | Gold: {gold}")
