import requests
from pathlib import Path

BASE_URL = "https://raw.githubusercontent.com/TracingInsights/2026/main"

RACES = [
    "Australian Grand Prix",
    "Chinese Grand Prix",
    "Japanese Grand Prix"
]

SESSIONS = {
    "Race": [
        "session_laptimes.json",
        "drivers.json",
        "weather.json",
        "rcm.json"
    ],
    "Qualifying": [
        "session_laptimes.json",
        "drivers.json",
        "weather.json"
    ]
}

OUTPUT_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"


def download_file(race, session, filename):
    url = (
        f"{BASE_URL}/"
        f"{race.replace(' ', '%20')}/"
        f"{session}/"
        f"{filename}"
    )

    output_folder = OUTPUT_DIR / race / session
    output_folder.mkdir(parents=True, exist_ok=True)

    output_file = output_folder / filename

    print(f"Downloading: {race} / {session} / {filename}")

    response = requests.get(url)

    if response.status_code == 200:
        output_file.write_bytes(response.content)
        print("  ✓ Done")
    else:
        print(f"  ✗ Failed ({response.status_code})")


for race in RACES:
    for session, files in SESSIONS.items():
        for filename in files:
            download_file(race, session, filename)

print("\nAll downloads complete!")