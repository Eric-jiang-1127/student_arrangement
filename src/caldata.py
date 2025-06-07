import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据库
conn = sqlite3.connect('../data/student.db')
df = pd.read_sql_query("SELECT * FROM student", conn)
conn.close()

print(df)

# 可视化成绩分布
df[['chinese', 'math', 'english']].hist(bins=10)
plt.suptitle("成绩分布")
plt.show()

# 统计平均分
print("平均分：")
print(df[['chinese', 'math', 'english']].mean())