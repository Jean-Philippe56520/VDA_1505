import base64
from pathlib import Path

# Chemin vers ton image
IMAGE_PATH = "bg.png"   # adapte si besoin
OUTPUT_FILE = "bg_base64.txt"

def image_to_base64(path: str) -> str:
    data = Path(path).read_bytes()
    return base64.b64encode(data).decode("utf-8")

if __name__ == "__main__":
    b64 = image_to_base64(IMAGE_PATH)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(b64)

    print("✅ Conversion terminée")
    print(f"➡ Base64 écrit dans : {OUTPUT_FILE}")
