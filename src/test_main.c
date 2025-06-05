#include <stdio.h>
#include "functions.h"

struct student studentinfo[100] = {
    {"202501001", "李明", {2005, 3, 1}, "101110200503010123", 89, 91, 87},
    {"202501002", "高亮", {2025, 8, 31}, "352101200508310910", 78, 92, 67}};
int rcount = 2;

int main()
{
    searchinfo();
}