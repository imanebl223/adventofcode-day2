# Auteur : Imane Ben Blla
# Description : Solutions pour la Part 1 et Part 2

# --- PART 1 ---
def is_safe(report):
    """Vérifie si un rapport est 'safe' selon les règles de la Part 1."""
    diffs = [report[i+1] - report[i] for i in range(len(report) - 1)]
    all_increasing = all(1 <= d <= 3 for d in diffs)
    all_decreasing = all(-3 <= d <= -1 for d in diffs)
    return all_increasing or all_decreasing


def part1(data):
    """Compte le nombre de rapports 'safe' pour la Part 1."""
    safe_count = 0
    for line in data:
        report = list(map(int, line.split()))
        if is_safe(report):
            safe_count += 1
    return safe_count


# --- PART 2 ---
def is_safe_with_dampener(report):
    """Vérifie si un rapport devient 'safe' après suppression d’un seul niveau."""
    if is_safe(report):
        return True
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        if is_safe(new_report):
            return True
    return False


def part2(data):
    """Compte le nombre de rapports 'safe' en tenant compte du Problem Dampener."""
    safe_count = 0
    for line in data:
        report = list(map(int, line.split()))
        if is_safe_with_dampener(report):
            safe_count += 1
    return safe_count


# --- MAIN ---
if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.readlines()

    print(" Part 1 - Safe reports:", part1(data))
    print("  Part 2 - Safe reports with Problem Dampener:", part2(data))
