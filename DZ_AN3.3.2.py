import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
df = pd.read_csv('divan_prices.csv')

# Проверка наличия столбца с ценами
if 'Цена' in df.columns:
    # Очистка цен от символов валюты и преобразование в числовой формат
    df['Цена'] = df['Цена'].replace({'₽': '', ',': '.', 'руб.': '', ' ': ''}, regex=True)
    df['Цена'] = pd.to_numeric(df['Цена'], errors='coerce')

    # Удаление NaN значений
    prices = df['Цена'].dropna()

    # Построение гистограммы
    plt.figure(figsize=(12, 6))
    plt.hist(prices, bins=10, edgecolor='black', alpha=0.7)

    # Настройка осей
    plt.title('Гистограмма цен')
    plt.xlabel('Цена')
    plt.ylabel('Количество')
    plt.grid(True)

    # Настройка форматирования оси X с шагом 1000
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1000))
    plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x):,}'))

    # Показ графика
    plt.show()
else:
    print("\nСтолбец с ценами не найден. Проверьте название столбца.")