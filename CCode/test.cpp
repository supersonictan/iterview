#include <cstring>

struct ListNode{
    int val;
    ListNode *next;
    ListNode(int x):val(x),next(NULL){}
};




ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    ListNode *sumList = new ListNode(0);
    ListNode *cur = sumList;

    int carry = 0;
    while (l1!=NULL || l2!=NULL || carry !=0) {
        int l1val = l1 == NULL ? 0 : l1->val;
        int l2val = l2 == NULL?0:l2->val;
        int sum = l1val + l2val + carry;
        carry = sum/10;
        sum %= 10;

        cur->next = new ListNode(sum);
        cur = cur ->next;
        l1 = l1==NULL?NULL:l1->next;
        l2 = l2==NULL?NULL:l2->next;
    }
    ListNode *t = sumList->next;
    delete sumList;
    return t;
}

bool hasCycle(ListNode *head) {
    ListNode* fast = head, *slow = head;
    while (fast != NULL && fast->next !=NULL){
        slow=slow->next;
        fast = fast->next->next;
        if (slow==fast) return true;
    }
    return false;
}