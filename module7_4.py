team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2






print('в команде Мастера кода участников: %s' % '5')

print('Итого сегодня в командах участников: %s и %s' % (5, 6))

print('Команда Волшебники данных решили задач: {} '.format(score_2))

print(f'Команда Мастера кода решила {score_1} задач'
      f', а команда Волшебники данных {score_2} задачи.')


# исход соревнования
if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'
print(f'Результат битвы: {challenge_result}')


tasks_total = score_1 + score_2  # количество задач
time_avg = (team1_time + team2_time) / tasks_total  # среднее время решения
print(f'Сегодня было решено {tasks_total} задач,',
      f'в среднем по {time_avg:.1f} секунды на задачу!')