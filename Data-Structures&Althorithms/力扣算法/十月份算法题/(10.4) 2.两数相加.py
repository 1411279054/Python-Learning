class ListNode:
    def __init__(self, item):
        self.val = item
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p,q = l1,l2
        new_ld = ListNode(0)
        pt = new_ld
        carry = 0
        while p != None or q != None:
            a = p.val if p != None else 0
            b = q.val if q != None else 0
            num = (a+b+carry) % 10
            carry = (a+b) // 10
            pt.next = ListNode(num)
            pt = pt.next
            if p != None: p=p.next
            if q != None: q=q.next
        if carry>0:
            pt.next = ListNode(carry)
        return new_ld.next
def main():
    l1 = ListNode(2)
    pt = l1
    pt.next = ListNode(4)
    pt = pt.next
    pt.next = ListNode(3)
    pt = pt.next
    pt.next = None
    l2 = ListNode(5)
    pt2 = l2
    pt2.next = ListNode(6)
    pt2 = pt2.next
    pt2.next = ListNode(4)
    pt2 = pt2.next
    pt2.next = None
    result_pt = Solution().addTwoNumbers(l1,l2)
    while result_pt != None:
        print(result_pt.val,end=" ")
        result_pt = result_pt.next
if __name__ == '__main__':
    main()
