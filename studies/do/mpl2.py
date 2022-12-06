import matplotlib.pyplot as plt
import csv

with open('task191.csv', 'r',encoding='utf-8') as csv_file:
    data = csv.DictReader(csv_file, delimiter=';')

    # средний расход бензина по месяцам
    count = [0] * 9 # список количества бензина по дням
    count1 = [0] * 9 # список количества операция по дням
    count2 = [0] * 9  # список сумм расстояний

    for i in data:
        if i['Дата'] == '1 октября':
            count[0] += int(i['Расход бензина'])
            count1[0] += 1
            count2[0] += int(i['Расстояние'])
        elif i['Дата'] == '2 октября':
            count[1] += int(i['Расход бензина'])
            count1[1] += 1
            count2[1] += int(i['Расстояние'])
        elif i['Дата'] == '3 октября':
            count[2] += int(i['Расход бензина'])
            count1[2] += 1
            count2[2] += int(i['Расстояние'])
        elif i['Дата'] == '4 октября':
            count[3] += int(i['Расход бензина'])
            count1[3] += 1
            count2[3] += int(i['Расстояние'])
        elif i['Дата'] == '5 октября':
            count[4] += int(i['Расход бензина'])
            count1[4] += 1
            count2[4] += int(i['Расстояние'])
        elif i['Дата'] == '6 октября':
            count[5] += int(i['Расход бензина'])
            count1[5] += 1
            count2[5] += int(i['Расстояние'])
        elif i['Дата'] == '7 октября':
            count[6] += int(i['Расход бензина'])
            count1[6] += 1
            count2[6] += int(i['Расстояние'])
        elif i['Дата'] == '8 октября':
            count[7] += int(i['Расход бензина'])
            count1[7] += 1
            count2[7] += int(i['Расстояние'])
        elif i['Дата'] == '9 октября':
            count[8] += int(i['Расход бензина'])
            count1[8] += 1
            count2[8] += int(i['Расстояние'])

    # среднее значение расхода бензина
    mean = list(map(lambda x, y: x / y, count, count1))
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    groups = [(str(i)) for i in range(1, 10)]
    groups1 = [(str(i) + ' октября') for i in range(1, 10)]
    ax1.grid(True)
    ax1.bar(groups, mean, label=groups)
    ax1.set_ylabel('расход бензина в день')
    ax1.set_title('Среднее значение \nрасхода бензина \nв день')

    # зависимость признака расстояния на расход бензина
    mean1 = list(map(lambda x, y: x / y, count2, count1))
    mean1.sort()
    mean.sort()
    ax2.grid(True)
    ax2.plot(mean, mean1)
    ax2.set_ylabel('среднее расстояние за день')
    ax2.set_xlabel('среднее количество бензина за день')
    ax2.set_title('Зависимость среднего количества \nбензина от среднего расстояния за день')

    # суммарное количество бензина по дням
    ax3.set_title('Процентное распределение количества бензина по дням')
    ax3.pie(count, labels=groups1, autopct='%1.1f%%')

    plt.show()
