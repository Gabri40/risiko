import random
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
from matplotlib.patches import Patch
import numpy as np
import multiprocessing

def roll(attackers, defenders):

    # Determine the number of dice each side rolls
    attacker_dice = min(3, attackers)
    defender_dice = min(3, defenders)

    # Roll the dice
    attacker_rolls = sorted([random.randint(1, 6) for _ in range(attacker_dice)], reverse=True)
    defender_rolls = sorted([random.randint(1, 6) for _ in range(defender_dice)], reverse=True)

    # print(f"Attacker rolls: {attacker_rolls}")
    # print(f"Defender rolls: {defender_rolls}")

    # Compare the dice rolls
    for a, d in zip(attacker_rolls, defender_rolls):
        if a > d:
            defenders -= 1
        else:
            attackers -= 1

    # print(f"Result: Attackers: {attackers}, Defenders: {defenders}")
    return attackers, defenders

def single_roll_plot(att,defs,n_rolls):
    rolls=[]

    for i in range(n_rolls):
        rolls.append(roll(att,defs))

    data_array=np.array(rolls)

    # Get unique rows and their counts
    unique_rows, counts = np.unique(data_array, axis=0, return_counts=True)

    # Calculate the percentages
    total_count = np.sum(counts)
    percentages = (counts / total_count) * 100

    
    # Plot a histogram
    plt.figure()
    plt.bar(range(len(unique_rows)), counts, tick_label=[str(tuple(row)) for row in unique_rows])
    plt.xlabel('Outcome')
    plt.ylabel('Count')
    plt.title(f"Attacker: {att}, Defender: {defs} - Single Throw - {n_rolls} Rolls")
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

    # Annotate bars with percentages
    for i, percentage in enumerate(percentages):
        plt.text(i, counts[i] + 500, f'{percentage:.2f}%', ha='center')

    plt.show()
    plt.close()


# keep rolling untill either attacker or defender has 0 armies
def roll_till_end_plot(att, defs, n_rolls):
    rolls = []

    for i in range(n_rolls):
        a = att
        d = defs
        while a > 0 and d > 0:
            a, d = roll(a, d)
        rolls.append((a, d))

    data_array = np.array(rolls)

    # Get unique rows and their counts
    unique_rows, counts = np.unique(data_array, axis=0, return_counts=True)

    # Calculate the percentages
    total_count = np.sum(counts)
    percentages = (counts / total_count) * 100

    # Calculate the total percentages for blue (attacker loses) and red (defender loses)
    blue_total_percentage = np.sum(percentages[np.where(unique_rows[:, 0] == 0)])
    red_total_percentage = np.sum(percentages[np.where(unique_rows[:, 1] == 0)])

    colors = [to_rgba('blue' if row[0] == 0 else 'red') for row in unique_rows]

    # Plot a histogram
    plt.figure()
    bars = plt.bar(range(len(unique_rows)), counts, color=colors, tick_label=[str(tuple(row)) for row in unique_rows])
    plt.xlabel('Outcome')
    plt.ylabel('Count')
    plt.title(f"Attacker: {att}, Defender: {defs} - Roll till end - {n_rolls} Rolls")
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

    # Annotate bars with percentages
    for i, percentage in enumerate(percentages):
        plt.text(i, counts[i] + 500, f'{percentage:.2f}%', ha='center')

    # Create custom legend handles and labels
    legend_elements = [
        Patch(facecolor='blue', label=f'Blue (Defense Win) - {blue_total_percentage:.2f}%'),
        Patch(facecolor='red', label=f'Red (Attack Win) - {red_total_percentage:.2f}%'),
    ]

    # Add a legend with custom handles and labels
    plt.legend(handles=legend_elements)

    plt.show()
    plt.close()


def win_chances(att, defs, n_rolls):
    rolls = []

    for i in range(n_rolls):
        a = att
        d = defs
        while a > 0 and d > 0:
            a, d = roll(a, d)
        rolls.append(1 if d == 0 else 0)

    # Calculate the percentage of ones (defender wins)
    percentage_attacker_wins = (sum(rolls) / len(rolls)) * 100

    print(f"{att}vs{defs} - Probability Attacker Wins: {percentage_attacker_wins:.2f}%")
    return percentage_attacker_wins

def simulate_rolls(n_rolls, att, defs):
    rolls = []

    for _ in range(n_rolls):
        a = att
        d = defs
        while a > 0 and d > 0:
            a, d = roll(a, d)
        rolls.append(1 if d == 0 else 0)

    return rolls

def win_chances_parallel(att, defs, n_rolls, num_processes=4):
    pool = multiprocessing.Pool(num_processes)
    results = []

    # Split the work into chunks for parallel processing
    chunk_size = n_rolls // num_processes
    chunks = [(chunk_size, att, defs) for _ in range(num_processes)]

    rolls_lists = pool.starmap(simulate_rolls, chunks)
    pool.close()
    pool.join()

    # Combine the results from each chunk
    rolls = [result for sublist in rolls_lists for result in sublist]

    # Calculate the percentage of times the attacker wins
    percentage_attacker_wins = (sum(rolls) / len(rolls)) * 100

    print(f"{att} vs {defs} - Probability Attacker Wins: {percentage_attacker_wins:.2f}%")
    return percentage_attacker_wins


att=7
defs=4
n_rolls=1000000 #million
num_processes=4
win_chances_parallel(att, defs, n_rolls, num_processes)
n_rolls=100000
# single_roll_plot(att,defs,n_rolls)
# roll_till_end_plot(att,defs,n_rolls)


