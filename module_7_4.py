
# использование %
team1_name = '"Мастера кода"'
team2_name = '"Волшебники данных"'
team1_num = 5
team2_num = 6

print('В команде %s участников: %s' % (team1_name, team1_num))
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))

# использование format()

score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

print('Команда {} решила задач: {}'.format(team2_name, score_2))
print('{} решили задачи за {} с'.format(team1_name, team1_time))

# использование f-строк


def winner(score1, score2, time1, time2):
    if score1 > score2 or (score1 == score2 and time1 < time2):
        result = team1_name
    elif score1 < score2 or (score1 == score2 and time1 > time2):
        result = team2_name
    else:
        result = "Ничья!"
    return result

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: победа команды {winner(score_1, score_2, team1_time, team2_time)}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg, 1)} секунды на задачу')