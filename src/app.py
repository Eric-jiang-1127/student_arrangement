from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import sqlite3
import pandas as pd
import json
import os
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Line
from pyecharts.globals import ThemeType

# 获取项目根目录
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 初始化 Flask 应用（只初始化一次）
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
    """搜索学生 - 支持多种搜索方式"""
    query = request.args.get('query', '')
    search_type = request.args.get('type', 'name')
    
    conn = get_db_connection()
    students = []
    
    try:
        if search_type == 'name':
            # 按姓名搜索（模糊匹配）
            students = conn.execute('SELECT * FROM student WHERE name LIKE ?', 
                                   (f'%{query}%',)).fetchall()
        
        elif search_type == 'no':
            # 按学号搜索（精确匹配或模糊匹配）
            students = conn.execute('SELECT * FROM student WHERE no LIKE ?', 
                                   (f'%{query}%',)).fetchall()
        
        elif search_type == 'id':
            # 按身份证号搜索（模糊匹配）
            students = conn.execute('SELECT * FROM student WHERE id LIKE ?', 
                                   (f'%{query}%',)).fetchall()
        
        elif search_type == 'chinese':
            # 按语文成绩搜索
            if query:
                # 支持范围搜索，例如：>=80, <=60, =90
                if query.startswith('>='):
                    score = float(query[2:])
                    students = conn.execute('SELECT * FROM student WHERE chinese >= ?', 
                                           (score,)).fetchall()
                elif query.startswith('<='):
                    score = float(query[2:])
                    students = conn.execute('SELECT * FROM student WHERE chinese <= ?', 
                                           (score,)).fetchall()
                elif query.startswith('>'):
                    score = float(query[1:])
                    students = conn.execute('SELECT * FROM student WHERE chinese > ?', 
                                           (score,)).fetchall()
                elif query.startswith('<'):
                    score = float(query[1:])
                    students = conn.execute('SELECT * FROM student WHERE chinese < ?', 
                                           (score,)).fetchall()
                elif query.startswith('='):
                    score = float(query[1:])
                    students = conn.execute('SELECT * FROM student WHERE chinese = ?', 
                                           (score,)).fetchall()
                else:
                    # 精确匹配
                    score = float(query)
                    students = conn.execute('SELECT * FROM student WHERE chinese = ?', 
                                           (score,)).fetchall()
        
        elif search_type == 'math':
            # 按数学成绩搜索
            if query:
                if query.startswith('>='):
                    score = float(query[2:])
                    students = conn.execute('SELECT * FROM student WHERE math >= ?', 
                                           (score,)).fetchall()
                elif query.startswith('<='):
                    score = float(query[2:])
                    students = conn.execute('SELECT * FROM student WHERE math <= ?', 
                                           (score,)).fetchall()
                elif query.startswith('>'):
                    score = float(query[1:])
                    students = conn.execute('SELECT * FROM student WHERE math > ?', 
                                           (score,)).fetchall()
                elif query.startswith('<'):
                    score = float(query[1:])
                    students = conn.execute('SELECT * FROM student WHERE math < ?', 
                                           (score,)).fetchall()
                elif query.startswith('='):
                    score = float(query[1:])
                    students = conn.execute('SELECT * FROM student WHERE math = ?', 
                                           (score,)).fetchall()
                else:
                    score = float(query)
                    students = conn.execute('SELECT * FROM student WHERE math = ?', 
                                           (score,)).fetchall()
        
        elif search_type == 'english':
            # 按英语成绩搜索
            if query:
                if query.startswith('>='):
                    score = float(query[2:])
                    students = conn.execute('SELECT * FROM student WHERE english >= ?', 
                                           (score,)).fetchall()
                elif query.startswith('<='):
                    score = float(query[2:])
                    students = conn.execute('SELECT * FROM student WHERE english <= ?', 
                                           (score,)).fetchall()
                elif query.startswith('>'):
                    score = float(query[1:])
                    students = conn.execute('SELECT * FROM student WHERE english > ?', 
                                           (score,)).fetchall()
                elif query.startswith('<'):
                    score = float(query[1:])
                    students = conn.execute('SELECT * FROM student WHERE english < ?', 
                                           (score,)).fetchall()
                elif query.startswith('='):
                    score = float(query[1:])
                    students = conn.execute('SELECT * FROM student WHERE english = ?', 
                                           (score,)).fetchall()
                else:
                    score = float(query)
                    students = conn.execute('SELECT * FROM student WHERE english = ?', 
                                           (score,)).fetchall()
        
        elif search_type == 'total':
            # 按总分搜索
            if query:
                if query.startswith('>='):
                    score = float(query[2:])
                    students = conn.execute('SELECT * FROM student WHERE (chinese + math + english) >= ?', 
                                           (score,)).fetchall()
                elif query.startswith('<='):
                    score = float(query[2:])
                    students = conn.execute('SELECT * FROM student WHERE (chinese + math + english) <= ?', 
                                           (score,)).fetchall()
                elif query.startswith('>'):
                    score = float(query[1:])
                    students = conn.execute('SELECT * FROM student WHERE (chinese + math + english) > ?', 
                                           (score,)).fetchall()
                elif query.startswith('<'):
                    score = float(query[1:])
                    students = conn.execute('SELECT * FROM student WHERE (chinese + math + english) < ?', 
                                           (score,)).fetchall()
                else:
                    score = float(query)
                    students = conn.execute('SELECT * FROM student WHERE (chinese + math + english) = ?', 
                                           (score,)).fetchall()
        
        elif search_type == 'average':
            # 按平均分搜索
            if query:
                if query.startswith('>='):
                    score = float(query[2:])
                    students = conn.execute('SELECT * FROM student WHERE (chinese + math + english) / 3.0 >= ?', 
                                           (score,)).fetchall()
                elif query.startswith('<='):
                    score = float(query[2:])
                    students = conn.execute('SELECT * FROM student WHERE (chinese + math + english) / 3.0 <= ?', 
                                           (score,)).fetchall()
                elif query.startswith('>'):
                    score = float(query[1:])
                    students = conn.execute('SELECT * FROM student WHERE (chinese + math + english) / 3.0 > ?', 
                                           (score,)).fetchall()
                elif query.startswith('<'):
                    score = float(query[1:])
                    students = conn.execute('SELECT * FROM student WHERE (chinese + math + english) / 3.0 < ?', 
                                           (score,)).fetchall()
                else:
                    score = float(query)
                    students = conn.execute('SELECT * FROM student WHERE (chinese + math + english) / 3.0 = ?', 
                                           (score,)).fetchall()
        
        elif search_type == 'year':
            # 按出生年份搜索
            if query:
                year = int(query)
                students = conn.execute('SELECT * FROM student WHERE year = ?', 
                                       (year,)).fetchall()
        
        else:
            # 默认显示所有学生
            students = conn.execute('SELECT * FROM student ORDER BY no').fetchall()
    
    except (ValueError, TypeError):
        # 处理无效的搜索参数
        flash('搜索参数格式错误，请检查输入！', 'error')
        students = conn.execute('SELECT * FROM student ORDER BY no').fetchall()
    
    finally:
        conn.close()
    
    return render_template('index.html', students=students, search_query=query, search_type=search_type)

@app.route('/advanced_search', methods=['GET', 'POST'])
def advanced_search():
    """高级搜索页面"""
    if request.method == 'POST':
        # 获取表单数据
        name = request.form.get('name', '').strip()
        no = request.form.get('no', '').strip()
        chinese_min = request.form.get('chinese_min', '')
        chinese_max = request.form.get('chinese_max', '')
        math_min = request.form.get('math_min', '')
        math_max = request.form.get('math_max', '')
        english_min = request.form.get('english_min', '')
        english_max = request.form.get('english_max', '')
        year = request.form.get('year', '')
        
        # 构建SQL查询
        conditions = []
        params = []
        
        if name:
            conditions.append("name LIKE ?")
            params.append(f"%{name}%")
        
        if no:
            conditions.append("no LIKE ?")
            params.append(f"%{no}%")
        
        if chinese_min:
            conditions.append("chinese >= ?")
            params.append(float(chinese_min))
        
        if chinese_max:
            conditions.append("chinese <= ?")
            params.append(float(chinese_max))
        
        if math_min:
            conditions.append("math >= ?")
            params.append(float(math_min))
        
        if math_max:
            conditions.append("math <= ?")
            params.append(float(math_max))
        
        if english_min:
            conditions.append("english >= ?")
            params.append(float(english_min))
        
        if english_max:
            conditions.append("english <= ?")
            params.append(float(english_max))
        
        if year:
            conditions.append("year = ?")
            params.append(int(year))
        
        # 执行查询
        conn = get_db_connection()
        if conditions:
            sql = f"SELECT * FROM student WHERE {' AND '.join(conditions)} ORDER BY no"
            students = conn.execute(sql, params).fetchall()
        else:
            students = conn.execute('SELECT * FROM student ORDER BY no').fetchall()
        
        conn.close()
        
        return render_template('index.html', students=students, is_search_result=True)
    
    return render_template('advanced_search.html')

@app.route('/api/search_stats')
def search_stats():
    """搜索统计API"""
    search_type = request.args.get('type', 'all')
    
    conn = get_db_connection()
    
    if search_type == 'score_distribution':
        # 成绩分布统计
        stats = {
            'chinese': {
                'excellent': conn.execute('SELECT COUNT(*) FROM student WHERE chinese >= 90').fetchone()[0],
                'good': conn.execute('SELECT COUNT(*) FROM student WHERE chinese >= 80 AND chinese < 90').fetchone()[0],
                'fair': conn.execute('SELECT COUNT(*) FROM student WHERE chinese >= 70 AND chinese < 80').fetchone()[0],
                'pass': conn.execute('SELECT COUNT(*) FROM student WHERE chinese >= 60 AND chinese < 70').fetchone()[0],
                'fail': conn.execute('SELECT COUNT(*) FROM student WHERE chinese < 60').fetchone()[0]
            },
            'math': {
                'excellent': conn.execute('SELECT COUNT(*) FROM student WHERE math >= 90').fetchone()[0],
                'good': conn.execute('SELECT COUNT(*) FROM student WHERE math >= 80 AND math < 90').fetchone()[0],
                'fair': conn.execute('SELECT COUNT(*) FROM student WHERE math >= 70 AND math < 80').fetchone()[0],
                'pass': conn.execute('SELECT COUNT(*) FROM student WHERE math >= 60 AND math < 70').fetchone()[0],
                'fail': conn.execute('SELECT COUNT(*) FROM student WHERE math < 60').fetchone()[0]
            },
            'english': {
                'excellent': conn.execute('SELECT COUNT(*) FROM student WHERE english >= 90').fetchone()[0],
                'good': conn.execute('SELECT COUNT(*) FROM student WHERE english >= 80 AND english < 90').fetchone()[0],
                'fair': conn.execute('SELECT COUNT(*) FROM student WHERE english >= 70 AND english < 80').fetchone()[0],
                'pass': conn.execute('SELECT COUNT(*) FROM student WHERE english >= 60 AND english < 70').fetchone()[0],
                'fail': conn.execute('SELECT COUNT(*) FROM student WHERE english < 60').fetchone()[0]
            }
        }
    else:
        # 基础统计
        stats = {
            'total_students': conn.execute('SELECT COUNT(*) FROM student').fetchone()[0],
            'avg_scores': {
                'chinese': conn.execute('SELECT AVG(chinese) FROM student').fetchone()[0],
                'math': conn.execute('SELECT AVG(math) FROM student').fetchone()[0],
                'english': conn.execute('SELECT AVG(english) FROM student').fetchone()[0]
            }
        }
    
    conn.close()
    return jsonify(stats)

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