import matplotlib.pyplot as plt

print("\n=== Health Modelling Simulation ===")
print("Enter realistic values within the suggested ranges below.")
print("(Press Enter to use the default shown in brackets.)\n")

# User inputs with suggested + ideal ranges
heart_rate = int(input("Heart rate (bpm 40–200, ideal 150–170) [160]: ") or 160)
sleep = float(input("Sleep hours (0–24, ideal 7–9) [8]: ") or 8)
bmi = float(input("BMI (10–50, ideal 20–24) [22]: ") or 22)
sys_bp = int(input("Systolic BP (70–200, ideal 90–120) [110]: ") or 110)
dia_bp = int(input("Diastolic BP (40–120, ideal 60–80) [70]: ") or 70)
water = float(input("Water intake (0–10 L, ideal ≥ 2) [2]: ") or 2)
stress = int(input("Stress level (1–10, ideal 1–3) [2]: ") or 2)

# Flat if rules for WHAT-IF (user) values
heart_rate_score = 0
if 150 <= heart_rate <= 170:
    heart_rate_score = 1

sleep_score = 0
if 7 <= sleep <= 9:
    sleep_score = 1

bmi_score = 0
if 20 <= bmi <= 24:
    bmi_score = 1

bp_score = 0
if 90 <= sys_bp <= 120 and 60 <= dia_bp <= 80:
    bp_score = 1

water_score = 0
if water >= 2:
    water_score = 1

stress_score = 0
if stress <= 3:
    stress_score = 1

what_if_scores = [
    heart_rate_score,
    sleep_score,
    bmi_score,
    bp_score,
    water_score,
    stress_score
]

# Total score + label
score = sum(what_if_scores)

levels = [
    "Very Poor",
    "Poor",
    "Fair",
    "Good",
    "Very Good",
    "Excellent",
    "Outstanding"
]

print(f"\nHealth Score: {score}/6 → {levels[score]}")

# Perfect healthy person (all 1s)
default_scores = [1, 1, 1, 1, 1, 1]

# Graph labels
parameters = ["Heart Rate", "Sleep", "BMI", "Blood Pressure", "Water", "Stress"]

# BAR CHART (shows student's scores)
plt.figure(figsize=(10, 5))
plt.bar(parameters, what_if_scores, color="skyblue")
plt.title("Bar Chart: Each bar = 1 if your value is within the ideal healthy range (0 = outside)")
plt.ylim(-0.1, 1.2)  # allows a visible 0-level baseline
plt.ylabel("Ideal Range Match (1 = Yes, 0 = No)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# LINE GRAPH (perfect vs your data) 
plt.figure(figsize=(12, 6))
plt.plot(parameters, default_scores, label="Perfect Healthy (Defaults)", marker="o", color="green")
plt.plot(parameters, what_if_scores, label="Your Data", marker="o", linestyle="--", color="blue")
plt.xlabel("Health Parameters")
plt.ylabel("Score (0 or 1)")
plt.title("Comparison of Health Scores (1 = ideal, 0 = outside)")
plt.legend()
plt.xticks(rotation=45)
plt.ylim(-0.2, 1.2)  # keeps the 0 line visible
plt.tight_layout()
plt.show()
