#include <stdio.h>
#include<string.h>
#include "functions.h"

typedef int (*SearchCond)(struct student *, void *);

int gen_isExist(SearchCond cond, void *value)
{
    /*函数接口定义：
    cond: 按功能查找的函数抽象
    value: 查找值
    在studentinfo数组中按功能查找对应的学生，如果该学生存在则返回他在数组中的序号（index），否则返回-1。*/
    for (int i = 0; i < rcount; i++)
    {
        if (cond(&studentinfo[i], value))
        {
            return i;
        }
    }
    return -1;
}

int cond_by_no(struct student *stu, void *value)
{
    return strcmp(stu->no, (char *)value) == 0;
}
int cond_by_name(struct student *stu, void *value)
{
    return strcmp(stu->name, (char *)value) == 0;
}
int cond_by_id(struct student *stu, void *value)
{
    return strcmp(stu->id, (char *)value) == 0;
}
int cond_by_chinese(struct student *stu, void *value)
{
    return stu->chinese == *(float *)value;
}
int cond_by_math(struct student *stu, void *value)
{
    return stu->math == *(float *)value;
}
int cond_by_english(struct student *stu, void *value)
{
    return stu->english == *(float *)value;
}

void searchinfo()
{
    /*
    函数接口定义：
    支持多种索引方式查找学生信息。
    1. 用户选择查找方式（1.编号 2.姓名 3.身份证 4.语文成绩 5.数学成绩 6.英语成绩）。
    2. 输入对应的查找内容。
    3. 系统查找并输出结果，若找到则输出学生信息，否则输出“无此人”。
    */

    printf("请选择查找方式：1.编号 2.姓名 3.身份证 4.语文成绩 5.数学成绩 6.英语成绩\n");
    int op;
    scanf("%d", &op);

    int ret = -1;
    char input[30];
    float score;
    switch (op)
    {
    case 1:
        printf("请输入要查询的编号:\n");
        scanf("%s", input);
        ret = gen_isExist(cond_by_no, input);
        break;
    case 2:
        printf("请输入要查询的姓名:\n");
        scanf("%s", input);
        ret = gen_isExist(cond_by_name, input);
        break;
    case 3:
        printf("请输入要查询的身份证:\n");
        scanf("%s", input);
        ret = gen_isExist(cond_by_id, input);
        break;
    case 4:
        printf("请输入要查询的语文成绩:\n");
        scanf("%f", &score);
        ret = gen_isExist(cond_by_chinese, &score);
        break;
    case 5:
        printf("请输入要查询的数学成绩:\n");
        scanf("%f", &score);
        ret = gen_isExist(cond_by_math, &score);
        break;
    case 6:
        printf("请输入要查询的英语成绩:\n");
        scanf("%f", &score);
        ret = gen_isExist(cond_by_english, &score);
        break;
    default:
        printf("查找方式无效！\n");
        return;
    }

    if (ret != -1)
    {
        printstu(studentinfo[ret]);
    }
    else
    {
        printf("无此人\n");
    }
}