def label(colors):
    # جدول الألوان وقيمها
    values = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    # استخراج أول رقمين
    first_digit = values[colors[0]]
    second_digit = values[colors[1]]

    # تكوين الرقم الأساسي
    base_value = int(f"{first_digit}{second_digit}")

    # معامل الضرب من اللون الثالث
    multiplier = 10 ** values[colors[2]]

    # القيمة النهائية بالأوم
    resistance = base_value * multiplier

    # تحديد الوحدة المناسبة
    if resistance >= 1_000_000_000:
        value = resistance / 1_000_000_000
        unit = "gigaohms"
    elif resistance >= 1_000_000:
        value = resistance / 1_000_000
        unit = "megaohms"
    elif resistance >= 1_000:
        value = resistance / 1_000
        unit = "kiloohms"
    else:
        value = resistance
        unit = "ohms"

    # تنسيق الرقم: لو صحيح زي 10.0 نحوله لـ 10
    if isinstance(value, float) and value.is_integer():
        value = int(value)

    return f"{value} {unit}"
