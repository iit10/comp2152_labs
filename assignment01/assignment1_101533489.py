"""
Author: Omar Romero
Assignment: #1
"""

gym_member = "Alex Alliton"
preferred_weight_kg = 20.5
highest_reps = 25
membership_active = True

workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (25, 50, 30),
    "Taylor": (40, 35, 25)
}

for friend, minutes in workout_stats.items():
    total_minutes = sum(minutes)
    workout_stats[f"{friend}_Total"] = total_minutes

workout_list = [list(minutes) for friend, minutes in workout_stats.items() if "_Total" not in friend]

yoga_running = [row[:2] for row in workout_list]
print("Yoga & Running Minutes:", yoga_running)

weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting Minutes for Last Two Friends:", weightlifting_last_two)

for friend, total in workout_stats.items():
    if "_Total" in friend and total >= 120:
        print(f"Great job staying active, {friend.split('_')[0]}!")

friend_name = input("Enter a friend's name: ")
if friend_name in workout_stats:
    yoga, running, weightlifting = workout_stats[friend_name]
    total_minutes = workout_stats[f"{friend_name}_Total"]
    print(f"{friend_name}'s Workout Minutes:")
    print(f"Yoga: {yoga}, Running: {running}, Weightlifting: {weightlifting}, Total: {total_minutes}")
else:
    print(f"Friend {friend_name} not found in the records.")

friend_totals = {friend: total for friend, total in workout_stats.items() if "_Total" in friend}
highest_friend = max(friend_totals, key=friend_totals.get).split("_")[0]
lowest_friend = min(friend_totals, key=friend_totals.get).split("_")[0]

print(f"Friend with the highest total workout minutes: {highest_friend}")
print(f"Friend with the lowest total workout minutes: {lowest_friend}")
