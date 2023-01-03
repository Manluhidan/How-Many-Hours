hour = 0
min = 0.0
values = 0.0
count = 0
def normal():
    min = values
    hour = 0
    sec = min - int(min)
    sec = sec * 100
    while min > 60 or sec > 60:
        if min > 60:
            hour = hour + 1
            min = min - 60
        if sec > 60:
            min = min + 1
            sec = sec - 60
    return f"Total minutes: {values}\nTotal videos: {count}\nYou will watch {hour} Hours, {int(min)} Minutes and {int(sec)} Seconds."

def quarter():
    min = values
    hour = 0
    min = min / 1.25
    sec = min - int(min)
    sec = sec * 100
    sec = sec / 1.25
    while min > 60 or sec > 60:
        if min > 60:
            hour = hour + 1
            min = min - 60
        if sec > 60:
            min = min + 1
            sec = sec - 60
    return f"Total minutes: {values}\nTotal videos: {count}\nYou will watch {hour} Hours, {int(min)} Minutes and {int(sec)} Seconds."

def half():
    min = values
    hour = 0
    min = min / 1.5
    sec = min - int(min)
    sec = sec * 100
    sec = sec / 1.5
    while min > 60 or sec > 60:
        if min > 60:
            hour = hour + 1
            min = min - 60
        if sec > 60:
            min = min + 1
            sec = sec - 60
    return f"Total minutes: {values}\nTotal videos: {count}\nYou will watch {hour} Hours, {int(min)} Minutes and {int(sec)} Seconds."

def threeQuarters():
    min = values
    hour = 0
    min = min / 1.75
    sec = min - int(min)
    sec = sec * 100
    sec = sec / 1.75
    while min > 60 or sec > 60:
        if min > 60:
            hour = hour + 1
            min = min - 60
        if sec > 60:
            min = min + 1
            sec = sec - 60
    return f"Total minutes: {values}\nTotal videos: {count}\nYou will watch {hour} Hours, {int(min)} Minutes and {int(sec)} Seconds."

def double():
    min = values
    hour = 0
    min = min / 2
    sec = min - int(min)
    sec = sec * 100
    sec = sec / 2
    while min > 60 or sec > 60:
        if min > 60:
            hour = hour + 1
            min = min - 60
        if sec > 60:
            min = min + 1
            sec = sec - 60
    return f"Total minutes: {values}\nTotal videos: {count}\nYou will watch {hour} Hours, {int(min)} Minutes and {int(sec)} Seconds."

# num = -1
# print("\n")

# while num !=0:
#     print("You will watch:",int(hour),"Hours and",int(min),"Minutes and",int(sec),"Seconds.")
#     print("You will watch with 2x:",int(x2H),"Hours and",int(x2M),"Minutes and",int(x2S),"Seconds.")
#     num = float(input("Enter 0 to close the program: "))