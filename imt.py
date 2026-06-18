mass = float(input())
height = float(input())

def IMT(m,h):
    optimal = "Оптимальная масса"
    low = "Недостаточная масса"
    over = "Избыточная масса"
    result = m / (h * h)
    if result > 25:
        return over
    elif result < 18.5:
        return low
    return optimal

print(IMT(mass, height))