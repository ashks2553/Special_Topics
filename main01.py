import pandas as pd
import random

data = {
    "سن": [random.randint(17, 20) for _ in range(100)],
    "جنسیت": [random.choice(["مرد", "زن"]) for _ in range(100)],
    "معدل": [round(random.uniform(12, 20), 2) for _ in range(100)],
    "ساعت مطالعه روزانه": [random.randint(1, 12) for _ in range(100)],
    "مشارکت کلاسی": [random.choice(["کم", "متوسط", "زیاد"]) for _ in range(100)],
    "دسترسی به معلم خصوصی": [random.choice(["بله", "خیر"]) for _ in range(100)],
    "وضعیت اقتصادی": [random.choice(["ضعیف", "متوسط", "خوب"]) for _ in range(100)],
    "تعداد کتاب غیر درسی": [random.choice(["کم", "زیاد"]) for _ in range(100)],
    "شرکت در آزمون های آزمایشی": [random.choice(["بله", "خیر"]) for _ in range(100)],
    "میزان استرس": [random.choice(["کم", "زیاد"]) for _ in range(100)],
    "سابقه تحصیلی والدین": [random.choice(["بله", "خیر"]) for _ in range(100)],
    "دسترسی به اینترنت": [random.choice(["بله", "خیر"]) for _ in range(100)],
    "محل زندگی": [random.choice(["شهر بزرگ", "شهر کوچک", "روستا"]) for _ in range(100)],
    "تعداد اعضای خانواده": [random.randint(1, 10) for _ in range(100)],
    "شرکت در کلاس های کنکور": [random.choice(["بله", "خیر"]) for _ in range(100)],
    "سلامت جسمی": [random.choice(["ضعیف", "متوسط", "خوب"]) for _ in range(100)],
    "علاقه به رشته هدف": [random.choice(["بله", "خیر"]) for _ in range(100)],
    "نوع مدرسه": [random.choice(["بد", "خوب"]) for _ in range(100)],
    "میزان استفاده از موبایل": [random.choice(["کم", "زیاد"]) for _ in range(100)],
    "سابقه مشاوره تحصیلی": [random.choice(["بله", "خیر"]) for _ in range(100)],
    "عملکرد کنکور": [random.choice(["ضعیف", "عالی"]) for _ in range(100)]
}

df = pd.DataFrame(data)
df.to_csv("دانش_آموزان_کنکور.csv", index=False)
df.to_excel("دانش_آموزان_کنکور.xlsx", index=False)