import pandas as pd
from datetime import datetime

# Завантажуємо дані з CSV
try:
    df = pd.read_csv('employees.csv')
except FileNotFoundError:
    print("Повідомлення про відсутність, або проблеми при відкритті файлу CSV.")
    exit()

# Додаємо колонку з віком
current_year = datetime.now().year
df['Вік'] = df['Дата народження'].apply(lambda x: current_year - int(x.split('-')[0]))

# Створюємо новий XLSX файл з 5 аркушами
with pd.ExcelWriter('employees.xlsx', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='all', index=False)
    df[df['Вік'] < 18].to_excel(writer, sheet_name='younger_18', index=False)
    df[(df['Вік'] >= 18) & (df['Вік'] <= 45)].to_excel(writer, sheet_name='18-45', index=False)
    df[(df['Вік'] > 45) & (df['Вік'] <= 70)].to_excel(writer, sheet_name='45-70', index=False)
    df[df['Вік'] > 70].to_excel(writer, sheet_name='older_70', index=False)

print("Ok, якщо програма завершила свою роботу успішно.")
