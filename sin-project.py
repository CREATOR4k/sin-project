def accurate_sine(degrees):
    if not (0 <= degrees <= 360):
        return None
    
    sign = 1
    x = degrees
    if 90 < x <= 180:
        x = 180 - x
    elif 180 < x <= 270:
        x = x - 180
        sign = -1  
    elif 270 < x <= 360:
        x = 360 - x
        sign = -1 

    # Bhaskara I's formula for approximating the sine function (works for 0–90°)
    
    numerator = 4 * x * (180 - x)
    denominator = 40500 - x * (180 - x)
    
    # Return the result, taking the quadrant sign into account

    return sign * (numerator / denominator)

try:
    user_input = input("Введите угол в градусах (от 0 до 360): ")
    angle = float(user_input)
    
    result = accurate_sine(angle)

    if result is not None:
        print(f"Точный синус (аппроксимация) для {angle}° равен: {result:.4f}")
    else:
        print("Ошибка: введите число строго от 0 до 360 градусов.")

except ValueError:
    print("Ошибка: введено не число. Пожалуйста, введите корректное числовое значение.")
