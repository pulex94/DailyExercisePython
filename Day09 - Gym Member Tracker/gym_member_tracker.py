import csv

with open("gym.csv", "r") as f:
    reader = csv.DictReader(f)
    gym = []
    for member in reader:
        member = {
            "name" : member["name"],
            "plan" : member["plan"],
            "sessions" : int(member["sessions"]),
            "monthly_fee" : int(member["monthly_fee"]),
            "active" : member["active"]
        }
        gym.append(member)
    
    members = {}
    for member in gym:
        member_info ={
            "sessions" : member["sessions"],
            "monthly_fee" : member["monthly_fee"],
            "active" : member["active"]
        }
        members[member["name"]] = member_info

    stats = {}
    for member, member_info in members.items():
        if member_info["active"] == "yes":
            stats[member] = {
                "total_sessions": member_info["sessions"],
                "total_revenue": member_info["monthly_fee"]
            }

    most_total_sessions_name = ""
    most_total_sessions_value = 0
    most_total_revenue_name = ""
    most_total_revenue_value = 0
    for member, member_info in stats.items():
        if member_info["total_sessions"] > most_total_sessions_value:
            most_total_sessions_name = member
            most_total_sessions_value = member_info["total_sessions"]
        if member_info["total_revenue"] > most_total_revenue_value:
            most_total_revenue_name = member
            most_total_revenue_value = member_info["total_revenue"]
    print(f"MOST SESSIONS = {most_total_sessions_name}: {most_total_sessions_value}")
    print(f"MOST REVENUE = {most_total_revenue_name}: {most_total_revenue_value}")

    plans = {}
    for member in gym:
        if member["plan"] not in plans:
            plans[member["plan"]] = 1
        else:
            plans[member["plan"]] += 1
    sorted_plan = sorted(plans.items(), key=lambda x :x[1], reverse=True)
    for plan in sorted_plan:
        print(f"{plan[0]}: {plan[1]}")
        
with open("inactive_members.txt", "w") as file:
    for member in gym:
        if member["active"] == "no":
            file.write(f"{member["name"]} - {member["plan"]} - Session: {member["sessions"]}\n")

with open("member_report.txt", "w") as file:
    sorted_gym = sorted(gym, key=lambda x :x["sessions"], reverse=True)
    for member in sorted_gym:
        file.write(f"{member["name"]} | Sessions: {member["sessions"]} | Revenue: {member["monthly_fee"]}€\n")