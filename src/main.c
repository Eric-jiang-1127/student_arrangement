#include <stdio.h>
#include <sqlite3.h>
#include "functions.h"

struct student studentinfo[100] = {
    {"202501001", "李明", {2005, 3, 1}, "101110200503010123", 89, 91, 87},
    {"202501002", "高亮", {2025, 8, 31}, "352101200508310910", 78, 92, 67},
    {"202501003", "江之涵", {2005, 11, 27}, "421302200511283310", 100, 100, 100}};
int rcount = 3;

int main()
{
    // 程序启动时可选：初始化数据库表结构
    sqlite3 *db;
    sqlite3_open("data/student.db", &db);
    const char *sql = "CREATE TABLE IF NOT EXISTS student ("
                      "no TEXT PRIMARY KEY,"
                      "name TEXT,"
                      "year INT,"
                      "month INT,"
                      "day INT,"
                      "id TEXT,"
                      "chinese REAL,"
                      "math REAL,"
                      "english REAL"
                      ");";
    sqlite3_exec(db, sql, 0, 0, 0);
    sqlite3_close(db);

    // 主程序
    int key;
    do
    {
        showmenu(); // 显示菜单
        scanf("%d", &key);
        if (key == 1)
            addinfo(); // 增加学生
        else if (key == 2)
            searchinfo(); // 查找学生
        else if (key == 3)
            modifyinfo(); // 修改
        else if (key == 4)
            deleteinfo(); // 删除
        else if (key == 5)
            sortinfo(); // 排序
        else if (key == 6)
            displayinfo(); // 打印
        else if (key == 0)
        {
            sync_to_db(); // 退出前同步数据到数据库
            printf("退出系统成功.\n");
            break;
        }
        else
            printf("选择有错,请重新选择正确的功能编号.\n");
    } while (1);

    return 0;
}