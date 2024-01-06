# Heroes Of Code And Logic \/|||


def heroes_create(n: int) -> dict:
    heroes = {}
    for _ in range(n):
        hero = input().split()
        name = hero[0]
        health_point = int(hero[1])
        mana_point = int(hero[2])
        heroes[name] = [health_point, mana_point]
    return heroes


def cast_spell(heroes: dict, instructions: list) -> dict:
    name = instructions[1]
    mana_needed = int(instructions[2])
    spell_name = instructions[3]
    if mana_needed > heroes[name][1]:
        print(f"{name} does not have enough MP to cast {spell_name}!")
    else:
        heroes[name][1] -= mana_needed
        print(f"{name} has successfully cast {spell_name} and now has {heroes[name][1]} MP!")
    return heroes


def take_damage(heroes: dict, instructions: list) -> dict:
    hero_name = instructions[1]
    damage = int(instructions[2])
    attacker = instructions[3]

    if damage >= heroes[hero_name][0]:
        print(f"{hero_name} has been killed by {attacker}!")
        heroes.pop(hero_name)
    else:
        heroes[hero_name][0] -= damage
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
    return heroes


def recharging(heroes: dict, instructions: list) -> dict:
    hero_name = instructions[1]
    amount = int(instructions[2])
    if heroes[hero_name][1] + amount > 200:
        print(f"{hero_name} recharged for {200 - heroes[hero_name][1]} MP!")
        heroes[hero_name][1] = 200
    else:
        heroes[hero_name][1] += amount
        print(f"{hero_name} recharged for {amount} MP!")
    return heroes


def heal(heroes: dict, instructions: list) -> dict:
    hero_name = instructions[1]
    amount = int(instructions[2])
    if heroes[hero_name][0] + amount > 100:
        print(f"{hero_name} healed for {100 - heroes[hero_name][0]} HP!")
        heroes[hero_name][0] = 100
    else:
        heroes[hero_name][0] += amount
        print(f"{hero_name} healed for {amount} HP!")
    return heroes


def display_heroes(heroes: dict):
    for hero in heroes:
        # print(hero + "\n" + "  HP: " + str(heroes[hero][0]) + "\n" + "  MP: " + str(heroes[hero][1]))
        print(f"{hero}\n  HP: {heroes[hero][0]}\n  MP: {heroes[hero][1]}")


def call_functions():
    n = int(input())
    heroes = heroes_create(n)

    command = input()

    while command != "End":
        instructions = command.split(" - ")
        action = instructions[0]

        if action == "CastSpell":
            heroes = cast_spell(heroes, instructions)
        elif action == "TakeDamage":
            heroes = take_damage(heroes, instructions)
        elif action == "Recharge":
            heroes = recharging(heroes, instructions)
        elif action == "Heal":
            heroes = heal(heroes, instructions)

        command = input()
    display_heroes(heroes)


if __name__ == "__main__":
    call_functions()
