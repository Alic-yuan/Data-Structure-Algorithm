from typing import  Optional

class Node:

    def __init__(self, data:int, next=None):
        self.data = data
        self._next = next

#单链表反转
def reverse(head:Node) -> Optional[Node]:
    reverse_head = None
    current = head
    while current:
        reverse_head, reverse_head._next, current = current, reverse_head, current._next
    return reverse_head


#检测环
def has_cycle(head:Node) -> bool:
    slow, fast = head, head
    while fast and fast._next:
        slow = slow._next
        fast = fast._next._next
        if slow == fast:
            return True
    return False


#有序链表合并
def merge_sorted_list(l1:Node, l2:Node) -> Optional[Node]:
    if l1 and l2:
        p1, p2 = l1, l2
        link = Node(0)
        link2 = link
        while p1 and p2:
            if p1.data < p2.data:
                link2._next = p1
                p1 = p1._next
            else:
                link2._next = p2
                p2 = p2._next
            link2 = link2._next
        link2._next = p1 if p1 else p2
        return link._next
    return l1 or l2



#删除倒数第n个节点。假设n大于0
def remove_nth_from_end(head:Node, n:int) -> Optional[Node]:
    fast = head
    count = 0
    while fast and count < n:
        fast = fast._next
        count += 1
    if not fast and count < n:
        return head
    if not fast and count == n:
        return head._next

    slow = head
    while fast._next:
        slow, fast = slow._next, fast._next
    slow._next = slow._next._next
    return slow


#找到中间节点
def find_middle_node(head:Node) -> Optional[Node]:
    slow, fast = head, head
    fast = fast._next if fast else None
    while fast and fast._next:
        slow, fast = slow._next, fast._next._next
    return slow


def print_all(head:Node):
    nums = []
    current = head
    while current:
        nums.append(current.data)
        current = current._next
    print("->".join(str(num) for num in nums))

if __name__ == '__main__':
    pass