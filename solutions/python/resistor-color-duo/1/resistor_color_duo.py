def value(colors):
    values = {
        "black": "0",
        "brown": "1",
        "red": "2",
        "orange": "3",
        "yellow": "4",
        "green": "5",
        "blue": "6",
        "violet": "7",
        "grey": "8",
        "white": "9"
    }

    first_two = colors[:2]

    result = ""
    for color in first_two:
        if color in values:
            result += values[color]
        else:
            return "لون غير معروف: " + color

    return int(result)
