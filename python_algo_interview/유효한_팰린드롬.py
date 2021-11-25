# # 유효한 팰린드롬
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         strs = []
        
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
                
#         while len(strs) > 1:
#             if strs.pop(0) != strs.pop():
#                 return False
#         return True

# 데크 자료형
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         strs : Deque = collections.deque()
            
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
                
#         while len(strs) > 1:
#             if strs.popleft() != strs.pop():
#                 return False
        
#         return True