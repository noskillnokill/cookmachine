import random

def Calulate_Damage_Instance(postmitigationDamage, effective_armor, dummy_health, damage_dealt, AA_Damage):
        postmitigationDamage /= (1 + (effective_armor / 100))

        dummy_health -= postmitigationDamage
        damage_dealt += postmitigationDamage
        AA_Damage += postmitigationDamage
        postmitigationDamage = 0

        return dummy_health, damage_dealt, postmitigationDamage, AA_Damage

def critcheck(modified_stats, crit_adjusting):

    # if modified_stats["Crit Chance"] > 0:
    #     postmitigationDamage = modified_stats["Attack Damage"] * (((modified_stats["Crit Multiplier"] - 1) * (modified_stats["Crit Chance"]) / 100) + 1)


    if modified_stats["Crit Chance"] > 0 and modified_stats["Crit Chance"] < 100:
            didcrit = random.randint(1, 100) <= modified_stats["Crit Chance"] + crit_adjusting
            crit_adjusting = 0
    elif modified_stats["Crit Chance"] >= 100:
        didcrit = True
    elif modified_stats["Crit Chance"] == 0:
        didcrit = False


    if not didcrit:
        postmitigationDamage = modified_stats["Attack Damage"]
        crit_adjusting += 5
    else:
        postmitigationDamage = modified_stats["Attack Damage"] * modified_stats["Crit Multiplier"]

    return postmitigationDamage, crit_adjusting