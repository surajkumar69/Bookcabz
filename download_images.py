import urllib.request
import time
import urllib.parse

images = {
    "fleet_crysta.jpg": "photorealistic premium white Toyota Innova Crysta car parked in India 8k resolution",
    "fleet_tempo.jpg": "photorealistic premium white Tempo Traveller minibus parked in India 8k resolution",
    "fleet_urbania.jpg": "photorealistic premium white Force Urbania luxury van parked in India 8k resolution",
    "fleet_carens.jpg": "photorealistic premium white Kia Carens car parked in India 8k resolution",
    "fleet_innova.jpg": "photorealistic premium white Toyota Innova car parked in India 8k resolution"
}

for filename, prompt in images.items():
    url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote(prompt)}"
    print(f"Downloading {filename}...")
    try:
        urllib.request.urlretrieve(url, f"assets/images/{filename}")
        print("Success")
    except Exception as e:
        print(f"Failed: {e}")
    time.sleep(2)
