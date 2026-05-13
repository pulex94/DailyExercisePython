Language: English
Title: Day08 - Hotel Booking Analyzer
Objective:
Practice building and navigating nested dictionaries and lists in Python, aggregating data across multiple keys, and writing filtered results to output TXT files.

Instructions:

Create a file called bookings.csv by copying the data below.
Read the CSV and store all records as a list of dictionaries.
Build a dictionary called hotels where each key is a hotel name and the value is a list of dictionaries, each containing: guest, nights, price_per_night, paid.
Loop through hotels and calculate the total revenue for each hotel (only bookings where paid is "yes").
Find and display the hotel with the highest total revenue.
Build a dictionary called guests where each key is a guest name and the value is the total number of nights they have stayed across all hotels.
Display the guest who has stayed the most nights in total.
Filter all bookings where paid is "no" and display how many unpaid bookings exist.
Save a file called unpaid_bookings.txt containing one line per unpaid booking formatted as: Guest - Hotel - Total: €X where X is nights × price_per_night.
Save a file called top_hotels.txt with hotels sorted by total revenue from highest to lowest, formatted as: HotelName: €X.
