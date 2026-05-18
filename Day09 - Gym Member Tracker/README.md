Language: English
Title: Day09 - Gym Member Tracker
Objective:
Practice building nested dictionaries and lists, aggregating data, handling multiple conditions, and writing filtered results to output TXT files. Introduction to basic error handling with try/except.

Instructions:

Create a file called gym.csv by copying the data below.
Read the CSV and store all records as a list of dictionaries, converting sessions and monthly_fee to the correct data types immediately.
Build a dictionary called members where each key is a member name and the value is a list of dictionaries, each containing: plan, sessions, monthly_fee, active.
Calculate the total sessions and total revenue (only active == "yes") for each member. Store results in a dictionary called stats.
Find and display the member with the most total sessions.
Find and display the member who has generated the most revenue.
Build a dictionary called plans where each key is a plan name and the value is the count of active members on that plan.
Display the plans sorted by count from highest to lowest.
Save a file called inactive_members.txt containing one line per inactive member formatted as: Name - Plan - Sessions: X.
Save a file called member_report.txt with all members sorted by total sessions (highest first), formatted as: Name | Sessions: X | Revenue: €Y.
