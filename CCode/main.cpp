#include <assert.h>
#include <cstring>
#include <string>
#include <iostream>
#include <vector>
#include <list>

using namespace std;
/*
 * 1. 实现strcpy函数
 * 2. 实现strlen
 * 3. 写String的成员函数
 * */

/*1 实现strcpy函数*/
char* strcpy(char*strDest, const char*strSrc)
{
    assert((strDest!=NULL) && (strSrc !=NULL));
    char* address = strDest;
    while( (*strDest++ = *strSrc++) !='\0' )
        NULL;//while体里面不做任何操作，就用了NULL;

    return address ;
}

/*2 实现strlen*/
int my_strlen(const char* strSrc) {
    if (strSrc == NULL) return 0;

    int resLen = 0;
    while ((*strSrc++) != '\0') {
        resLen ++;
    }
    return resLen;
}

/*3 String的成员函数*/
class String
{
public:
        String(const char *str = NULL); // 通用构造函数
        String(const String &another); // 拷贝构造函数
        ~String(); // 析构函数
        //& operater = (const String &rhs); // 赋值函数
private:
        char* m_data; // 用于保存字符串

};
//通用构造函数
String::String(const char*str)
{
    char* m_data;
    if ( str == NULL ) // strlen在参数为NULL时会抛异常才会有这步判断
    {
        m_data = new char[1] ;
        m_data[0] ='\0' ;
    }
    else
    {
        m_data = new char[strlen(str) +1];
        strcpy(m_data, str);
    }
}
//拷贝构造函数
String::String(const String &another)
{
    char* m_data;
    m_data = new char[strlen(another.m_data) +1];
    strcpy(m_data, another.m_data);
}



int main()
{
    vector<int> v ;
    list<int> l;

    v.reserve(2);
    v.push_back(123);
    v.push_back(345);
    for (int i = 0; i < 100; ++i) {
        v.push_back(i);
        l.push_back(i);
    }

    for (vector<int>::iterator vi = v.begin(); vi != v.end()  ; vi++) {
        cout << *vi;
    }
}