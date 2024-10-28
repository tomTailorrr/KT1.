'''import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Создание списка машин
data = {
    'Brend': ['Toyota', 'Honda', 'Ford', 'BMW', 'Audi'],
    'Model': ['Camry', 'Civic', 'Focus', 'X5', 'A4'],
    'Year': [2020, 2019, 2018, 2021, 2020],
    'Price': [25000, 45000, 12500, 60000, 30000],

}

# Создание DataFrame
df = pd.DataFrame(data)

# Вывод DataFrame в консоль
print(df)
plt.plot(df.Brend,df.Price)
plt.show()'''