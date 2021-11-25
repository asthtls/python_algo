# 문자열 뒤집기

# reverse 함수 사용
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         s.reverse()


# # two point 사용
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
        
#         left, right = 0, len(s)-1
        
#         while left < right:
#             s[left], s[right] = s[right], s[left]
            
#             left += 1
#             right -= 1
        