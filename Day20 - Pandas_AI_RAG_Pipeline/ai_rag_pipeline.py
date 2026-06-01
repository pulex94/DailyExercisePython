import pandas as pd
import numpy as np
import json
from anthropic import Anthropic

max_temperature = 70
max_pressure = 6.0
max_vibration = 1.0
max_hours_without_maintenance = 2000


df = pd.read_csv("machines_data.csv")
conditions = [
    (df["temperature"] > max_temperature)
    | (df["pressure"] > max_pressure)
    | (df["vibration"] > max_vibration),
    (df["temperature"] >= max_temperature * 0.9)
    | (df["pressure"] >= max_pressure * 0.9)
    | (df["vibration"] >= max_vibration * 0.9),
]
choices = [
    "CRITICAL",
    "WARNING",
]
df["status"] = np.select(conditions, choices, default="OK")

critical_machines = df[df["status"] != "OK"]
critical_machines_list = critical_machines.to_dict(orient="records")
current_day = pd.Timestamp.now()

df["last_maintenance"] = pd.to_datetime(df["last_maintenance"])
df["days_since_maintenance"] = (current_day - df["last_maintenance"]).dt.days

client = Anthropic(api_key="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

prompt = f"""
You are a expert engeneer in machine production.
Create a report in English.

You have to do a report of this {critical_machines_list}
- Individual recommendation per machine
- Priority order for interventions
- Estimated downtime risk
- If {df["days_since_maintenance"]} is over the limit {max_hours_without_maintenance} is a problem so put a warning
Easy to read and understand. 
Minimalist. Use 20 words for each machine
"""

reponse = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1000,
    messages=[{"role": "user", "content": prompt}],
)
text = reponse.content[0].text.encode("utf-8", errors="ignore").decode("utf-8")

with open("report.txt", "w", encoding="utf-8") as f:
    f.write(text)

with open("alert.json", "w") as f:
    json.dump(critical_machines_list, f, indent=2)
