# 反转链表 (Reverse Linked List)

## 基本信息

- 题目来源：美团-后端开发、字节跳动-客户端开发、滴滴-算法工程师
- 难度级别：简单
- 相关标签：链表、双指针

## 出现次数统计

- 总次数：4次（美团2次、字节跳动1次、滴滴1次）

## 题目描述

给你单链表的头节点 `head` ，请你反转链表，并返回反转后的链表。

示例 1：
```
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
```

示例 2：
```
输入：head = [1,2]
输出：[2,1]
```

示例 3：
```
输入：head = []
输出：[]
```

## 解题思路

1. **双指针法**：使用两个指针 `prev` 和 `curr` 分别指向当前节点的前一个节点和当前节点。遍历链表时，将 `curr.next` 指向 `prev`，然后更新 `prev` 和 `curr`。时间复杂度 O(n)，空间复杂度 O(1)。

2. **递归法**：通过递归将链表分为两部分，反转后半部分，然后将前半部分连接到反转后的后半部分。时间复杂度 O(n)，空间复杂度 O(n)（递归栈）。

## 代码实现

### 双指针法（推荐）

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head):
    prev = None
    curr = head

    while curr:
        # 保存下一个节点
        next_node = curr.next
        # 反转指向
        curr.next = prev
        # 更新指针
        prev = curr
        curr = next_node

    return prev
```

### 递归法

```python
def reverseList(head):
    # 递归终止条件
    if not head or not head.next:
        return head

    # 反转后面的链表
    reversed_head = reverseList(head.next)
    # 将当前节点接到反转后链表的尾部
    head.next.next = head
    # 避免循环
    head.next = None

    return reversed_head
```

## 总结

反转链表是链表操作中的基础题目，考察了对链表指针的理解和操作能力。双指针法由于其常量级空间复杂度通常是面试中的首选解法。
