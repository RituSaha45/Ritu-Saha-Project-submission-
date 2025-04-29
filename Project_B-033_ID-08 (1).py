import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("G:\\onedrive\\Desktop\\monthly salary.csv")
average_salary = df['salary_in_usd'].mean()
print(f"Average Salary in USD: {average_salary:.2f}")
plt.figure(figsize=(10, 6))
plt.hist(df['salary_in_usd'], bins=30, color='blue', edgecolor='black')
plt.axvline(average_salary, color='red', linestyle='dashed', linewidth=2, label=f'Average Salary: ${average_salary:.2f}')
plt.title('Distribution of Salaries in USD')
plt.xlabel('Salary in USD')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.show()