
import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


try:
    recursion_order = int(input("Введіть рівень рекурсії (ціле число): "))
    if recursion_order >= 0:
        draw_koch_snowflake(recursion_order)
    else:
        print("Ви ввели відʼємне число. Перезапустіть програму ще раз.")
except ValueError:
    print("Ви ввели не ціле число. Перезапустіть програму ще раз.")
