def is_safe(report):
    # Vérifie si un rapport est "safe"
    diffs = [report[i+1] - report[i] for i in range(len(report)-1)]
    
    # Tous les écarts doivent être entre 1 et 3 ou entre -3 et -1
    all_increasing = all(1 <= d <= 3 for d in diffs)
    all_decreasing = all(-3 <= d <= -1 for d in diffs)
    return all_increasing or all_decreasing


with open("input.txt") as f:
    lines = f.readlines()

safe_count = 0
for line in lines:
    report = list(map(int, line.split()))
    if is_safe(report):
        safe_count += 1

print("Safe reports:", safe_count)
