#include <stdio.h>
#include <string.h>
#include "functions.h"

typedef int (*Compare)(struct student, struct student);

int cmp_no(struct student s1, struct student s2)
{
    return strcmp(s1.no, s2.no) > 0;
}

int cmp_name(struct student s1, struct student s2)
{
    return strcmp(s1.name, s2.name) > 0;
}

int cmp_id(struct student s1, struct student s2)
{
    return strcmp(s1.id, s2.id);
}

int cmp_chinese(struct student s1, struct student s2)
{
    return s1.chinese - s2.chinese > 0;
}

int cmp_math(struct student s1, struct student s2)
{
    return s1.math - s2.math > 0;
}

int cmp_eng(struct student s1, struct student s2)
{
    return s1.english - s2.english > 0;
}

void sort(Compare function)
{
    for (int i = 0; i < rcount - 1; i++)
    {
        for (int j = 0; j < rcount - i - 1; j++)
        {
            if (function(studentinfo[j], studentinfo[j + 1]))
            {
                struct student temp = studentinfo[j];
                studentinfo[j] = studentinfo[j + 1];
                studentinfo[j + 1] = temp;
            }
        }
    }
}

void sortinfo()
{
    /*函数接口定义：
    系统提示：
    输入排序的字段号码:1.编号 2.姓名 3.身份证 4.语文 5.数学 6.英语

    如果输入的字段号码不在1-6之间，则输出一行：
    输入的字段号码有错.
    否则按照相应字段对课程计划进行排序

    步骤如下：
    1.用户输入操作码4, 系统应提示:输入排序的字段号码:1.编号 2.姓名 3.身份证 4.语文 5.数学 6.英语
    2.系统接收用户输入的字段号码，并进行判断
    2.1.字段号码在1-6之间，按照相应字段对学生信息进行排序
    2.2 字段号码不在1-6之间，系统应提示：输入的字段号码有错.
    2.3 排序后，调用displayinfo()，显示排序结果
    3.用户输入0 退出系统*/

    printf("输入排序的字段号码:1.编号 2.姓名 3.身份证 4.语文 5.数学 6.英语\n");
    int choice;

    scanf("%d", &choice);

    Compare p = NULL;
    switch (choice)
    {
    case 1:
        p = cmp_no;
        break;

    case 2:
        p = cmp_name;
        break;
    case 3:
        p = cmp_id;
        break;
    case 4:
        p = cmp_chinese;
        break;
    case 5:
        p = cmp_math;
        break;
    case 6:
        p = cmp_eng;
        break;

    default:
        printf("输入的字段号码有错.\n");
        break;
    }
    if (p != NULL)
    {
        sort(p);
        printf("信息已按指定字段排序。\n");
        displayinfo();
    }
}