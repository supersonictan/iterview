//
// Created by TanZhen on 2017/8/14.
//




#include <cstring>

/*1. 你有两个用链表代表的整数，其中每个节点包含一个数字。
 * 数字存储按照在原来整数中相反的顺序，使得第一个数字位于链表的开头。
 * 写出一个函数将两个整数相加，用链表形式返回和。*/
struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };
ListNode *addLists(ListNode *l1, ListNode *l2) {
    // write your code here
    if (l1 == NULL) { return l2;}
    if (l2 == NULL) { return l1;}
    int c= 0;
    int t= 0;
    ListNode *head = new ListNode(0);
    ListNode *p = head;
    while (l1!=NULL&&l2!= NULL)
    {
        t = l1->val+l2->val + c;
        c = t/10;
        t = t%10;
        p->next = new ListNode(t);
        p = p->next;
        l1 = l1->next;
        l2 = l2->next;
    }
    while (l1 != NULL&&l2==NULL)
    {
        t = l1->val + c;
        c = t/10;
        t = t%10;
        p->next = new ListNode(t);
        p = p->next;
        l1 = l1->next;
    }
    while (l2 != NULL&&l1==NULL)
    {
        t = l2->val + c;
        c = t/10;
        t = t%10;
        p->next = new ListNode(t);
        p = p->next;
        l2 = l2->next;
    }
    if (c != 0)
    {
        p->next = new ListNode(c);
    }
    return head->next;
}






int main(){

}
