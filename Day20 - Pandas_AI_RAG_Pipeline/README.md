# 1. Read CSV with Pandas
# 2. Add status column for each machine:
#    - Any parameter over limit: "CRITICAL"
#    - One parameter at 90% of limit: "WARNING"
#    - All parameters ok: "OK"
# 3. Filter critical and warning machines
# 4. Calculate days since last maintenance
#    (use datetime and pd.to_datetime)
# 5. Save alerts to alerts.json
# 6. Build a detailed prompt with all machine data
# 7. Send to Claude API and request:
#    - Individual recommendation per machine
#    - Priority order for interventions
#    - Estimated downtime risk
# 8. Save the AI report to maintenance_report.txt
# 9. Print summary: how many OK, WARNING, CRITICAL