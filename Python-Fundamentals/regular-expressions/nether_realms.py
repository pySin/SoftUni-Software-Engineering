# Nether Realms
import re


def divide_demons(demons):
    demons = [x.strip() for x in demons.split(", ")]
    return demons


def demon_health(demon):
    pattern = r"[^0-9+=*\/\.-]"
    result = re.findall(pattern, demon)
    health = sum([ord(x) for x in result])
    return health


def demon_damage(demon):
    pattern = r"[-+]*\d+\.\d+|[-+]*\d+"
    result = re.findall(pattern, demon)
    damage = sum([float(x) for x in result])
    for symbol in demon:
        if symbol == "*":
            damage *= 2
        elif symbol == "/":
            damage /= 2
    return damage


def call_functions():

    demons = sorted(divide_demons(input()))
    for demon in demons:
        health = demon_health(demon)
        damage = demon_damage(demon)
        if health > 0:
            print(f"{demon} - {health} health, {damage:.2f} damage")


if __name__ == "__main__":
    call_functions()
