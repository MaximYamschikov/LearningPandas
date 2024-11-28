def correlation_solution(x, y):
    n = len(x)
    xs = sum(x)/n
    ys = sum(y)/n

    sum_xy = 0.0
    sum_x = 0.0
    sum_y = 0.0
    for i in range(n):
        sum_xy += (x[i] - xs) * (y[i] - ys)
        sum_x += (x[i] - xs)**2
        sum_y += (y[i] - ys)**2

    return round(sum_xy/((sum_x*sum_y)**0.5),2)

x = [0,6,15,9,10]
y = [15,
18,
21,
17,
19
]

print(correlation_solution(x,y))