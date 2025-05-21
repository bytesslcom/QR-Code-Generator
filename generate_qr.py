import sqlite3
import uuid
import qrcode

def add_entry(title, text, image_url):
    entry_id = str(uuid.uuid4())[:8]
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO entries (id, title, text, image_url) VALUES (?, ?, ?, ?)",
              (entry_id, title, text, image_url))
    conn.commit()
    conn.close()
    return entry_id

def generate_qr(entry_id):
    url = f"https://qr-code-generator-1-8sq9.onrender.co/view/{entry_id}"
    img = qrcode.make(url)
    img.save(f"{entry_id}.png")
    print(f"QR Code saved as {entry_id}.png with URL: {url}")

# Example usage
if __name__ == '__main__':
    title = "Welcome!"
    text = "Scan this to see the greeting message and image."
    image_url = "https://via.placeholder.com/300.png"
    entry_id = add_entry(title, text, image_url)
    generate_qr(entry_id)
