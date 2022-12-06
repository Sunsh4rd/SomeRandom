import matplotlib.pyplot as plt
import pandas as pd

sales = pd.read_csv('sale_of_tour_packages.csv', delimiter=';')
agent = pd.read_csv('travel_agents.csv', delimiter=';')
travels = pd.read_csv('travels.csv', delimiter=';')

tmp = sales.merge(agent)
all_oper = tmp.merge(travels)

# 1 Задание
states = ["Благовещенск","Архангельск","Астрахань","Белгородская","Белгород","Брянск","Владимир","Волгоград",
"Вологда","Воронеж","Иваново","Иркутск","Калининград","Калуга","Кемерово","Киров","Кострома",
"Курган","Курск","Санкт-Петербург","Липецк","Магадан","Москва","Мурманск","Нижний Новгород",
"Новгород","Новосибирск","Омск","Оренбург","Орел","Пенза","Псков","Ростов-на-Дону","Рязань",
"Самара","Саратов","Южно-Сахалинск","Екатеринбург","Смоленск","Тамбов","Тверь","Томск","Тула",
"Тюмень","Ульяновск","Челябинск","Ярославль","Биробиджан"]

City = travels[travels['Город'].isin(states)]['ID тура'].reset_index(drop=True)
toursInCity = sales[sales['ID тура'].isin(City)]
toursInCity = toursInCity.drop(['ID операции', 'Дата', 'ID туроператора'], axis=1).reset_index(drop=True)
toursInCity = toursInCity.groupby("ID тура").sum()
ansSum = toursInCity['Количество проданных путёвок'].sum()
print(ansSum)

# 2 Задание
gorisont = all_oper[all_oper['Название'] == 'Горизонт']
o = gorisont.groupby(['Город']).agg({'Стоимость, на 1 чел' : 'max'})
t = o.to_dict()['Стоимость, на 1 чел']
gor_list = list(t.keys())
sale_gor = list(t.values())

fig1, ax1 = plt.subplots()
ax1.pie(sale_gor, labels=gor_list, autopct='%1.1f%%')
plt.show()

# 3 Задание
dream = all_oper[all_oper['Название'] == 'Мечта']
l = dream.groupby(['Дата']).agg({'Количество проданных путёвок' : 'sum'})
t = l.to_dict()['Количество проданных путёвок']
gor_list = list(t.keys()) # даты
sale_gor = list(t.values()) # значения


fig, axes = plt.subplots()
axes.barh(gor_list, sale_gor)
plt.show()