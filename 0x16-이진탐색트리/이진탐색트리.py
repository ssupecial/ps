class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        self.cur_node = self.root
        while True:
            if value < self.cur_node.value:
                if self.cur_node.left is None:
                    self.cur_node.left = Node(value)
                    break
                else:
                    self.cur_node = self.cur_node.left
            else:
                if self.cur_node.right is None:
                    self.cur_node.right = Node(value)
                    break
                else:
                    self.cur_node = self.cur_node.right

    def search(self, value):
        self.cur_node = self.root
        while self.cur_node:
            if value == self.cur_node.value:
                return True
            elif value < self.cur_node.value:
                if self.cur_node.left is None:
                    return False
                else:
                    self.cur_node = self.cur_node.left
            else:
                if self.cur_node.right is None:
                    return False
                else:
                    self.cur_node = self.cur_node.right

    def delete(self, value):
        # 삭제할 노드가 있는지 검사하고 없으면 Fasle 반환
        is_search = self.search(value)
        if is_search is False:
            return False

        self.cur_node = self.root
        self.parent_node = self.root
        while self.cur_node:
            if value == self.cur_node.value:
                break
            elif value < self.cur_node.value:
                self.parent_node = self.cur_node
                self.cur_node = self.cur_node.left
            else:
                self.parent_node = self.cur_node
                self.cur_node = self.cur_node.right

        # 자식 노드가 없을 때
        if self.cur_node.left is None and self.cur_node.right is None:
            if self.cur_node == self.parent_node:
                self.root = None
            elif value < self.parent_node.value:
                self.parent_node.left = None
            else:
                self.parent_node.right = None

        # 자식 노드가 한 개만 있을 때 (Left)
        elif self.cur_node.left is not None and self.cur_node.right is None:
            if value < self.parent_node.value:
                self.parent_node.left = self.cur_node.left
            else:
                self.parent_node.right = self.cur_node.left

        # 자식 노드가 한 개만 있을 떄 (Right)
        elif self.cur_node.left is None and self.cur_node.right is not None:
            if value < self.parent_node.value:
                self.parent_node.left = self.cur_node.right
            else:
                self.parent_node.right = self.cur_node.right

        # 자식 노드가 둘 다 있을 때
        else:
            # 현재 노드보다 큰 것 중에 가장 작은 노드
            self.change_parent_node = self.cur_node.right
            self.change_node = self.cur_node.right
            while self.change_node.left is not None:
                self.change_parent_node = self.change_node
                self.change_node = self.change_node.left

            self.cur_node.value = self.change_node.value
            if self.change_node.right is not None:
                self.change_parent_node.left = self.change_node.right
            else:
                self.change_parent_node.left = None

        return True


arr = [5, 2, 4, 22, 10, 12, 15, 60, 44, 9]
root = Node(30)
bst = BST(root)
for i in arr:
    bst.insert(i)
print(bst.search(22))  # True
print(bst.search(61))  # False
print(bst.search(60))  # True
print(bst.delete(60))  # True
print(bst.search(60))  # False
print(bst.delete(22))  # True
print(bst.delete(44))  # True
print(bst.search(22))  # False
print(bst.search(44))  # False
