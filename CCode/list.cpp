#include <cstring>
#include <vector>
#include <cstdlib>


using namespace std;

/*
 * 1.链表求和
 * 2.链表翻转
 * 3.判断链表是否有环
 * 4.两个链表交叉点
 * 5.两个链表合并:1->3->8->11->15->null，2->null， 返回 1->2->3->8->11->15->null
 * 6.链表排序nlgn
 * 7.排序K个链表
 * 8.返回链表中环的起始位置
 * 9.判断单向链表是否回文
 * */




struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };

int getLength(ListNode* n);
ListNode *mergeList(ListNode *head1, ListNode *head2) ;

//1.两个链表求和
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

//2.链表翻转
ListNode *reverse(ListNode *head) {
    //给出一个链表1->2->3->null，这个翻转后的链表为3->2->1->null
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
        if(fast == slow) {return true;}
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

//5. 将两个排序链表合并为一个新的排序链表
ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
    //1->3->8->11->15->null，2->null， 返回 1->2->3->8->11->15->null
    ListNode *pnew,*phead = l1;
    if(l1 == NULL)  { return l2; }
    else if(l2 == NULL) { return l1; }
    else {
        if(l1->val <= l2->val) {
            phead = pnew = l1;
            l1 = l1->next;
        } else {
            phead = pnew = l2;
            l2 = l2->next;
        }
        while(l1!=NULL && l2!=NULL) {
            if(l1->val <= l2->val) {
                pnew->next = l1;
                l1 = l1->next;
                pnew = pnew->next;
            } else {
                pnew->next = l2;
                l2 = l2->next;
                pnew = pnew->next;
            }
        }
        if(l1!=NULL && l2==NULL) { pnew->next = l1; }
        if(l2!=NULL && l1==NULL) { pnew->next = l2; }
        return phead;
    }
}

//6. 在 O(n log n) 时间复杂度和常数级的空间复杂度下给链表排序。
ListNode *sortList(ListNode *head) {
    if(head == NULL || head->next == NULL) return head;

    ListNode *fast = head, *slow = head, *temp = head;
    while(fast != NULL && fast->next != NULL) {
        temp = slow;
        slow = slow->next;
        fast = fast->next->next;
    }
    temp->next = NULL;
    return mergeList(sortList(head), sortList(slow));
}
ListNode *mergeList(ListNode *head1, ListNode *head2) {
    if(!head1) return head2;
    if(!head2) return head1;

    ListNode newHead(0);
    ListNode *temp = &newHead;
    while(head1 && head2) {
        if (head1->val < head2->val) {
            temp->next = head1;
            head1 = head1->next;
        } else {
            temp->next = head2;
            head2 = head2->next;
        }
        temp = temp->next;
    }
    if(head1 != NULL) { temp->next = head1; }
    else if(head2 != NULL) { temp->next = head2; }

    return newHead.next;
}

//7. 排序K个链表。[2->4->null,null,-1->null]，返回 -1->2->4->null
ListNode *mergeKLists(std::vector<ListNode *> &lists) {
    if (lists.size() == 0) {return NULL;}

    while (lists.size() > 1) {
        std::vector<ListNode *> tmpVec;
        for (int i = 0; i+1 < lists.size(); i+=2) {
            ListNode* mergeList = mergeTwoLists(lists[i], lists[i+1]);
            tmpVec.push_back(mergeList);
        }
        if (lists.size()%2 == 1){
            tmpVec.push_back(lists[lists.size()-1]);
        }
        lists = tmpVec;
    }
    return lists[0];
}

/*8.返回链表中环的起始位置*/
ListNode *detectCycle(ListNode *head) {
    ListNode *fast=head, *slow = head;
    if (head == NULL) {return NULL;}

    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) break;
    }
    if(fast == NULL||fast->next ==NULL)
        return NULL;
    fast = head;
    while (fast != slow) {
        slow = slow->next;
        fast = fast->next;
    }
    return fast;
}

/*9.判断单向链表是否回文*/
bool isPalindrome(ListNode* head) {
    ListNode *next = head;
    ListNode *now = head;
    ListNode *pre = NULL;
    int lenth = 0;
    if(head == NULL || head->next == NULL)
        return true;
    //取得长度
    while(next != NULL) {
        next = next->next;
        lenth++;
    }
    //遍历到中间，并逆置,最后next指向后半段
    for(int i = 0; i < (lenth / 2); i++) {
        next = now->next;
        now->next = pre;
        pre = now;
        now = next;
    }
    if((lenth % 2) == 1)
        next = next->next;
    //两个指针开始向两头移动，取值比较
    while(next  && pre ) {
        if(next->val != pre->val)
            return false;
        next = next->next;
        pre = pre->next;
    }
    return true;//比较中没有发现不同值，则为回文链表
}

/*10.两个链表相加，数的低位在链表尾部*/
ListNode * addLists2(ListNode * l1, ListNode * l2) {
    if (!l1 && !l2) return NULL;
    int len1 = getLength(l1), len2 = getLength(l2);
    if (len1 < len2) swap(l1, l2);
    int diff = abs(len1 - len2);
    ListNode* vhead = new ListNode(0);
    ListNode* cur = vhead, *combo = vhead;
    while (diff--) {
        cur->next = new ListNode(l1->val);
        cur = cur->next;
        if (cur->val != 9) combo = cur;//如果是9combo还指向最高的0
        l1 = l1->next;
    }
    while (l1) {
        int val = l1->val + l2->val;
        if (val > 9) {//处理进位
            val %= 10;
            combo->val++;
            combo = combo->next;//当前位计算完了应该下一位,必须有eg:399
            while (combo) {//可能当前已经是9了
                combo->val = 0;
                combo = combo->next;
            }
        }
        cur->next = new ListNode(val);
        cur = cur->next;
        if (cur->val != 9) combo = cur;
        l1 = l1->next, l2 = l2->next;
    }
    ListNode* head = vhead;
    if (!vhead->val) {
        head = vhead->next;
        delete(vhead);
    }
    return head;
}


int main(){
    addTwoNumbers(NULL,NULL);
    reverse(NULL);
}
