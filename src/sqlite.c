#include <stdio.h>
#include "functions.h"
#include<sqlite3.h>

// 数据同步函数：将当前 studentinfo 写入数据库
void sync_to_db()
{
    sqlite3 *db;
    sqlite3_open("data/student.db", &db);

    // 可选：清空表，防止旧数据残留
    sqlite3_exec(db, "DELETE FROM student;", 0, 0, 0);

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

    const char *insert_sql = "INSERT OR REPLACE INTO student "
                             "(no, name, year, month, day, id, chinese, math, english) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);";
    sqlite3_stmt *stmt;
    sqlite3_prepare_v2(db, insert_sql, -1, &stmt, NULL);

    for (int i = 0; i < rcount; i++)
    {
        sqlite3_bind_text(stmt, 1, studentinfo[i].no, -1, SQLITE_STATIC);
        sqlite3_bind_text(stmt, 2, studentinfo[i].name, -1, SQLITE_STATIC);
        sqlite3_bind_int(stmt, 3, studentinfo[i].birthday.year);
        sqlite3_bind_int(stmt, 4, studentinfo[i].birthday.month);
        sqlite3_bind_int(stmt, 5, studentinfo[i].birthday.day);
        sqlite3_bind_text(stmt, 6, studentinfo[i].id, -1, SQLITE_STATIC);
        sqlite3_bind_double(stmt, 7, studentinfo[i].chinese);
        sqlite3_bind_double(stmt, 8, studentinfo[i].math);
        sqlite3_bind_double(stmt, 9, studentinfo[i].english);

        sqlite3_step(stmt);
        sqlite3_reset(stmt);
    }
    sqlite3_finalize(stmt);
    sqlite3_close(db);
}