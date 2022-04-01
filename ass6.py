def driver(speed):
    if speed <= 70:
        print("OK")
    elif speed > 70:
        local = speed - 70
        x =local//5
        print("points ",x)
        if x>=12:
            print("License suspended")

print(driver(70))