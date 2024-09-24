
from items import items
from damagecalc import Calulate_Damage_Instance


class itemeffects:


    @staticmethod
    def checkitems(modified_stats, selected_champ_abilites, postmitigationDamage, item_names, Guinsoo_Rageblade_stacked, dummy_health, champ_level, dummy_max_health, autoattacks, onHitHits):

        if "Guinsoos Rageblade" in item_names:
             postmitigationDamage, Guinsoo_Rageblade_stacked, modified_stats["Attack Speed"] = itemeffects.Guinsoos_Rageblade_stacking(modified_stats, selected_champ_abilites, postmitigationDamage, item_names, Guinsoo_Rageblade_stacked)
        if "Kraken Slayer" in item_names:
            postmitigationDamage = itemeffects.Kraken_Slayer(postmitigationDamage, item_names, onHitHits, champ_level, dummy_health, dummy_max_health)
        if "Blade of the Ruined King" in item_names:
            postmitigationDamage = itemeffects.Blade_Of_The_Ruined_King(postmitigationDamage, item_names, dummy_health)
        if "Titanic" in item_names:
            postmitigationDamage = itemeffects.TitanicHydra(postmitigationDamage, item_names, modified_stats, champ_level)
        if "Hullbreaker" in item_names:
            postmitigationDamage = itemeffects.Hullbreaker(postmitigationDamage, item_names, modified_stats, champ_level, onHitHits)

        return postmitigationDamage, Guinsoo_Rageblade_stacked, modified_stats["Attack Speed"], onHitHits
        
        

    @staticmethod
    def Guinsoos_Rageblade_stacking(modified_stats, selected_champ_abilites, postmitigationDamage, item_names, Guinsoo_Rageblade_stacked):
        if "Guinsoos Rageblade" in item_names:
            if Guinsoo_Rageblade_stacked <= 3:
                Guinsoo_Rageblade_stacked += 1
                modified_stats["Attack Speed"] += (0.08 * modified_stats["Attack Ratio"])
            else:
                postmitigationDamage += 30
        return postmitigationDamage, Guinsoo_Rageblade_stacked, modified_stats["Attack Speed"]

    @staticmethod
    def Guinsoos_Rageblade_stacked(modified_stats, selected_champ_abilites, postmitigationDamage, item_names, champ_level, dummy_health, dummy_max_health, effective_armor, damage_dealt, AA_Damage, selected_champ, autoattacks, onHitHits, Guinsoo_Rageblade_stacked):
        if autoattacks % 3 == 0 and Guinsoo_Rageblade_stacked == 4:
            onHitHits += 1
            postmitigationDamage, Guinsoo_Rageblade_stacked, modified_stats["Attack Speed"], onHitHits = itemeffects.checkitems(modified_stats, selected_champ_abilites, postmitigationDamage, item_names, Guinsoo_Rageblade_stacked, dummy_health, champ_level, dummy_max_health, autoattacks, onHitHits)
            dummy_health, damage_dealt, postmitigationDamage, AA_Damage = Calulate_Damage_Instance(postmitigationDamage, effective_armor, dummy_health, damage_dealt, AA_Damage)
        return postmitigationDamage, dummy_health, damage_dealt, AA_Damage, onHitHits, Guinsoo_Rageblade_stacked
    
    @staticmethod
    def Kraken_Slayer(postmitigationDamage, item_names, onHitHits, champ_level, dummy_health, dummy_max_health):
        if "Kraken Slayer" in item_names:
            if onHitHits % 3 == 0:
                postmitigationDamage += 112 * (1 + (dummy_health / dummy_max_health / 2))
                if champ_level >= 9:    
                    postmitigationDamage += ((champ_level - 8) * 13.6) * (1 + (dummy_health / dummy_max_health / 2))
        return postmitigationDamage
    
    def TitanicHydra(postmitigationDamage, item_names, modified_stats, champ_level):
        if "Titanic" in item_names:
            postmitigationDamage += ((modified_stats["Health"] + (99 * (champ_level - 1))) * 0.015)
        return postmitigationDamage
        
    def Hullbreaker(postmitigationDamage, item_names, modified_stats, champ_level, onHitHits):
        if "Hullbreaker" in item_names and onHitHits % 5 == 0:
            postmitigationDamage += ((modified_stats["Health"] + (99 * (champ_level - 1))) * 0.035) + (65 * 1.4)
        return postmitigationDamage
 


    @staticmethod
    def Blade_Of_The_Ruined_King(postmitigationDamage, item_names, dummy_health):
        if "Blade of the Ruined King" in item_names:
            postmitigationDamage += dummy_health * 0.06
        return postmitigationDamage
    

    def Trinity_Force(item_names, SpellBladeCooldown):
        if "Trinity Force" in item_names:
            if SpellBladeCooldown > 0:
                SpellBlade = 0
                return SpellBlade
            else:
                SpellBlade = 2
                return SpellBlade
            

            
