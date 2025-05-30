import pandas as pd
import random

# تعریف مقادیر عددی برای ویژگی‌های کیفی
مقادیر_کیفی = {
    "ضعیف": 0,
    "متوسط": 1,
    "خوب": 2,
    "عالی": 3,
    "مرد": 0,
    "زن": 1,
    "ندارد": 0,
    "دارد": 1,
    "کم": 0,
    "متوسط": 1,
    "زیاد": 2,
    "شهری": 0,
    "روستایی": 1
}

data = {
    "سن": [random.randint(17, 20) for _ in range(100)],
    "جنسیت": [random.choice([0, 1]) for _ in range(100)],  # 0: مرد، 1: زن
    "معدل": [round(random.uniform(14, 20), 2) for _ in range(100)],
    "ساعت_مطالعه_روزانه": [random.randint(1, 8) for _ in range(100)],
    "مشارکت_کلاسی": [random.choice([0, 1, 2, 3]) for _ in range(100)],  # 0: ضعیف، 3: عالی
    "دسترسی_به_معلم_خصوصی": [random.choice([0, 1]) for _ in range(100)],  # 0: ندارد، 1: دارد
    "وضعیت_اقتصادی": [random.choice([0, 1, 2]) for _ in range(100)],  # 0: کم، 2: زیاد
    "تعداد_کتاب_غیردرسی": [random.randint(0, 50) for _ in range(100)],
    "شرکت_در_آزمون_های_آزمایشی": [random.randint(0, 20) for _ in range(100)],
    "میزان_استرس": [random.choice([0, 1, 2]) for _ in range(100)],  # 0: کم، 2: زیاد
    "سابقه_تحصیلی_والدین": [random.choice([0, 1, 2, 3]) for _ in range(100)],  # 0: ضعیف، 3: عالی
    "دسترسی_به_اینترنت": [random.choice([0, 1]) for _ in range(100)],  # 0: ندارد، 1: دارد
    "محل_زندگی": [random.choice([0, 1]) for _ in range(100)],  # 0: شهری، 1: روستایی
    "تعداد_اعضای_خانواده": [random.randint(1, 8) for _ in range(100)],
    "شرکت_در_کلاس_های_کنکور": [random.choice([0, 1]) for _ in range(100)],
    "سلامت_جسمی": [random.choice([0, 1, 2, 3]) for _ in range(100)],  # 0: ضعیف، 3: عالی
    "علاقه_به_رشته_هدف": [random.choice([0, 1, 2, 3]) for _ in range(100)],
    "نوع_مدرسه": [random.choice([0, 1, 2]) for _ in range(100)],  # 0: دولتی، 1: غیرانتفاعی، 2: تیزهوشان
    "میزان_استفاده_از_موبایل": [random.choice([0, 1, 2]) for _ in range(100)],  # 0: کم، 2: زیاد
    "سابقه_مشاوره_تحصیلی": [random.choice([0, 1]) for _ in range(100)],  # 0: ندارد، 1: دارد
    "عملکرد_کنکور": [random.choice([0, 1, 2, 3]) for _ in range(100)]  # متغیر هدف: 0: ضعیف، 3: عالی
}

df = pd.DataFrame(data)

# ذخیره داده‌ها در فایل‌های CSV و Excel
df.to_csv("دانش_آموزان_کنکور01.csv", index=False, encoding='utf-8-sig')
df.to_excel("دانش_آموزان_کنکور01.xlsx", index=False)

print("داده‌های 100 دانش‌آموز با 20 ویژگی ایجاد و ذخیره شد.")