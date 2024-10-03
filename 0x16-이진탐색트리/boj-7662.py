# from collections import deque

# t = int(input())


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#         self.num = 1


# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self, value):
#         if self.root is None:
#             self.root = Node(value)
#         else:
#             self.cur_node = self.root
#             while True:
#                 if value == self.cur_node.value:
#                     self.cur_node.num += 1
#                     break
#                 elif value < self.cur_node.value:
#                     if self.cur_node.left is None:
#                         self.cur_node.left = Node(value)
#                         break
#                     else:
#                         self.cur_node = self.cur_node.left
#                 else:
#                     if self.cur_node.right is None:
#                         self.cur_node.right = Node(value)
#                         break

#                     else:
#                         self.cur_node = self.cur_node.right

#     def delete_min(self):
#         if self.root is None:
#             return

#         self.parent_node = self.root
#         self.cur_node = self.root
#         while self.cur_node.left:
#             self.parent_node = self.cur_node
#             self.cur_node = self.cur_node.left

#         if self.cur_node.num > 1:  # 중복이 있으면 개수를 한 개 줄여주면 됨
#             self.cur_node.num -= 1
#             return

#         if self.parent_node == self.cur_node:  # 최솟값이 Root 노드인 경우
#             if self.cur_node.right is not None:
#                 self.root = self.cur_node.right
#             else:
#                 self.root = None
#         else:
#             if self.cur_node.right is not None:
#                 # 오른쪽 노드에서 가장 작은 값 찾기
#                 self.change_parent_node = self.cur_node.right
#                 self.change_node = self.cur_node.right

#                 while self.change_node.left is not None:
#                     self.change_parent_node = self.change_node
#                     self.change_node = self.change_node.left

#                 self.cur_node.value = self.change_node.value
#                 self.cur_node.num = self.change_node.num

#                 if self.change_node.right is not None:
#                     self.change_parent_node.left = self.change_node.right
#                 else:
#                     self.change_parent_node.left = None
#             else:
#                 self.parent_node.left = None

#     def delete_max(self):
#         if self.root is None:
#             return
#         self.parent_node = self.root
#         self.cur_node = self.root
#         while self.cur_node.right:
#             self.parent_node = self.cur_node
#             self.cur_node = self.cur_node.right
#         if self.cur_node.num > 1:  # 중복이 있으면 개수를 한 개 줄여주면 됨
#             self.cur_node.num -= 1
#             return
#         if self.parent_node == self.cur_node:  # 최댓값이 Root 노드인 경우
#             if self.cur_node.left is not None:
#                 self.root = self.cur_node.left
#             else:
#                 self.root = None
#         else:
#             if self.cur_node.left is not None:  # 왼쪽 노드에서 최댓값 찾기
#                 self.change_node = self.cur_node.left
#                 self.change_parent_node = self.cur_node.left

#                 while self.change_node.right is not None:
#                     self.change_parent_node = self.change_node
#                     self.change_node = self.change_node.right

#                 self.cur_node.value = self.change_node.value
#                 self.cur_node.num = self.change_node.num

#                 self.change_parent_node.right = None
#             else:
#                 self.parent_node.right = None

#     def check_empty(self):
#         if self.root is None:
#             return True
#         else:
#             return False

#     def find_min(self):
#         self.cur_node = self.root
#         while self.cur_node.left is not None:
#             self.cur_node = self.cur_node.left

#         return self.cur_node.value

#     def find_max(self):
#         self.cur_node = self.root
#         while self.cur_node.right is not None:
#             self.cur_node = self.cur_node.right
#         return self.cur_node.value


# for _ in range(t):
#     k = int(input())
#     bst = BST()
#     for i in range(k):
#         action, num = input().split()
#         num = int(num)
#         if action == "I":
#             bst.insert(num)
#         elif action == "D":
#             if num == -1:
#                 bst.delete_min()
#             elif num == 1:
#                 bst.delete_max()

#     if bst.check_empty():
#         print("EMPTY")
#     else:
#         print(bst.find_max(), bst.find_min())
