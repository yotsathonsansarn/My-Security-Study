import getpass

print("--- ระบบล็อกอินปลอดภัย (V1) ---")
user = input("ชื่อผู้ใช้: ").lower()

if user == "admin":
    print("❌ ไม่อนุญาตให้ใช้ชื่อ admin")
else:
    password = getpass.getpass("รหัสผ่าน: ")
    if len(password) < 8:
        print("❌ รหัสสั้นเกินไป")
    else:
        print(f"✅ ยินดีต้อนรับคุณ {user}")
        