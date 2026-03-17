import os
from dotenv import load_dotenv
import getpass

# 1. โหลดข้อมูลจากไฟล์ .env เข้ามาในหน่วยความจำ
load_dotenv()

# 2. ดึงค่าออกมาใช้ผ่านตัวแปรระบบ (System Environment)
correct_password = os.getenv("SUPER_SECRET_PASSWORD")
admin_name = os.getenv("ADMIN_USER")

print(f"--- ระบบล็อกอินระดับ Enterprise ---")
user_input = input("Username: ")
pass_input = getpass.getpass("Password: ")

if user_input == admin_name and pass_input == correct_password:
    print("✅ ยินดีด้วย! คุณเข้าสู่ระบบด้วยสิทธิ์สูงสุด")
else:
    print("❌ ข้อมูลไม่ถูกต้อง")