import random

def attack_roll(attackers, defenders):
    # Ensure there are at least 1 attacker and 1 defender
    if attackers < 1 or defenders < 1:
        return "Invalid number of armies"

    # Determine the number of dice each side rolls
    attacker_dice = min(3, attackers)
    defender_dice = min(3, defenders)

    # Roll the dice
    attacker_rolls = sorted([random.randint(1, 6) for _ in range(attacker_dice)], reverse=True)
    defender_rolls = sorted([random.randint(1, 6) for _ in range(defender_dice)], reverse=True)

    print(f"Attacker rolls: {attacker_rolls}")
    print(f"Defender rolls: {defender_rolls}")

    # Compare the dice rolls
    for a, d in zip(attacker_rolls, defender_rolls):
        if a > d:
            defenders -= 1
        else:
            attackers -= 1

    print(f"Result: Attackers: {attackers}, Defenders: {defenders}")
    return attackers, defenders






