import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from itertools import combinations

import numpy as np
from itertools import combinations as itertools_combinations
import itertools
from champions import Champions
from items import items
from champions import champion_stats

crit_adjusting = 0

def calculate_modified_stats(selected_champ, item_names, bonusattackspeed, bonusattackdamage, bonus_crit, bonushealth):
    base_stats = champion_stats[selected_champ]
    modified_stats = {
        "Health": base_stats["Health"] + bonushealth,
        "Attack Damage": base_stats["Attack Damage"] + bonusattackdamage,
        "Attack Speed": 0,
        "Attack Ratio": base_stats["Attack Ratio"],
        "Crit Chance": base_stats["Crit Chance"] + bonus_crit,
        "Crit Multiplier": base_stats["Crit Multiplier"],
        "Lethality": base_stats["Lethality"],
        "Percent Armor Penetration": base_stats["Percent Armor Penetration"]
    }

    # Apply item effects
    for item_name in item_names:
        item_effects = items.get(item_name, {})
        for key, value in item_effects.items():
            if key in modified_stats:
                modified_stats[key] += value

    # Calculate attack speed
    modified_stats["Attack Speed"] = ((modified_stats["Attack Speed"] + ((bonusattackspeed) /100))) * base_stats["Attack Ratio"] + base_stats["Attack Speed"]

    # Calculate percent armor penetration if Serylda Grudge is equipped
    if "Serylda Grudge" in item_names:
        modified_stats["Percent Armor Penetration"] = 25 + (modified_stats["Lethality"] * 0.11)

    modified_stats["Attack Damage"] = modified_stats["Attack Damage"] + ((modified_stats["Health"] - base_stats["Health"])  * 0.02 if "OverLords BloodMail" in item_names else 0)

    return modified_stats

def run_simulation_once(modified_stats, item_names, dummy_health, dummy_max_health, champ_level, selected_champ, effective_armor):
    time_to_kill = 0
    autoattacks = 0
    damage_dealt = 0
    Guinsoo_Rageblade_stacked = 0
    Highest_AA_Damage = 0
   
    time_to_kill, autoattacks, damage_dealt, Guinsoo_Rageblade_stacked, Highest_AA_Damage = Champions.BaseAALoop(time_to_kill, autoattacks, damage_dealt, Guinsoo_Rageblade_stacked, Highest_AA_Damage, modified_stats, item_names, dummy_health, dummy_max_health, champ_level, effective_armor, selected_champ)

    return time_to_kill, autoattacks, damage_dealt, Guinsoo_Rageblade_stacked, Highest_AA_Damage

def run_multiple_simulations(selected_champ, item_names, n, bonusattackspeed, bonusattackdamage, bonus_crit, dummy_armor, dummy_health, champ_level, bonushealth):
    modified_stats = calculate_modified_stats(selected_champ, item_names, bonusattackspeed, bonusattackdamage, bonus_crit, bonushealth)
    total_time_to_kill = 0
    total_autoattacks = 0
    total_damage_dealt = 0
    dps_values = []

    dummy_max_health = dummy_health

    effective_armor = (dummy_armor * (1 - (modified_stats["Percent Armor Penetration"] / 100))) - modified_stats["Lethality"]
    if effective_armor < 0:
        effective_armor = 0

    for _ in range(n):
        dummy_health_local = dummy_health
        time_to_kill, autoattacks, damage_dealt, Guinsoo_Rageblade_stacked, Highest_AA_Damage = run_simulation_once(
            modified_stats, item_names, dummy_health_local, dummy_max_health, champ_level, selected_champ, effective_armor
        )
        total_time_to_kill += time_to_kill
        total_autoattacks += autoattacks
        total_damage_dealt += damage_dealt
        dps_values.append(damage_dealt / time_to_kill)  # Collect DPS values

    avg_time_to_kill = total_time_to_kill / n
    avg_autoattacks = total_autoattacks / n
    avg_dps = total_damage_dealt / total_time_to_kill
    median_dps = np.median(dps_values)
    lowest_dps = min(dps_values)
    highest_dps = max(dps_values)

    return avg_time_to_kill, avg_autoattacks, avg_dps, median_dps, lowest_dps, highest_dps, modified_stats, Guinsoo_Rageblade_stacked, Highest_AA_Damage

def update_results():
    sort_by = sort_var.get()
    
    if not results:
        results_text.delete(1.0, tk.END)
        results_text.insert(tk.END, "No results to display.\n")
        return

    # Sort results based on selected criterion
    if sort_by in ["Average DPS", "Median DPS", "Lowest DPS", "Highest DPS", "Highest AA Damage"]:
        sorted_results = sorted(results.items(), key=lambda x: x[1][sort_by], reverse=True)
    else:
        sorted_results = sorted(results.items(), key=lambda x: x[1]["Average DPS"], reverse=True)

    # Display results in the UI
    results_text.delete(1.0, tk.END)
    results_text.insert(tk.END, "Top 10 Item Combinations:\n")
    results_text.insert(tk.END, "=" * 40 + "\n")
    for item_combination, stats in sorted_results[:10]:
        items_str = ", ".join(item_combination)
        results_text.insert(tk.END, f"Items: {items_str}\n")
        results_text.insert(tk.END, f"Average Time to Kill: {stats['Average Time to Kill']:.2f} seconds\n")
        results_text.insert(tk.END, f"Average Number of Auto-attacks: {stats['Average Number of Auto-attacks']:.2f}\n")
        results_text.insert(tk.END, f"Average DPS: {stats['Average DPS']:.2f}\n")
        results_text.insert(tk.END, f"Median DPS: {stats['Median DPS']:.2f}\n")
        results_text.insert(tk.END, f"Lowest DPS: {stats['Lowest DPS']:.2f}\n")
        results_text.insert(tk.END, f"Highest DPS: {stats['Highest DPS']:.2f}\n")
        results_text.insert(tk.END, f"Attack Speed: {stats['Attack Speed']:.2f}\n")
        results_text.insert(tk.END, f"Attack Damage: {stats['Attack Damage']:.2f}\n")
        results_text.insert(tk.END, f"Percent Armor Penetration: {stats['Percent Armor Penetration']:.2f}%\n")
        results_text.insert(tk.END, f"Lethality: {stats['Lethality']:.2f}\n")
        results_text.insert(tk.END, f"Crit Chance: {stats['Crit Chance']:.2f}%\n")
        results_text.insert(tk.END, f"Crit Multiplier: {stats['Crit Multiplier']:.2f}\n")
        results_text.insert(tk.END, f"Highest AA Damage: {stats['Highest AA Damage']:.2f}\n")
        results_text.insert(tk.END, "-" * 40 + "\n")

def contains_illegal_combination(combination, illegal_combinations):
    # Check if any illegal combination is a subset of the given combination
    return any(illegal_combination.issubset(combination) for illegal_combination in illegal_combinations)

def generate_legal_combinations(selected_items, number_of_items, illegal_combinations):
    # Generate all item combinations
    all_combinations = itertools.combinations(selected_items, number_of_items)

    # Convert illegal combinations to frozensets for fast subset checking
    illegal_combinations_set = [frozenset(illegal_comb) for illegal_comb in illegal_combinations]

    # Filter out illegal combinations
    legal_combinations = [
        comb for comb in all_combinations 
        if not contains_illegal_combination(frozenset(comb), illegal_combinations_set)
    ]

    return legal_combinations  

def run_simulation():
    global results  # Use the global variable to store results

    # Retrieve user inputs
    selected_champ = champ_var.get()
    bonusattackspeed = int(attackspeed_entry.get())
    bonusattackdamage = int(attackdamage_entry.get())
    bonushealth = int(bonushealth_entry.get())
    bonus_crit = int(crit_entry.get())  # Additional crit from UI
    dummy_armor = int(armor_entry.get())
    dummy_health = int(health_entry.get())
    num_simulations = int(simulations_entry.get())
    number_of_items = int(items_entry.get())
    sort_by = sort_var.get()  # Get selected sort criterion
    champ_level = int(level_entry.get())

    if selected_champ not in champion_stats:
        messagebox.showerror("Error", f"Champion '{selected_champ}' not found in champion stats")
        return

    selected_items = [item for item, var in item_vars.items() if var.get()]

    # Identify crit-related items among the selected items
    crit_items = [item for item in selected_items if items[item].get("Crit Chance", 0) > 0]

    # Define illegal combinations
    illegal_combinations = [
        frozenset({"Lord Dominik's Regards", "Serylda's Grudge", "Mortal Reminder"}),
        frozenset({"Lord Dominik's Regards", "Serylda's Grudge"}),
        frozenset({"Serylda's Grudge", "Mortal Reminder"}),
        frozenset({"Lord Dominik's Regards", "Mortal Reminder"}),
    ]

    # Filter out illegal combinations
    legal_combinations = generate_legal_combinations(selected_items, number_of_items, illegal_combinations)

# Global variable to store simulation results
    results = {}

    Number_of_sims_totals = len(legal_combinations)
    print (Number_of_sims_totals)

    # Simulate combinations with crit items
    for item_combination in [comb for comb in legal_combinations if any(item in crit_items for item in comb)]:
        # Determine total crit chance for the combination
        crit_chance = sum(items[item].get("Crit Chance", 0) for item in item_combination) + bonus_crit
        crit_chance = min(100, crit_chance)  # Cap crit chance at 100%

        if crit_chance >= 100:
            # Simulate exactly once
            avg_time_to_kill, avg_autoattacks, avg_dps, median_dps, lowest_dps, highest_dps, modified_stats, Guinsoo_Rageblade_stacked, Highest_AA_Damage = run_multiple_simulations(
                selected_champ, item_combination, 1, bonusattackspeed, bonusattackdamage, bonus_crit, dummy_armor, dummy_health, champ_level, bonushealth
            )
        else:
            # Simulate as many times as specified
            avg_time_to_kill, avg_autoattacks, avg_dps, median_dps, lowest_dps, highest_dps, modified_stats, Guinsoo_Rageblade_stacked, Highest_AA_Damage = run_multiple_simulations(
                selected_champ, item_combination, 1, bonusattackspeed, bonusattackdamage, bonus_crit, dummy_armor, dummy_health, champ_level, bonushealth
            )

        results[item_combination] = {
            "Average Time to Kill": avg_time_to_kill,
            "Average Number of Auto-attacks": avg_autoattacks,
            "Average DPS": avg_dps,
            "Median DPS": median_dps,
            "Lowest DPS": lowest_dps,
            "Highest DPS": highest_dps,
            "Highest AA Damage": Highest_AA_Damage,
            "Attack Speed": modified_stats["Attack Speed"] + (Guinsoo_Rageblade_stacked * 0.08 * modified_stats["Attack Ratio"] + 0.3 * modified_stats["Attack Ratio"] if selected_champ == "Jinx" else 0),
            "Attack Damage": modified_stats["Attack Damage"],
            "Percent Armor Penetration": modified_stats["Percent Armor Penetration"],
            "Lethality": modified_stats["Lethality"],
            "Crit Chance": modified_stats["Crit Chance"],
            "Crit Multiplier": modified_stats["Crit Multiplier"],
        }

    # Simulate combinations without crit items
    for item_combination in [comb for comb in legal_combinations if not any(item in crit_items for item in comb)]:
        crit_chance = bonus_crit
        if crit_chance >= 1 and crit_chance < 100:
            avg_time_to_kill, avg_autoattacks, avg_dps, median_dps, lowest_dps, highest_dps, modified_stats, Guinsoo_Rageblade_stacked, Highest_AA_Damage = run_multiple_simulations(
                selected_champ, item_combination, 1, bonusattackspeed, bonusattackdamage, bonus_crit, dummy_armor, dummy_health, champ_level, bonushealth
            )
        elif crit_chance >= 100:
            avg_time_to_kill, avg_autoattacks, avg_dps, median_dps, lowest_dps, highest_dps, modified_stats, Guinsoo_Rageblade_stacked, Highest_AA_Damage = run_multiple_simulations(
                selected_champ, item_combination, 1, bonusattackspeed, bonusattackdamage, bonus_crit, dummy_armor, dummy_health, champ_level, bonushealth
            )
        else:
            avg_time_to_kill, avg_autoattacks, avg_dps, median_dps, lowest_dps, highest_dps, modified_stats, Guinsoo_Rageblade_stacked, Highest_AA_Damage = run_multiple_simulations(
                selected_champ, item_combination, 1, bonusattackspeed, bonusattackdamage, bonus_crit, dummy_armor, dummy_health, champ_level, bonushealth
            )

        results[item_combination] = {
            "Average Time to Kill": avg_time_to_kill,
            "Average Number of Auto-attacks": avg_autoattacks,
            "Average DPS": avg_dps,
            "Median DPS": median_dps,
            "Lowest DPS": lowest_dps,
            "Highest DPS": highest_dps,
            "Highest AA Damage": Highest_AA_Damage,
            "Attack Speed": modified_stats["Attack Speed"] + (Guinsoo_Rageblade_stacked * 0.08 * modified_stats["Attack Ratio"]) + (0.3 * modified_stats["Attack Ratio"] if selected_champ == "Jinx" else 0),
            "Attack Damage": modified_stats["Attack Damage"],
            "Percent Armor Penetration": modified_stats["Percent Armor Penetration"],
            "Lethality": modified_stats["Lethality"],
            "Crit Chance": modified_stats["Crit Chance"],
            "Crit Multiplier": modified_stats["Crit Multiplier"],
        }

    update_results()


def select_all_items():
    for var in item_vars.values():
        var.set(True)

root = tk.Tk()
root.title("Champion Simulation")

# Create and place widgets for champion selection and input fields
tk.Label(root, text="Select Champion:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
champ_var = tk.StringVar(value="Vayne")
champ_dropdown = ttk.Combobox(root, textvariable=champ_var, values=list(champion_stats.keys()))
champ_dropdown.grid(row=0, column=1, padx=10, pady=5)

attack_speed_var = tk.StringVar(value="0")
tk.Label(root, text="Bonus Attack Speed (%):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
attackspeed_entry = tk.Entry(root, textvariable=attack_speed_var)
attackspeed_entry.grid(row=1, column=1, padx=10, pady=5)

attack_damage_var = tk.StringVar(value="0")
tk.Label(root, text="Bonus Attack Damage:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
attackdamage_entry = tk.Entry(root, textvariable=attack_damage_var)
attackdamage_entry.grid(row=2, column=1, padx=10, pady=5)

bonus_crit_var = tk.StringVar(value="0")
tk.Label(root, text="Crit Chance (%):").grid(row=3, column=0, padx=10, pady=5, sticky="w")
crit_entry = tk.Entry(root, textvariable=bonus_crit_var)
crit_entry.grid(row=3, column=1, padx=10, pady=5)

armor_var = tk.StringVar(value="100")
tk.Label(root, text="Dummy Armor:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
armor_entry = tk.Entry(root, textvariable=armor_var)
armor_entry.grid(row=4, column=1, padx=10, pady=5)

health_var = tk.StringVar(value="2500")
tk.Label(root, text="Dummy Health:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
health_entry = tk.Entry(root, textvariable=health_var)
health_entry.grid(row=5, column=1, padx=10, pady=5)

num_simulations_var = tk.StringVar(value="100")
tk.Label(root, text="Number of Simulations:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
simulations_entry = tk.Entry(root, textvariable=num_simulations_var)
simulations_entry.grid(row=6, column=1, padx=10, pady=5)

items_var = tk.StringVar(value="1")
tk.Label(root, text="Number of Items:").grid(row=7, column=0, padx=10, pady=5, sticky="w")
items_entry = tk.Entry(root, textvariable=items_var)
items_entry.grid(row=7, column=1, padx=10, pady=5)

champ_level_var = tk.StringVar(value="1")
tk.Label(root, text="Champion Level:").grid(row=8, column=0, padx=10, pady=5, sticky="w")
level_entry = tk.Entry(root, textvariable=champ_level_var)
level_entry.grid(row=8, column=1, padx=10, pady=5)

bonushealth_var = tk.StringVar(value="1")
tk.Label(root, text="Bonus Health:").grid(row=9, column=0, padx=10, pady=5, sticky="w")
bonushealth_entry = tk.Entry(root, textvariable=bonushealth_var)
bonushealth_entry.grid(row=9, column=1, padx=10, pady=5)

tk.Label(root, text="Sort By:").grid(row=10, column=0, padx=10, pady=5, sticky="w")
sort_var = tk.StringVar(value="Average DPS")
sort_dropdown = ttk.Combobox(root, textvariable=sort_var, values=[
    "Average DPS", "Median DPS", "Lowest DPS", "Highest DPS", "Highest AA Damage"
])
sort_dropdown.grid(row=10, column=1, padx=10, pady=5)
sort_dropdown.bind("<<ComboboxSelected>>", lambda event: update_results())

run_button = tk.Button(root, text="Run Simulation", command=run_simulation)
run_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

select_all_button = tk.Button(root, text="Select All", command=select_all_items)
select_all_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

results_text = tk.Text(root, width=80, height=20)
results_text.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

# Frame to hold item checkboxes with scrollbar
scrollbar_frame = tk.Frame(root)
scrollbar_frame.grid(row=13, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Canvas for the scrollbar
canvas = tk.Canvas(scrollbar_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Vertical scrollbar
scrollbar = tk.Scrollbar(scrollbar_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Frame inside the canvas for checkboxes
item_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=item_frame, anchor="nw")

# Update scrollbar configuration
item_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Dictionary to hold variables for each checkbox
item_vars = {}

# Create checkboxes for each item
for item in items.keys():
    var = tk.BooleanVar(value=False)
    item_vars[item] = var
    checkbox = tk.Checkbutton(item_frame, text=item, variable=var)
    checkbox.pack(anchor="w")

# Start the Tkinter event loop
root.mainloop()

