import time
import requests  # use 'requests' if testing on desktop Python

# === CONFIG ===
FIREBASE_URL = "https://gpstracker-6bdd1-default-rtdb.asia-southeast1.firebasedatabase.app/location.json"  # <-- YOUR Firebase URL ending in .json

# Simulated GPS data
def simulate_gps():
    # You can change this to simulate different locations
    lat = 12.843492
    lon = 80.151388
    return lat, lon

# Upload using PATCH
def patch_to_firebase(lat, lon):
    data = {
        "latitude": lat,
        "longitude": lon
    }
    try:
        response = requests.patch(FIREBASE_URL, json=data)
        if response.status_code == 200:
            print("Patched to Firebase successfully!")
        else:
            print("Patch failed. Status:", response.status_code)
        response.close()
    except Exception as e:
        print("Error:", e)

# Main loop
def main():
    print("Testing PATCH to Firebase (simulated GPS)...")
    i=0
    while True:
        lat, lon = simulate_gps()
        print("Simulated Location:", lat+i, lon+i)
        i+=0.0001
        patch_to_firebase(lat+i, lon+i)
        time.sleep(2)  # Wait before next patch

# Run it
if __name__ == "__main__":
    main()
