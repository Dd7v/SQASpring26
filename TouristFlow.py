def get_max_capacity(site_type):
    if site_type == 1:
        site_name = "Beach"
        max_capacity = 500
    elif site_type == 2:
        site_name = "Heritage Site"
        max_capacity = 200
    elif site_type == 3:
        site_name = "Nature Reserve"
        max_capacity = 174
    elif site_type == 4:
        site_name = "Urban Attraction"
        max_capacity = 800
    else:
        site_name = "Unknown"
        max_capacity = 0
    return site_name, max_capacity

def check_alert_level(current_visitors, max_capacity):
    if max_capacity == 0:
        return "ERROR", "Invalid site type selected."
    percentage = (current_visitors / max_capacity) * 100
    if percentage <= 60:
        alert = "GREEN"
        action = "Normal operations. Site is within safe capacity."
    elif percentage <= 85:
        alert = "AMBER"
        action = "Monitor closely. Redirect tourists to alternative sites."
    else:
        alert = "RED"
        action = "CRITICAL. Stop new entries. Initiate tourist redirection."
    return alert, action

site_type = int(input("Enter site type (1=Beach, 2=Heritage, 3=Nature, 4=Urban): "))
current_visitors = int(input("Enter current visitor count: "))

site_name, max_capacity = get_max_capacity(site_type)
alert, action = check_alert_level(current_visitors, max_capacity)

print(f"\nSite: {site_name}")
print(f"Visitors: {current_visitors} / {max_capacity}")
print(f"Alert Level: {alert}")
print(f"Recommended Action: {action}")
