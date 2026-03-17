import base64

# สมมติรหัสผ่านที่เราจะส่งผ่าน Network
secret = "MyPassword123"

# 1. แปลงเป็น Base64 (เหมือนการเปลี่ยนภาษาให้คนทั่วไปอ่านไม่ออก)
encoded = base64.b64encode(secret.encode())
print(f"ข้อมูลที่ส่งผ่านสายแลน: {encoded}")

# 2. ฝั่งรับ (Server) ก็ต้องถอดรหัสออกมา
decoded = base64.b64decode(encoded).decode()
print(f"ข้อมูลที่ Server ได้รับ: {decoded}")
