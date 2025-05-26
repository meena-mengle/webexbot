import time
import requests
import datetime

# Your API tokens
WEBEX_BOT_TOKEN = "ZGUzYTUzMmYtNDI4Ny00Yzk2LTgxMjUtNjg4MGE0ZDU3OTFkMzk1MTljMDktZDA3_PF84_2ec9c128-5f70-44f0-ac34-595d586542bb"
MAPBOX_TOKEN = "pk.eyJ1IjoibTMzbmEiLCJhIjoiY21iNTdzazVvMXl0ZjJpc2I5YzI4aTIwaCJ9.X8TJe6IPT0NqbtWN0_I6jQ"

WEBEX_API = "https://webexapis.com/v1"
HEADERS = {
    "Authorization": f"Bearer {WEBEX_BOT_TOKEN}",
    "Content-Type": "application/json"
}

# Track processed message IDs to avoid reprocessing
processed_messages = set()

def get_messages():
    res = requests.get(f"{WEBEX_API}/messages", headers=HEADERS)
    if res.status_code == 200:
        return res.json().get("items", [])
    return []

def send_message(room_id, text):
    payload = {"roomId": room_id, "text": text}
    requests.post(f"{WEBEX_API}/messages", headers=HEADERS, json=payload)

def geocode_city(city):
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{city}.json?access_token={MAPBOX_TOKEN}"
    res = requests.get(url)
    data = res.json()
    if data["features"]:
        lon, lat = data["features"][0]["center"]
        return lat, lon
    return None, None

def get_iss_pass(lat, lon):
    url = f"http://api.open-notify.org/iss-pass.json?lat={lat}&lon={lon}"
    res = requests.get(url)
    if res.status_code == 200:
        return res.json().get("response", [])
    return []

def process_message(message):
    text = message.get("text", "")
    person_email = message.get("personEmail")
    room_id = message.get("roomId")
    message_id = message.get("id")

    # Avoid echoing bot's own messages
    if person_email.endswith("@webex.bot") or message_id in processed_messages:
        return

    if text.lower().startswith("/city"):
        parts = text.strip().split(" ", 1)
        if len(parts) != 2:
            send_message(room_id, "Usage: `/city city_name`")
            return

        city_name = parts[1]
        lat, lon = geocode_city(city_name)

        if lat and lon:
            passes = get_iss_pass(lat, lon)
            if passes:
                reply = f"Next ISS flyovers over *{city_name}*:\n"
                for p in passes[:3]:
                    dt = datetime.datetime.fromtimestamp(p["risetime"])
                    reply += f"- {dt.strftime('%Y-%m-%d %H:%M:%S')} for {p['duration']} seconds\n"
            else:
                reply = "Could not get ISS pass data."
        else:
            reply = "Couldn't find that city. Try another name."

        send_message(room_id, reply)
        processed_messages.add(message_id)

def main_loop():
    print("Polling for new Webex messages...")
    while True:
        try:
            messages = get_messages()
            for msg in messages:
                process_message(msg)
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(5)  # Poll every 5 seconds

if __name__ == "__main__":
    main_loop()
