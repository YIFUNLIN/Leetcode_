# 113 交大資財所: 利用Linked List 實作 大數運算
class Node:
    """定義單向鏈結串列的節點"""
    def __init__(self, digit):
        self.digit = digit  # 存單個數字
        self.next = None    # 指向下一個節點

class BigNumber:
    """用鏈結串列來表示大數字"""
    def __init__(self):
        self.head = None  # 初始化為空鏈結串列 (self.head 指向整個鏈結串列的第一個節點（也就是最低位數）)

def BN_new():
    """對應 BN_new()，建立一個新的鏈結串列"""
    return BigNumber()

def BN_insert(big_number, value):
    """將數字插入到鏈結串列的頭部（因為最低位在前）"""
    new_node = Node(value)   # 創建新節點
    new_node.next = big_number.head  # 新節點的 next 指向舊的 head
    big_number.head = new_node      # 更新 head，讓它指向新節點
    
def BN_add(A, B, C):
    """兩個 BigNumber 相加，把結果存入 C"""
    carry = 0  # 進位變數
    p1, p2 = A.head, B.head  # 指向 A 和 B 的起始節點（最低位）

    while p1 or p2 or carry:
        sum_val = carry  # 先加上進位值
        if p1:  # 如果 A 還有數字
            sum_val += p1.digit
            p1 = p1.next  # 移動到下一個數字
        if p2:  # 如果 B 還有數字
            sum_val += p2.digit
            p2 = p2.next  # 移動到下一個數字

        carry = sum_val // 10  # 計算進位
        BN_insert(C, sum_val % 10)  # 只存個位數

def BN_print(big_number):
    """印出整個數字（從鏈結串列轉成字串）"""
    if not big_number.head:  # 如果鏈結串列是空的，則輸出 0
        print("0")
        return
    current = big_number.head  # 從頭開始遍歷
    result = []
    while current:
        result.append(str(current.digit))  # 把數字轉成字串存入陣列
        current = current.next  # 移動到下一個節點
    print("".join(result))  # 連接所有數字並輸出

# ------------------------測試程式--------------------
A = BN_new()
B = BN_new()
C = BN_new()

# A 存入 987654321
for i in range(9, 0, -1):  # 9, 8, ..., 1
    BN_insert(A, i)

# B 存入 88888888
for _ in range(8):  # 8 個 8
    BN_insert(B, 8)

# 執行 A + B
BN_add(A, B, C)

# 印出計算結果
BN_print(C)
