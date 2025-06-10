# 学生管理系统 (Student Management System)

  

一个功能完整的学生信息管理系统，采用 C 语言作为核心后端，Python Flask 作为 Web 前端，SQLite 作为数据库的混合架构设计。

  

## 🚀 项目特色

  

- **双端架构**：C 语言命令行 + Python Web 界面

- **数据持久化**：SQLite 数据库存储

- **数据可视化**：交互式图表展示

- **响应式设计**：现代化 Web 界面

- **完整功能**：增删改查、排序、搜索、统计分析

  

## 📁 项目结构

```
C语言大作业：学生管理系统 (student_arrangement)
│
├── 📁 项目根目录 /home/eric/C_project/stu_arr/
│   ├── 📄 README.md                    # 项目详细说明文档
│   ├── 📄 requirements.txt             # Python依赖包列表
│   ├── 📄 build.sh                     # C程序自动构建脚本
│   ├── 📄 CMakeLists.txt              # CMake构建配置文件
│   ├── 📄 .gitignore                  # Git忽略文件配置
│   └── 📄 LICENSE                     # 项目许可证文件
│
├── 📁 src/ (源代码目录)
│   ├── 🔧 C语言核心模块
│   │   ├── 📄 main.c                  # 主程序入口，菜单控制逻辑
│   │   ├── 📄 showinfo.c              # 信息显示、表格输出、菜单界面
│   │   ├── 📄 edit_stu.c              # 学生信息增删改功能实现
│   │   ├── 📄 search.c                # 多种搜索算法实现
│   │   ├── 📄 sort.c                  # 排序算法实现(按成绩、学号等)
│   │   └── 📄 sqlite.c                # SQLite数据库操作接口
│   │
│   ├── 🌐 Python Web应用
│   │   ├── 📄 app.py                  # Flask主应用程序
│   │   │                              #   - 路由处理 (/, /add, /edit, /delete, /search)
│   │   │                              #   - 数据库操作封装
│   │   │                              #   - 多种搜索方式实现
│   │   │                              #   - PyEcharts图表生成
│   │   │                              #   - RESTful API接口
│   │   └── 📄 caldata.py              # 数据分析和统计脚本
│   │                                  #   - Pandas数据处理
│   │                                  #   - 成绩统计分析
│
├── 📁 include/ (C语言头文件)
│   └── 📄 functions.h                 # 所有函数声明和结构体定义
│                                      #   - struct student 学生信息结构
│                                      #   - 数据库操作函数声明
│                                      #   - 工具函数声明
│
├── 📁 templates/ (Web前端模板)
│   ├── 📄 base.html                   # 基础模板 (导航栏、样式、脚本)
│   ├── 📄 index.html                  # 主页学生列表展示
│   │                                  #   - 响应式表格设计
│   │                                  #   - 多种搜索功能界面
│   │                                  #   - 增删改查操作按钮
│   ├── 📄 add_student.html            # 添加学生信息表单
│   ├── 📄 edit_student.html           # 编辑学生信息表单
│   ├── 📄 advanced_search.html        # 高级搜索多条件筛选
│   └── 📄 analytics.html              # 数据分析可视化页面
│                                      #   - PyEcharts交互式图表
│                                      #   - 统计卡片展示
│                                      #   - 成绩分布分析
│
├── 📁 data/ (数据存储目录)
│   └── 📄 student.db                  # SQLite数据库文件
│                                      #   - student表：学生基本信息和成绩
│                                      #   - 自动创建索引优化查询
│
├── 📁 build/ (编译输出目录)
│   ├── 📄 studentarrangement          # 编译后的C可执行文件
│   ├── 📄 Makefile                    # CMake生成的构建文件
│   └── 📁 CMakeFiles/                 # CMake缓存和临时文件
│
├── 📁 venv/ (Python虚拟环境)
│   ├── 📁 bin/                        # Python解释器和脚本
│   ├── 📁 lib/                        # 安装的Python包
│   │   └── 📁 python3.12/site-packages/
│   │       ├── 📦 flask/              # Web框架
│   │       ├── 📦 pandas/             # 数据分析
│   │       ├── 📦 pyecharts/          # 图表库
│   │       └── 📦 sqlite3/            # 数据库接口
│   └── 📄 pyvenv.cfg                  # 虚拟环境配置
│
└── 📁 docs/ (文档目录) [可选扩展]
    ├── 📄 API文档.md                  # RESTful API接口说明
    ├── 📄 数据库设计.md               # 数据库表结构设计
    ├── 📄 开发指南.md                 # 开发环境搭建指南
    └── 📁 screenshots/                # 项目截图展示
        ├── 🖼️ 主界面.png
        ├── 🖼️ 搜索功能.png
        └── 🖼️ 数据分析.png

═══════════════════════════════════════════════════════════════

📊 技术架构说明：

🔧 后端技术栈：
├── C语言 + GCC编译器        → 核心业务逻辑
├── SQLite3 数据库          → 数据持久化存储  
├── CMake 构建系统          → 跨平台编译管理
└── Shell脚本自动化         → 一键构建部署

🌐 前端技术栈：
├── Python Flask Web框架    → HTTP服务和路由
├── Jinja2 模板引擎         → 动态HTML生成
├── Bootstrap 5 UI框架      → 响应式界面设计
├── Font Awesome 图标库     → 美观图标支持
└── JavaScript + jQuery     → 前端交互逻辑

📈 数据处理：
├── Pandas 数据分析库       → 数据清洗和统计
├── PyEcharts 可视化库      → 交互式图表生成
├── SQLite Python驱动      → 数据库连接操作
└── JSON数据交换格式        → API接口数据传输

═══════════════════════════════════════════════════════════════

🚀 核心功能模块：

📋 C语言核心功能：
├── 🔍 多种搜索方式 (按姓名、学号、成绩、身份证等)
├── 📊 多字段排序 (升序/降序，单科/总分/平均分)
├── ✏️ 完整CRUD操作 (增加、删除、修改、查看)
├── 💾 SQLite数据持久化 (事务处理、数据一致性)
└── 🖥️ 命令行交互界面 (菜单导航、错误处理)

🌐 Python Web功能：
├── 🎨 现代化Web界面 (响应式设计、移动端适配)
├── 🔍 智能搜索系统 (实时搜索、高级筛选)
├── 📊 数据可视化 (柱状图、饼图、折线图)
├── 📈 统计分析功能 (成绩分布、排名统计)
├── 🔌 RESTful API (JSON数据接口)
└── 🛡️ 数据验证保护 (表单验证、SQL注入防护)

═══════════════════════════════════════════════════════════════

📁 文件大小统计 (预估)：
├── 源代码文件：~50KB
├── 数据库文件：~1-10MB (取决于学生数量)
├── Python虚拟环境：~100MB
├── 编译产物：~500KB
└── 项目文档：~5MB

🔗 外部依赖：
├── 系统依赖：GCC, CMake, Python3, SQLite3
├── Python包：Flask, Pandas, PyEcharts
└── 前端库：Bootstrap, Font Awesome (CDN)
```  
  

## 🛠️ 技术栈

  

### 后端 (C 语言)

- **编译器**: GCC

- **构建工具**: CMake

- **数据库**: SQLite3

- **功能**: 核心业务逻辑、数据管理

  

### 前端 (Python)

- **框架**: Flask

- **数据处理**: Pandas

- **图表库**: PyEcharts

- **UI 框架**: Bootstrap 5

- **图标**: Font Awesome

  

## 📋 功能特性

  

### C 语言核心功能

1. **学生信息管理**

   - ✅ 添加学生信息

   - ✅ 修改学生信息  

   - ✅ 删除学生信息

   - ✅ 查看所有学生

  

2. **查询功能**

   - ✅ 按学号查找

   - ✅ 按姓名查找

   - ✅ 模糊搜索

  

3. **排序功能**

   - ✅ 按学号排序

   - ✅ 按成绩排序

   - ✅ 按姓名排序

  

4. **数据持久化**

   - ✅ SQLite 数据库存储

   - ✅ 程序退出时自动保存

  

### Python Web 功能

1. **现代化界面**

   - ✅ 响应式设计

   - ✅ 美观的表格展示

   - ✅ 友好的用户交互

  

2. **数据可视化**

   - ✅ 成绩分布图表

   - ✅ 各科平均分对比

   - ✅ 学生成绩趋势分析

   - ✅ 交互式图表展示

  

3. **统计分析**

   - ✅ 总人数统计

   - ✅ 各科平均分、最高分、最低分

   - ✅ 成绩分布统计

  

## 🔧 安装和使用

  

### 环境要求

- Linux/Unix 系统

- GCC 编译器

- CMake (版本 >= 3.10)

- Python 3.x

- SQLite3 开发库

  

### 1. 克隆项目

```bash

git clone https://github.com/Eric-jiang-1127/student_arrangement.git

cd student_arrangement

```

  

### 2. 安装系统依赖

#### Ubuntu/Debian

```shell
sudo apt-get update

sudo apt-get install build-essential cmake libsqlite3-dev python3 python3-pip

# CentOS/RHEL

sudo yum install gcc cmake sqlite-devel python3 python3-pip

```



  

### 3. 编译 C 程序

```shell
# 使用自动构建脚本

chmod +x build.sh
./build.sh  

# 或手动编译

mkdir build && cd build
cmake ..
make
cd ..
```



### 4. 设置 Python 环境

```shell
# 创建虚拟环境

python3 -m venv venv
 
# 激活虚拟环境

source venv/bin/activate

# 安装依赖包

pip install -r requirements.txt

```

  

### 5. 运行程序

  

运行 C 语言版本 (命令行界面)

  

```shell

./build/studentarrangement

```

  
  

运行 Python Web 版本

```shell
# 确保虚拟环境已激活

source venv/bin/activate

# 启动 Web 服务

python src/app.py

# 在浏览器中访问 http://localhost:5000
```

  

## 🎯 使用指南

  

### C 语言命令行版本

  

**启动程序**

```bash

./build/studentarrangement

```

  


  

### **主菜单功能总览**

  

#### **一、控制台程序（C 语言版本）**

  

程序启动后显示文本菜单，通过数字键选择功能：

1. 运行程序后会显示主菜单
2. 输入数字选择相应功能：
    - `1` - 添加学生信息
    - `2` - 查找学生信息
    - `3` - 修改学生信息
    - `4` - 删除学生信息
    - `5` - 排序学生信息
    - `6` - 显示所有学生信息
    - `0` - 退出系统

  

#### **二、Python Web 版本（Flask 框架）**

  

1. 启动 Web 服务后，在浏览器访问 [http://localhost:5000](vscode-file://vscode-app/d:/MyApps/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)
2. 主页显示所有学生信息列表
3. 使用搜索框按姓名或学号搜索学生
4. 点击"添加学生"按钮添加新学生
5. 点击编辑/删除按钮管理学生信息
6. 访问"数据分析"页面查看统计图表

  
## 📊 数据格式

### 学生信息结构

```C
struct student {

    char no[15];           // 学号

    char name[20];         // 姓名

    struct {

        int year;          // 出生年份

        int month;         // 出生月份

        int day;           // 出生日期

    } birthday;

    char id[25];           // 身份证号

    double chinese;        // 语文成绩

    double math;           // 数学成绩

    double english;        // 英语成绩

};
```



### SQLite 数据库表结构

``` sql
CREATE TABLE student (

    no TEXT PRIMARY KEY,    -- 学号，主键

    name TEXT NOT NULL,     -- 姓名，非空

    year INTEGER,           -- 出生年份

    month INTEGER,          -- 出生月份  

    day INTEGER,            -- 出生日期

    id TEXT,                -- 身份证号

    chinese REAL,           -- 语文成绩

    math REAL,              -- 数学成绩

    english REAL            -- 英语成绩

);
```

**索引优化**

-- 为常用查询字段创建索引

```sql
CREATE INDEX idx_name ON student(name);

CREATE INDEX idx_score ON student(chinese, math, english);
```


### API 接口文档

|方法|路径|功能|参数|
|---|---|---|---|
|GET|`/`|主页，显示学生列表|-|
|GET|`/add`|添加学生页面|-|
|POST|`/add`|提交新学生信息|表单数据|
|GET|`/edit/<no>`|编辑学生页面|学号|
|POST|`/edit/<no>`|更新学生信息|学号，表单数据|
|GET|`/delete/<no>`|删除学生|学号|
|GET|`/search`|搜索学生|query, type|
|GET|`/analytics`|数据分析页面|-|
|GET|`/api/students`|获取学生数据API|-|

## 📈 数据可视化功能

### 图表类型

1. **柱状图**：各科平均分对比
2. **饼图**：成绩分布统计（优秀、良好、及格、不及格）
3. **折线图**：学生成绩趋势分析
4. **散点图**：科目间成绩相关性分析

### 统计指标

- 总学生数量
- 各科平均分、最高分、最低分
- 成绩分布情况
- 排名统计

## 🧪 测试数据

系统内置测试数据：

- 学生1：李明 (202501001) - 语文89 数学91 英语87
- 学生2：高亮 (202501002) - 语文78 数学92 英语67
- 学生3：江之涵 (202501003) - 语文100 数学100 英语100


## 🔄 版本更新日志

### v2.0.0 (当前版本)

- ✅ 新增 Python Flask Web 前端
- ✅ 集成 PyEcharts 数据可视化
- ✅ 实现响应式 Web 界面
- ✅ 添加 RESTful API 接口
- ✅ 完善数据库操作

### v1.0.0 (基础版本)

- ✅ C 语言命令行界面
- ✅ 基本增删改查功能
- ✅ SQLite 数据库支持
- ✅ 排序和搜索功能


## 🚧 开发计划

### 短期计划 (1-2个月)

- <input disabled="" type="checkbox"> 添加用户登录认证
- <input disabled="" type="checkbox"> 实现数据导入导出功能
- <input disabled="" type="checkbox"> 优化移动端显示效果
- <input disabled="" type="checkbox"> 添加数据备份恢复功能

### 中期计划 (3-6个月)

- <input disabled="" type="checkbox"> 支持多用户管理
- <input disabled="" type="checkbox"> 添加成绩统计报表
- <input disabled="" type="checkbox"> 实现实时数据同步
- <input disabled="" type="checkbox"> 开发移动端APP

### 长期计划 (6-12个月)

- <input disabled="" type="checkbox"> 微服务架构重构
- <input disabled="" type="checkbox"> 支持分布式部署
- <input disabled="" type="checkbox"> 集成机器学习成绩预测
- <input disabled="" type="checkbox"> 开发完整的教务管理系统

## 🐛 已知问题

1. 中文字符在某些终端可能显示异常
2. Web 界面在低版本浏览器可能兼容性问题
3. 大数据量时查询性能待优化

## 🤝 贡献指南

欢迎贡献代码！请遵循以下步骤：

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交改动 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 代码规范

- C 代码遵循 GNU 编码规范
- Python 代码遵循 PEP 8 规范
- 提交信息使用中文，格式清晰

## 📝 许可证

本项目采用 MIT 许可证 - 查看 LICENSE 文件了解详情

## 👨‍💻 作者信息

- **Eric Jiang** - _项目创建者和主要开发者_
- GitHub: [Eric-jiang-1127](vscode-file://vscode-app/d:/MyApps/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)
- Email: [eric.jiang@example.com](vscode-file://vscode-app/d:/MyApps/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)

## 🙏 致谢

### 开源技术支持

- [Flask](vscode-file://vscode-app/d:/MyApps/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) - Python Web 框架
- [PyEcharts](vscode-file://vscode-app/d:/MyApps/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) - Python 数据可视化库
- [Bootstrap](vscode-file://vscode-app/d:/MyApps/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) - 前端 UI 框架
- [SQLite](vscode-file://vscode-app/d:/MyApps/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) - 嵌入式数据库
- [CMake](vscode-file://vscode-app/d:/MyApps/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) - 跨平台构建工具

### 特别感谢

- 指导老师的悉心指导
- 同学们的测试反馈
- 开源社区的技术支持

---

⭐ 如果这个项目对您有帮助，请给它一个星标！

📧 有任何问题或建议，欢迎提交 Issue 或发送邮件！



  

