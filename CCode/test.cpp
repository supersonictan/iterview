#include <cstring>
#include <cstdlib>
#include <string>

using namespace std;

struct ListNode{
    int val;
    ListNode *next;
    ListNode(int x):val(x),next(NULL){}
};

int getLength(ListNode* n) {
    if (!n) return 0;
    int len = 0;
    while (n) {
        len++;
        n = n->next;
    }
    return len;
}


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





ListNode * addLists2(ListNode * l1, ListNode * l2) {
    if(!l1 && !l2) return NULL;
    int len_a = getLength(l1), len_b = getLength(l2);
    if (len_a < len_b) swap(l1,l2);
    int diff = abs(len_a - len_b);
    ListNode* vhead = new ListNode(0);
    ListNode* cur = vhead, *combo = vhead;
    while (diff--) {
        cur->next = new ListNode(l1->val);
        cur = cur->next;
        l1 = l1->next;
        if (cur->val != 9) combo = cur;
    }
    while (l1) {
        int val = l1->val + l2->val;
        if (val>9){
            val %= 10;
            combo->val++;
            combo = combo->next;
            while (combo) {
                combo->val = 0;
                combo = combo->next;
            }
        }
        cur->next = new ListNode(val);
        cur = cur->next;
        l1 = l1->next, l2 = l2->next;
        if (cur->val !=9) combo = cur;
    }
    ListNode* head = vhead;
    if (!vhead->val){
        head = vhead->next;
        delete(vhead);
    }
    return head;
}

