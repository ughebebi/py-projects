i = 2

def m2cm(m:float)->float:
    cm_in_m = 100
    return cm_in_m*m

def cm2m(cm:float)->float:
    m_in_cm = 0.01
    return m_in_cm*cm

def strrepeat (s:str,cnt:int):
    for i in range(1,cnt+1):
        print(i*s)

def ticket (cm:int)->int:

    price = 0

    if cm < 120:
        price = 0
    elif cm >= 120 and cm <150:
        price = 100
    elif cm >=150:
        price = 200

    return price

def check_height(cm:int)->bool:
    if cm < 80:
        result = False
    elif cm > 230:
        result = False
    else:
        result = True

    return result