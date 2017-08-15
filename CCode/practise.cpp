#include <cstring>
/*
 * 1.链表求和
 * 2.链表翻转
 * 3.判断链表是否有环
 * 4.两个链表交叉点
 * */



/*1.
 * 链表求和
 * 你有两个用链表代表的整数，其中每个节点包含一个数字。
 * 数字存储按照在原来整数中相反的顺序，使得第一个数字位于链表的开头。
 * 写出一个函数将两个整数相加，用链表形式返回和。
 * 3->1->5->null 和 5->9->2->null，返回 8->0->8->null
 * */
struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };

int getLength(ListNode* n);

ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    ListNode *sumList = new ListNode(-1);
    ListNode *cur = sumList;
    int carry = 0;
    while (l1 != NULL || l2 != NULL || carry != 0) {
        int l1val = l1 == NULL ? 0 : l1->val;
        int l2val = l2 == NULL ? 0 : l2->val;
        int sum = l1val + l2val + carry;
        carry = sum / 10; //进位
        sum %= 10;
        cur->next = new ListNode(sum);
        cur = cur->next;
        l1 = l1 == NULL ? NULL : l1->next;
        l2 = l2 == NULL ? NULL : l2->next;
    }
    ListNode *t = sumList->next;
    delete sumList;
    return t;
}

/*
 * 2.链表翻转
 * 给出一个链表1->2->3->null，这个翻转后的链表为3->2->1->null
 * */
ListNode *reverse(ListNode *head) {
    ListNode *now = head;
    ListNode *next = NULL;
    ListNode *pre = NULL;

    while (now != NULL) {
        next = now->next;//因为head要指向NULL,所以先保存下个节点
        now->next = pre;//head指向NULL或者之前的节点
        pre = now;
        now = next;
    }
    return pre;
}
/*3.判断链表是否有环*/
bool hasCycle(ListNode *head) {
    ListNode *fast = head, *slow = head;

    while(fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;

        if(fast == slow) {
            return true;
        }
    }
    return false;
}

/*4.两个链表交叉点*/
ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    if (!headA||!headB) return NULL;
    int la = getLength(headA), lb = getLength(headB);
    if (la > lb) {
        for(int i=0; i<(la-lb); i++) headA = headA->next;
    } else{
        for(int i=0; i<(lb-la); i++) headB = headB->next;
    }

    while (headA && headB && headA!=headB) {
        headA = headA->next;
        headB = headB->next;
    }
    return (headA && headB)?headA:NULL;
}
int getLength(ListNode* n){
    int cnt = 0;
    while (n) {
        n = n->next;
        cnt++;
    }
    return cnt;
}


int main(){

}
