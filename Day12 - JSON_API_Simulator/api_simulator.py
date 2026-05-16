import json

with open("factory_api.json") as f:
    data = json.load(f)

    factory = data["factory"]
    timestamp = data["timestamp"]
    machines = data["machines"]  # list
    limits = data["limits"]

    for machine in machines:
        machine_temp = machine["temperature"]
        machine_press = machine["pressure"]
        machine_status = machine["status"]
        temperature_limit = limits["max_temperature"]
        pressure_limit = limits["max_pressure"]

        if machine_temp > temperature_limit and machine_press > pressure_limit:
            machine["status"] = "CRITICAL"
        elif machine_temp > temperature_limit:
            machine["status"] = "ALERT"
        elif machine_press > pressure_limit:
            machine["status"] = "ALERT"

        else:
            machine["status"] = "OK"

    count = {
        "OK": {"total": 0, "machines": []},
        "ALERT": {"total": 0, "machines": []},
        "CRITICAL": {"total": 0, "machines": []},
    }

    for machine in machines:
        if machine["status"] in count:
            count[machine["status"]]["total"] += 1
            count[machine["status"]]["machines"].append(machine["name"])

with open("alert.json", "w") as f:
    json.dump(count, f, indent=2)

print("SUMMARY OF THE REPORT:")
for key, value in count.items():
    print(f"  {key} : {", ".join(machine for machine in value["machines"])}")
