#ifndef FUNCTIONS_H
#define FUNCTIONS_H

struct date
{
    int year;
    int month;
    int day;
};

struct student
{
    char no[10];
    char name[20];
    struct date birthday;
    char id[20];
    float chinese;
    float math;
    float english;
}; // define the student structure

extern struct student studentinfo[100]; // 只声明
extern int rcount;                      // 只声明

void showmenu();
void addinfo();
int isExist(char No[]);
void searchinfo();
void modifyinfo();
void deleteinfo();
void sortinfo();
void displayinfo();

#endif