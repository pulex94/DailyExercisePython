The program must:
# 1. Read the JSON file
# 2. Extract factory name and timestamp
# 3. Read limits from the JSON — not hardcoded
# 4. Check each machine:
#    - temperature > max_temperature: ALERT
#    - pressure > max_pressure: ALERT
#    - both over limit: CRITICAL
#    - all ok: OK
# 5. Count machines by status: OK, ALERT, CRITICAL
# 6. Save the results to a new file alerts.json
# 7. Print a clean summary report
New challenge:
# Limits come from the JSON file — not hardcoded in Python
# Save results to a new JSON file using json.dump()