#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "functions.h"

int isExist(char No[])
{
    /*函数接口定义：
    在studentinfo数组中查找编号为No的学生，如果该学生存在则返回他在数组中的序号（index），否则返回-1。*/
    for (int i = 0; i < rcount; i++)
    {
        if (strcmp(studentinfo[i].no, No) == 0)
        {
            return i;
        }
    }
    return -1;
}

void input_student(struct student *p)
{
    // 输入单个学生的信息
    scanf("%s %s %d %d %d %s %f %f %f", p->no, p->name, &p->birthday.year, &p->birthday.month, &p->birthday.day, p->id, &p->chinese, &p->math, &p->english);
}

void addinfo()
{
    /*
    函数接口定义：
    接收用户输入的信息，创建结构变量存放学生信息，并将该学生信息加入到数组studentinfo已有学生的末尾。
    步骤如下：
    1.用户输入操作码1, 系统应提示:输入学生数量
    2.用户输入学生数量, 系统应提示:请输入学生编号,姓名,生日（年月日用空格分隔）,身份证,语文,数学,英语 成绩，用空格分隔,一个学生一行
    3.用户按要求输入多个学生后
    3.1 系统检查输入的编号是否重复(调用函数isExist,需要自己实现)
    3.2 添加编号不重复的学生，并统计本次添加的学生数。
    3.3 系统提示:成功添加{xx}条学生信息.
    4.用户输入0 退出系统
    */

    // 为输入的学生分配内存
    printf("输入学生数量\n");
    int size;
    scanf("%d", &size);
    struct student *temp = (struct student *)malloc(size * sizeof(struct student));
    if (temp == NULL)
    {
        printf("内存分配失败\n");
        return;
    }

    // 输入新学生内容
    printf("请输入学生编号 姓名 生日（年月日用空格分隔） 身份证 语文 数学 英语成绩,一个学生一行\n");
    for (int i = 0; i < size; i++)
    {
        input_student(&temp[i]);
    }

    // 将新学生的信息比对并加入数据中
    int count = 0;
    for (int i = 0; i < size; i++)
    {
        if (isExist(temp[i].no) == -1)
        {
            studentinfo[rcount++] = temp[i];
            count++;
        }
    }
    printf("成功添加%d条学生信息.\n", count);
}

void searchinfo()
{
    /*
    函数接口定义：
    接收用户输入的一个编号xxx，如果数组studentinfo中存在该编号，则在新行输出该学生信息，输出格式如下：编号10，姓名20，出生日期YYYY-MM-DD，身份证20，成绩5位保留1位小数，如果不存在，在新行显示“无此人”。*/
    printf("请输入要查询的编号:\n");
    char tempno[10];
    scanf("%s", tempno);
    int ret = isExist(tempno);
    if (ret != -1)
    {
        printstu(studentinfo[ret]);
    }
    else
    {
        printf("无此人\n");
    }
}

void modifyinfo()
{
    /*
    函数接口定义：
    接收用户输入的一个编号xxx，如果studentinfo中存在该编号，则继续读取新的学生信息，输入格式如下

    编号 姓名 生日（年月日用空格分隔） 身份证 语文 数学 英语

    用新的学生信息替换原来的学生信息，（注意编号为学生记录的唯一标识，因此编号不允许修改）如果不存在该编号，则输出一行提示信息：
    编号为xxx的学生信息不存在,修改失败.

    步骤如下：
    1.用户输入操作码3, 系统应提示:输入要修改的编号
    2.系统接收用户输入的编号，并查找对应的数组下标（isExist函数）
    3.找到对应的编号
    3.1.系统应提示：输入学生信息:编号 姓名 生日（年月日用空格分隔） 身份证 语文 数学 英语
    3.2.系统接收用户输入，判断两次输入的编号是否一致
    3.2.1. 如果一致，修改该学生信息，系统提示：成功修改.
    3.2.2. 如果不一致，系统提示：编号不允许修改,修改失败.
    4. 没有找到对应编号，系统应提示：编号为xxx的学生信息不存在,修改失败.
    5.用户输入0 退出系统
    */
    printf("输入要修改的编号\n");
    char tempno[20];
    scanf("%s", tempno);
    int index = isExist(tempno);
    if (index == -1)
    {
        printf("编号为%s的学生信息不存在,修改失败.\n", tempno);
    }
    else
    {
        printf("输入学生信息:编号 姓名 生日（年月日用空格分隔） 身份证 语文 数学 英语\n");
        struct student new;
        input_student(&new);
        if (strcmp(tempno, new.no)!=0)
        {
            printf("编号不允许修改,修改失败.\n");
        }
        else
        {
            studentinfo[index] = new;
            printf("成功修改.\n");
        }
    }
}

void deleteinfo()
{
    /*函数接口定义：
    接收用户输入的一个编号xxx，如果数组studentinfo中存在该编号，删除该学生信息，系统提示：
    删除学生信息成功.
    如果不存在该编号，则输出一行：
    编号为xxx的学生信息不存在,删除失败.

    步骤如下：
    1.用户输入操作码3, 系统应提示:输入要删除的编号
    2.系统接收用户输入的编号，并查找对应的学生信息
    2.1.找到对应学生信息，系统删除该学生信息，更新studentinfo，系统提示：删除学生信息成功.
    2.2 没有找到对应学生信息，系统提示：编号为xxx的学生信息不存在,删除失败.
    3.用户输入0 退出系统
    */
    printf("输入要删除的编号\n");
    char tempno[20];
    scanf("%s", tempno);
    int index = isExist(tempno);
    if (index == -1)
    {
        printf("编号为%s的学生信息不存在,删除失败.\n", tempno);
    }
    else
    {
        for (int i = index; i < rcount-1; i++)
        {
            studentinfo[i] = studentinfo[i+1];
        }
        rcount--;
        printf("删除学生信息成功.\n");
    }
}