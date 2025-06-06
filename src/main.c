#include <stdio.h>
#include "functions.h"

struct student studentinfo[100] = {
    {"202501001", "李明", {2005, 3, 1}, "101110200503010123", 89, 91, 87},
    {"202501002", "高亮", {2025, 8, 31}, "352101200508310910", 78, 92, 67},
    {"202501003", "江之涵", {2005, 11, 27}, "421302200511283310", 100, 100, 100}};
int rcount = 3;

int main()
{
    int key;
    do
    {
        showmenu(); // 函数1:显示菜单
        scanf("%d", &key);
        if (key == 1)
            addinfo(); // 函数2:增加学生
        else if (key == 2)
            searchinfo(); // 函数3:查找学生（按编号）
        else if (key == 3)
            modifyinfo(); // #函数4:修改
        else if (key == 4)
            deleteinfo(); // 函数5:删除
        else if (key == 5)
            sortinfo(); // 函数6:排序
        else if (key == 6)
            displayinfo(); // 函数7:打印
        else if (key == 0)
        {
            printf("退出系统成功.\n");
            break;
        }
        else
            printf("选择有错,请重新选择正确的功能编号.\n");
    } while (1);
    return 0;
}