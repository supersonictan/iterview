#include <stdio.h>
 
const int LENGTH = 50;
const int WIDTH=10;

int main()
{
   /* 我的第一个 C 程序 */
   printf("====================2017年8月8日\n");
   printf("Length*width=%d\n", LENGTH*WIDTH);
   int a = 250;
   int* ptr;
   ptr = &a;
   printf("&a=%d,ptr=%d\n",&a, ptr);

   double balance[5] = {1000.0, 2.0, 3.4, 7.0, 50.0};




   printf("====================2017年8月6日\n");
   printf("Hello, World! \n");
   printf("int size is:%lu",sizeof(int));   
   return 0;
}
