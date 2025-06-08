from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # 用于 flash 消息

# 获取项目根目录
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, template_folder=os.path.join(project_root, 'templates'))
app.secret_key = 'your_secret_key_here'

# 数据库路径
DB_PATH = os.path.join(project_root, 'data', 'student.db')

# 确保 data 目录存在
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """初始化数据库表"""
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS student (
        no TEXT PRIMARY KEY,
        name TEXT,
        year INT,
        month INT,
        day INT,
        id TEXT,
        chinese REAL,
        math REAL,
        english REAL
    )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    """主页 - 显示所有学生"""
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM student ORDER BY no').fetchall()
    conn.close()
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    """添加学生"""
    if request.method == 'POST':
        no = request.form['no']
        name = request.form['name']
        year = int(request.form['year'])
        month = int(request.form['month'])
        day = int(request.form['day'])
        id_card = request.form['id']
        chinese = float(request.form['chinese'])
        math = float(request.form['math'])
        english = float(request.form['english'])
        
        conn = get_db_connection()
        try:
            conn.execute('''INSERT INTO student 
                           (no, name, year, month, day, id, chinese, math, english)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                        (no, name, year, month, day, id_card, chinese, math, english))
            conn.commit()
            flash('学生信息添加成功！', 'success')
        except sqlite3.IntegrityError:
            flash('学号已存在，添加失败！', 'error')
        finally:
            conn.close()
        
        return redirect(url_for('index'))
    
    return render_template('add_student.html')

@app.route('/edit/<student_no>', methods=['GET', 'POST'])
def edit_student(student_no):
    """编辑学生信息"""
    conn = get_db_connection()
    
    if request.method == 'POST':
        name = request.form['name']
        year = int(request.form['year'])
        month = int(request.form['month'])
        day = int(request.form['day'])
        id_card = request.form['id']
        chinese = float(request.form['chinese'])
        math = float(request.form['math'])
        english = float(request.form['english'])
        
        conn.execute('''UPDATE student 
                       SET name=?, year=?, month=?, day=?, id=?, chinese=?, math=?, english=?
                       WHERE no=?''',
                    (name, year, month, day, id_card, chinese, math, english, student_no))
        conn.commit()
        conn.close()
        flash('学生信息修改成功！', 'success')
        return redirect(url_for('index'))
    
    student = conn.execute('SELECT * FROM student WHERE no = ?', (student_no,)).fetchone()
    conn.close()
    
    if student is None:
        flash('学生不存在！', 'error')
        return redirect(url_for('index'))
    
    return render_template('edit_student.html', student=student)

@app.route('/delete/<student_no>')
def delete_student(student_no):
    """删除学生"""
    conn = get_db_connection()
    conn.execute('DELETE FROM student WHERE no = ?', (student_no,))
    conn.commit()
    conn.close()
    flash('学生信息删除成功！', 'success')
    return redirect(url_for('index'))

@app.route('/search')
def search():
    """搜索学生"""
    query = request.args.get('query', '')
    search_type = request.args.get('type', 'name')
    
    conn = get_db_connection()
    
    if search_type == 'name':
        students = conn.execute('SELECT * FROM student WHERE name LIKE ?', 
                               (f'%{query}%',)).fetchall()
    elif search_type == 'no':
        students = conn.execute('SELECT * FROM student WHERE no LIKE ?', 
                               (f'%{query}%',)).fetchall()
    else:
        students = conn.execute('SELECT * FROM student').fetchall()
    
    conn.close()
    return render_template('index.html', students=students, search_query=query)

from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import sqlite3
import pandas as pd
import json
import os
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Line
from pyecharts.globals import ThemeType


@app.route('/analytics')
def analytics():
    """数据分析页面"""
    conn = get_db_connection()
    df = pd.read_sql_query("SELECT * FROM student", conn)
    conn.close()
    
    if df.empty:
        return render_template('analytics.html', no_data=True)
    
    # 计算统计数据
    stats = {
        'total_students': len(df),
        'avg_chinese': round(df['chinese'].mean(), 2),
        'avg_math': round(df['math'].mean(), 2),
        'avg_english': round(df['english'].mean(), 2),
        'max_chinese': float(df['chinese'].max()),
        'max_math': float(df['math'].max()),
        'max_english': float(df['english'].max()),
        'min_chinese': float(df['chinese'].min()),
        'min_math': float(df['math'].min()),
        'min_english': float(df['english'].min()),
    }
    
    # 1. 平均分柱状图
    avg_bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="800px", height="400px"))
        .add_xaxis(["语文", "数学", "英语"])
        .add_yaxis("平均分", [stats['avg_chinese'], stats['avg_math'], stats['avg_english']])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="各科平均分"),
            yaxis_opts=opts.AxisOpts(name="分数"),
            xaxis_opts=opts.AxisOpts(name="科目"),
        )
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=True, position="top"),
        )
    )
    
    # 2. 成绩分布饼图（以语文为例，按分数段统计）
    chinese_bins = pd.cut(df['chinese'], bins=[0, 60, 70, 80, 90, 100], labels=['不及格', '及格', '良好', '优秀', '满分'])
    chinese_counts = chinese_bins.value_counts()
    
    pie_data = []
    for grade, count in chinese_counts.items():
        if pd.notna(grade):  # 排除 NaN 值
            pie_data.append([str(grade), int(count)])
    
    score_pie = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="800px", height="400px"))
        .add("", pie_data)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="语文成绩分布"),
            legend_opts=opts.LegendOpts(orient="vertical", pos_right="10%", pos_top="20%"),
        )
        .set_series_opts(
            label_opts=opts.LabelOpts(formatter="{b}: {c}人 ({d}%)"),
        )
    )
    
    # 3. 学生成绩对比图（取前10名学生）
    top_students = df.head(10)
    student_names = top_students['name'].tolist()
    chinese_scores = top_students['chinese'].tolist()
    math_scores = top_students['math'].tolist()
    english_scores = top_students['english'].tolist()
    
    line_chart = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="800px", height="400px"))
        .add_xaxis(student_names)
        .add_yaxis("语文", chinese_scores, is_smooth=True)
        .add_yaxis("数学", math_scores, is_smooth=True)
        .add_yaxis("英语", english_scores, is_smooth=True)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="学生成绩对比"),
            yaxis_opts=opts.AxisOpts(name="分数"),
            xaxis_opts=opts.AxisOpts(name="学生", axislabel_opts=opts.LabelOpts(rotate=45)),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            legend_opts=opts.LegendOpts(pos_top="5%"),
        )
    )
    
    # 将图表转换为 HTML
    avg_bar_html = avg_bar.render_embed()
    score_pie_html = score_pie.render_embed()
    line_chart_html = line_chart.render_embed()
    
    return render_template('analytics.html', 
                         avg_bar_html=avg_bar_html,
                         score_pie_html=score_pie_html,
                         line_chart_html=line_chart_html,
                         stats=stats)

@app.route('/api/students')
def api_students():
    """API 接口 - 获取所有学生数据"""
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM student').fetchall()
    conn.close()
    
    students_list = []
    for student in students:
        students_list.append({
            'no': student['no'],
            'name': student['name'],
            'birthday': f"{student['year']}-{student['month']:02d}-{student['day']:02d}",
            'id': student['id'],
            'chinese': student['chinese'],
            'math': student['math'],
            'english': student['english']
        })
    
    return jsonify(students_list)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)