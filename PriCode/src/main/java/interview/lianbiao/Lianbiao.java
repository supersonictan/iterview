package interview.lianbiao;

/**
 * Created by Supersonic on 2016/7/24.
 */
public class Lianbiao {


    /**
     * 判断是否有环
     */
    public boolean hasCircle(Node head){
        if(head == null) return false;
        Node fast = head;
        Node slow = head;
        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if(slow == fast){
                return true;
            }
        }
        return false;
    }
    /**
     *链表环起点
     */
    public Node getCircleStart(Node head){
        if(head == null) return null;
        Node fast = head;
        Node slow = head;
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if(slow == fast) {break; }
        }
        fast = head;
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next;
            if(fast == slow){ return fast;}
        }
        return null;
    }

    /**
     * 两个链表的交点
     */
    public Node getIntersection(Node headA,Node headB){
        if(headA == null || headB == null) {return null;}
        int aLength = 0,bLength = 0; //计算长度
        Node a = headA, b = headB;

        if(aLength > bLength){
            for(int i=0; i<(aLength-bLength); i++){
                a = a.next;
            }
        }else if(bLength > aLength){
            for(int i=0; i<(bLength-aLength); i++){
                b = b.next;
            }
        }
        while (a != null && b != null){
            if(a == b) { return a;}
            else {
                a = a.next;
                b = b.next;
            }
        }
        return null;
    }

    /**
     * 链表反转
     */
    public Node reverseList(Node head){
        if(head == null || head.next == null) { return head;}

        Node current = head;
        Node next = null;
        Node newHead = null;
        while(current != null){
            next = current.next; //将current的next节点保存,cause current节点变了就找不到next了
            current.next = newHead; //将 1节点的next指向null
            newHead = current; //将newHead引用指向1节点，为了2节点指向1
            current = next;
        }
        return newHead;
    }

    /**
     * 合并两个有序链表
     */
    public Node mergeList(Node headA, Node headB){
        if(headA == null && headB == null) { return null; }
        if(headA == null) { return headB; }
        if(headB == null) {return headA; }

        Node newHead;
        Node current;
        if(headA.data < headB.data){
            newHead = headA;
            current = newHead;
            headA = headA.next;
        } else {
            newHead = headB;
            current = newHead;
            headB = headB.next;
        }
        while (headA != null && headB != null){
            if(headA.data < headB.data){
                current.next = headA;
                current = current.next;
                headA = headA.next;
            } else {
                current.next = headB;
                current = current.next;
                headB = headB.next;
            }
        }
        if(headA != null) {current.next = headA;}
        if(headB != null) {current.next = headB;}
        return newHead;
    }
}
class Node {
    //注：此处的两个成员变量权限不能为private，因为private的权限是仅对本类访问。
    int data; //数据域
    Node next;//指针域

    public Node(int data) {
        this.data = data;
    }

}
