import math
import random as rd

average_point_x = 0
average_point_y = 0
summation_point_x = 0
summation_point_y = 0
circle_radius_x = 0.5
circle_radius_y = 0.5
amount_estimates = range(0, 50)
amount_points = range(0, 100)
pi_approximation = 0
distance_point_radius = 0


for estimate in amount_estimates:
    amount_points_in_circle = 0
    for point in amount_points:
        point_x = rd.random()
        point_y = rd.random()
        distance_point_radius = (
            (point_x - circle_radius_x)**2 + (point_y - circle_radius_y)**2)**0.5
        if distance_point_radius < circle_radius_x:
            amount_points_in_circle += 1

    print("Número de pontos dentro do círculo:", amount_points_in_circle)
    print("Número total de pontos:", len(amount_points))
    probability_point_in_circle = amount_points_in_circle/len(amount_points)
    pi_approximation_current_estimative = 4 * probability_point_in_circle
    error_estimate = abs(math.pi - pi_approximation_current_estimative)

    print("Estimativa para p", probability_point_in_circle)
    print("Estimativa para pi", pi_approximation_current_estimative)
    print("Erro:", error_estimate)
    error_estimate_sum += abs(math.pi - pi_approximation_current_estimative)
    print()

error_estimate_average = error_estimate_sum/len(amount_estimates)
print("Em", len(amount_estimates), "repetições do jogo, a media de erro estimada, em um total de",
      len(amount_points), "pontos por estimativa, eh", error_estimate_average)
