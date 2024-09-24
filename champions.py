from itemeffects import itemeffects
from items import items
from damagecalc import Calulate_Damage_Instance
from damagecalc import critcheck



champion_stats = {
    "Jinx": {
        "Health": 610,
        "Health Growth": 99,
        "Health Regen": 3.75,
        "Health Regen Growth": 0.5,
        "Mana": 245,
        "Mana Regen": 6.7,
        "Mana Regen Growth": 1,
        "Attack Damage": 59,
        "Attack Damage Growth": 3.4,
        "Attack Speed": 0.625,
        "Attack Ratio": 0.625,
        "Attack Speed Growth": 1,
        "Armor": 28,
        "Armor Growth": 3.5,
        "Magic Resist": 30,
        "Magic Resist Growth": 1.3,
        "Movement Speed": 325,
        "Attack Range": 525,
        "Crit Chance": 0,
        "Crit Multiplier": 1.75,
        "Percent Armor Penetration": 0,
        "Lethality": 0,
        "Abilities": {
            "Passive": {
                "Passive Type": "Attack Speed Buff",
                "On Hit Mod": 0,   
            },
            "Q": {
                "AttackSpeedincreaseJinx": 30,
                "TriggersSpellBlade": False,
                "applies onhit": False,
                "Cooldown": 0,                  
                "BaseDamage": 0,
                "BonusAttackDamageRatio": 0,    
                "AttackDamageRatio": 0,
                "Level": 0,
                "ManaCost": 0,       
            },
            "W": {
                "Cooldown": 0,
            },
            "E": {
                # Add properties for E here
            },
            "R": {
                # Add properties for R here
            }
        }
    },
    "Miss Fortune": {
        "Health": 540,
        "Health Growth": 99,
        "Health Regen": 3.5,
        "Health Regen Growth": 0.55,
        "Mana": 255,
        "Mana Regen": 8,
        "Mana Regen Growth": 0.8,
        "Attack Damage": 55,
        "Attack Damage Growth": 3.5,
        "Attack Speed": 0.656,
        "Attack Ratio": 0.625,
        "Attack Speed Growth": 3.2,
        "Armor": 22,
        "Armor Growth": 3.5,
        "Magic Resist": 30,
        "Magic Resist Growth": 0.5,
        "Movement Speed": 330,
        "Attack Range": 550,
        "Crit Chance": 0,
        "Crit Multiplier": 1.75,
        "Percent Armor Penetration": 0,
        "Lethality": 0,
        "Abilities": {
            "Passive": {
                "Passive Type": "Apply Once",
                "Apply Once": 0.5,
                "Damage Type": "AD",
            },
            "Q": {
                "TriggersSpellBlade": True,
                "applies onhit": True,
                "Cooldown": 7,                  
                "BaseDamage": 20,
                "BonusAttackDamageRatio":0,            
                "AttackDamageRatio": 1,
                "Level": 0,
                "ManaCost": 0,       
            },
            "W": {
                "Cooldown": 0,
            },
            "E": {
                # Add properties for E here
            },
            "R": {
                # Add properties for R here
            }
        }
    },
    "Senna": {
        "Health": 540,
        "Health Growth": 99,
        "Health Regen": 3.5,
        "Health Regen Growth": 0.55,
        "Mana": 255,
        "Mana Regen": 8,
        "Mana Regen Growth": 0.8,
        "Attack Damage": 50,
        "Attack Damage Growth": 3.5,
        "Attack Speed": 0.625,
        "Attack Ratio": 0.4,
        "Attack Speed Growth": 3.2,
        "Armor": 22,
        "Armor Growth": 3.5,
        "Magic Resist": 30,
        "Magic Resist Growth": 0.5,
        "Movement Speed": 330,
        "Attack Range": 550,
        "Crit Chance": 0,
        "Crit Multiplier": 1.75,
        "Percent Armor Penetration": 0,
        "Lethality": 0,
        "Abilities": {
            "Passive": {
                "Passive Type": "On Hit Mod",
                "On Hit Mod": 0.2,
                "Damage Type": "AD",  
            },
            "Q": {
                "TriggersSpellBlade": True,
                "ability reset": 1,
                "applies onhit": True,
                "Cooldown": 15,                  
                "BaseDamage": 30,               
                "BonusAttackDamageRatio": 0.4,
                "AttackDamageRatio": 0,
                "Level": 0,
                "ManaCost": 0,       
            },
            "W": {
                "BaseDamage": 0,
                "Cooldown": 6,  
            },
            "E": {
                # Add properties for E here
            },
            "R": {
                # Add properties for R here
            }
        }
    },
    "Vayne": {
        "Health": 540,
        "Health Growth": 99,
        "Health Regen": 3.5,
        "Health Regen Growth": 0.55,
        "Mana": 255,
        "Mana Regen": 8,
        "Mana Regen Growth": 0.8,
        "Attack Damage": 60,
        "Attack Damage Growth": 3.5,
        "Attack Speed": 0.625,
        "Attack Ratio": 0.4,
        "Attack Speed Growth": 3.2,
        "Armor": 22,
        "Armor Growth": 3.5,
        "Magic Resist": 30,
        "Magic Resist Growth": 0.5,
        "Movement Speed": 330,
        "Attack Range": 550,
        "Crit Chance": 0,
        "Crit Multiplier": 1.75,
        "Percent Armor Penetration": 0,
        "Lethality": 0,
        "Abilities": {
            "Passive": {
                  "Passive Type": "MS Buff",
            },
            "Q": {
                "TriggersSpellBlade": True,
                "applies onhit": True,
                "Cooldown": 6,                  
                "BaseDamage": 0,               
                "BonusAttackDamageRatio": 0,
                "AttackDamageRatio": 1.75,
                "Level": 0,
                "ManaCost": 0,       
            },
            "W": {
                "On Hit Mod": 0.06,
                "Cooldown": 0,
            },
            "E": {
                # Add properties for E here
            },
            "R": {
                # Add properties for R here
            }
        }
    },
    "Fiora": {
        "Health": 620,
        "Health Growth": 99,
        "Health Regen": 3.5,
        "Health Regen Growth": 0.55,
        "Mana": 255,
        "Mana Regen": 8,
        "Mana Regen Growth": 0.8,
        "Attack Damage": 66,
        "Attack Damage Growth": 3.5,
        "Attack Speed": 0.69,
        "Attack Ratio": 0.625,
        "Attack Speed Growth": 3.2,
        "Armor": 22,
        "Armor Growth": 3.5,
        "Magic Resist": 30,
        "Magic Resist Growth": 0.5,
        "Movement Speed": 330,
        "Attack Range": 550,
        "Crit Chance": 0,
        "Crit Multiplier": 1.75,
        "Percent Armor Penetration": 0,
        "Lethality": 0,
        "Abilities": {
            "Passive": {
                "Cooldown": 1.75,
                "Passive Type": "On Hit Mod",
                "Damage Type": "True",
                "Damage Scaling": "Max Health",
                "On Hit Mod": 0.04, 
            },
            "Q": {
                "TriggersSpellBlade": True,
                "applies onhit": True,
                "Cooldown": 6.5,                  
                "BaseDamage": 70,               
                "BonusAttackDamageRatio": 0.9,
                "AttackDamageRatio": 0,
                "Level": 0,
                "ManaCost": 0,       
            },
            "W": {
                "Cooldown": 0,
            },
            "E": {
                # Add properties for E here
            },
            "R": {
                # Add properties for R here
            }
        }
    }
}



class Champions:

    @staticmethod


    def selectchamp(selected_champ):
        selected_champ_abilites = champion_stats[selected_champ]["Abilities"]
        return selected_champ_abilites
    


    def BaseAALoop(time_to_kill, autoattacks, damage_dealt, Guinsoo_Rageblade_stacked, Highest_AA_Damage, modified_stats, item_names, dummy_health, dummy_max_health, champ_level, effective_armor, selected_champ):
        selected_champ_abilites = Champions.selectchamp(selected_champ)
        CooldownP = 0 if "Cooldown" in selected_champ_abilites["Passive"] else None 
        CooldownQ = selected_champ_abilites["Q"]["Cooldown"]
        CooldownW = selected_champ_abilites["W"]["Cooldown"]
        CooldownE = 0
        CooldownR = 0
        onHitHits = 0
        crit_adjusting = 0
        SpellBladeCooldown = 0
        AA_Damage = 0
        execute_point = dummy_health * 0.05 if "The Collector" in item_names else 0
        postmitigationDamage = 0
        onHitHits = 0


        while dummy_health > execute_point:
            autoattacks += 1
            onHitHits += 1
            if modified_stats["Crit Chance"] > 0:
                postmitigationDamage, crit_adjusting = critcheck(modified_stats, crit_adjusting)
            else:
                postmitigationDamage = modified_stats["Attack Damage"]

            
            postmitigationDamage, Guinsoo_Rageblade_stacked, modified_stats["Attack Speed"], onHitHits = itemeffects.checkitems(modified_stats, selected_champ_abilites, postmitigationDamage, item_names, Guinsoo_Rageblade_stacked, dummy_health, champ_level, dummy_max_health, autoattacks, onHitHits)
            dummy_health, damage_dealt, postmitigationDamage, AA_Damage = Calulate_Damage_Instance(postmitigationDamage, effective_armor, dummy_health, damage_dealt, AA_Damage) 


            # postmitigationDamage, CooldownP, dummy_health, damage_dealt = Champions.BasePassiveLoop(modified_stats, selected_champ_abilites, postmitigationDamage, selected_champ, autoattacks, dummy_max_health, CooldownP, dummy_health, damage_dealt)
            # dummy_health, damage_dealt, postmitigationDamage, AA_Damage = Calulate_Damage_Instance(postmitigationDamage, effective_armor, dummy_health, damage_dealt, AA_Damage) 
            # postmitigationDamage, SpellBladeCooldown, dummy_health, CooldownQ, CooldownW, onHitHits, damage_dealt, AA_Damage = Champions.BaseQLoop(modified_stats, selected_champ_abilites, postmitigationDamage, execute_point, dummy_max_health, champ_level, dummy_health, item_names, SpellBladeCooldown, CooldownQ, CooldownP, selected_champ, autoattacks, damage_dealt, AA_Damage, CooldownW, onHitHits, Guinsoo_Rageblade_stacked)
            # dummy_health, damage_dealt, postmitigationDamage, AA_Damage = Calulate_Damage_Instance(postmitigationDamage, effective_armor, dummy_health, damage_dealt, AA_Damage) 
            # postmitigationDamage, SpellBladeCooldown, dummy_health, CooldownW, onHitHits, damage_dealt, AA_Damage = Champions.BaseWLoop(modified_stats, selected_champ_abilites, postmitigationDamage, execute_point, dummy_max_health, champ_level, dummy_health, item_names, SpellBladeCooldown, selected_champ, autoattacks, damage_dealt, AA_Damage, CooldownW, onHitHits)
            # dummy_health, damage_dealt, postmitigationDamage, AA_Damage = Calulate_Damage_Instance(postmitigationDamage, effective_armor, dummy_health, damage_dealt, AA_Damage)
            if "Trinity Force" in item_names:
                SpellBladeCooldown -= (1 / modified_stats["Attack Speed"])
            if autoattacks % 3 == 0 and "Guinsoos Rageblade" in item_names:
                postmitigationDamage, dummy_health, damage_dealt, AA_Damage, onHitHits, Guinsoo_Rageblade_stacked = itemeffects.Guinsoos_Rageblade_stacked(modified_stats, selected_champ_abilites, postmitigationDamage, item_names, champ_level, dummy_health, dummy_max_health, effective_armor, damage_dealt, AA_Damage, selected_champ, autoattacks, onHitHits, Guinsoo_Rageblade_stacked)
                
            time_to_kill += 1 / modified_stats["Attack Speed"]
            Highest_AA_Damage = max(Highest_AA_Damage, AA_Damage)
            AA_Damage = 0

            if "Cooldown" in selected_champ_abilites["Passive"]: CooldownP -= (1 / modified_stats["Attack Speed"])

        if "Guinsoos Rageblade" in item_names:
            if Guinsoo_Rageblade_stacked <= 4:
                modified_stats["Attack Speed"] -= (0.08 * modified_stats["Attack Ratio"]) * Guinsoo_Rageblade_stacked
        if selected_champ == "Jinx":
            modified_stats["Attack Speed"] -= champion_stats[selected_champ]["Attack Ratio"] * 0.55


        return time_to_kill, autoattacks, damage_dealt, Guinsoo_Rageblade_stacked, Highest_AA_Damage
               
    @staticmethod
    def BasePassiveLoop(modified_stats, selected_champ_abilites, postmitigationDamage, selected_champ, autoattacks, dummy_max_health, CooldownP, dummy_health, damage_dealt):
        if "Apply Once" in selected_champ_abilites["Passive"]["Passive Type"] and autoattacks == 1:
            postmitigationDamage += selected_champ_abilites["Passive"]["Apply Once"] * modified_stats["Attack Damage"]
            
        if "On Hit Mod" in selected_champ_abilites["Passive"]["Passive Type"]:
            if "AD" in selected_champ_abilites["Passive"]["Damage Type"]:
                postmitigationDamage += selected_champ_abilites["Passive"]["On Hit Mod"] * modified_stats["Attack Damage"]   
            if "True" in selected_champ_abilites["Passive"]["Damage Type"]:
                if "Cooldown" in selected_champ_abilites["Passive"]:
                    if CooldownP <= 0:
                        CooldownP = selected_champ_abilites["Passive"]["Cooldown"]
                        damage_dealt += (3 + (selected_champ_abilites["Passive"]["On Hit Mod"] * (modified_stats["Attack Damage"] - champion_stats[selected_champ]["Attack Damage"]))) / 100 * dummy_max_health
                        dummy_health -= (3 + (selected_champ_abilites["Passive"]["On Hit Mod"] * (modified_stats["Attack Damage"] - champion_stats[selected_champ]["Attack Damage"]))) / 100 * dummy_max_health
            
        return postmitigationDamage, CooldownP, dummy_health, damage_dealt
  
 # if "On Hit Mod" in selected_champ_abilites["Passive"]["Passive Type"] and "AP" in  selected_champ_abilites["Passive"]["Damage Type"]:



    @staticmethod
    def BaseQLoop(modified_stats, selected_champ_abilites, postmitigationDamage, execute_point, dummy_max_health, champ_level, dummy_health, item_names, SpellBladeCooldown, CooldownQ, CooldownP, selected_champ, autoattacks, damage_dealt, AA_Damage, CooldownW, onHitHits, Guinsoo_Rageblade_stacked):
            if selected_champ == "Jinx" and autoattacks <= 3:
                modified_stats["Attack Speed"] += champion_stats[selected_champ]["Attack Ratio"] * 0.18
            if CooldownQ > 0:
                if "ability reset" in selected_champ_abilites["Q"]:
                    CooldownQ -= selected_champ_abilites["Q"]["ability reset"] 
                CooldownQ -= (1 / modified_stats["Attack Speed"]) #check if it goes below 0 in the same iteration of the loop then do it before the next iteration
            else:
                print(CooldownQ)
                CooldownQ = selected_champ_abilites["Q"]["Cooldown"] + CooldownQ
                print(CooldownQ)
                postmitigationDamage = selected_champ_abilites["Q"]["BaseDamage"] + selected_champ_abilites["Q"]["BonusAttackDamageRatio"] * (modified_stats["Attack Damage"] - champion_stats[selected_champ]["Attack Damage"]) + selected_champ_abilites["Q"]["AttackDamageRatio"] * modified_stats["Attack Damage"]
                CooldownQ -= selected_champ_abilites["Q"]["ability reset"] if "ability reset" in selected_champ_abilites["Q"] else 0
                if selected_champ_abilites["Q"]["applies onhit"] == True:
                    postmitigationDamage, Guinsoo_Rageblade_stacked, modified_stats["Attack Speed"], onHitHits = itemeffects.checkitems(modified_stats, selected_champ_abilites, postmitigationDamage, item_names, Guinsoo_Rageblade_stacked, dummy_health, champ_level, dummy_max_health, autoattacks, onHitHits)
                    postmitigationDamage, SpellBladeCooldown, dummy_health, CooldownW, onHitHits, damage_dealt, AA_Damage = Champions.BaseWLoop(modified_stats, selected_champ_abilites, postmitigationDamage, execute_point, dummy_max_health, champ_level, dummy_health, item_names, SpellBladeCooldown, selected_champ, autoattacks, damage_dealt, AA_Damage, CooldownW, onHitHits)
                    postmitigationDamage, CooldownP, dummy_health, damage_dealt = Champions.BasePassiveLoop(modified_stats, selected_champ_abilites, postmitigationDamage, selected_champ, autoattacks, dummy_max_health, CooldownP, dummy_health, damage_dealt)
                if selected_champ_abilites["Q"]["TriggersSpellBlade"] and selected_champ_abilites["Q"]["applies onhit"] == True:
                    SpellBlade = itemeffects.Trinity_Force(item_names, SpellBladeCooldown)
                    if SpellBlade == 2 and selected_champ_abilites["Q"]["applies onhit"]:
                        postmitigationDamage += champion_stats[selected_champ]["Attack Damage"] * 2
                        SpellBladeCooldown = 1.5
                        SpellBlade == 0
                

            return postmitigationDamage, SpellBladeCooldown, dummy_health, CooldownQ, CooldownW, onHitHits, damage_dealt, AA_Damage
    
    @staticmethod
    def BaseWLoop(modified_stats, selected_champ_abilites, postmitigationDamage, execute_point, dummy_max_health, champ_level, dummy_health, item_names, SpellBladeCooldown, selected_champ, autoattacks, damage_dealt, AA_Damage, CooldownW, onHitHits):
        if "On Hit Mod" in selected_champ_abilites["W"]:
            if onHitHits % 3 == 0:
                if selected_champ == "Vayne":
                    dummy_health -= selected_champ_abilites["W"]["On Hit Mod"] * dummy_max_health
                    damage_dealt += selected_champ_abilites["W"]["On Hit Mod"] * dummy_max_health
                    AA_Damage += selected_champ_abilites["W"]["On Hit Mod"] * dummy_max_health

        return postmitigationDamage, SpellBladeCooldown, dummy_health, CooldownW, onHitHits, damage_dealt, AA_Damage

            

    


                    

