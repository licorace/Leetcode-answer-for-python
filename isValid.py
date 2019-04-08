#这个方法十分暴力，但是很简单，对于正确的来说，每一次都能去掉一个括号，最后就成了空，就拿举例来说，先去掉[],再去掉(),最后去掉{}
class Solution:
    def isValid(self, s: str) -> bool:
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''  #这一步是判断s是否为空，是的话返回True，不是的话返回False

if __name__ == '__main__':
    s = Solution()
    print(s.isValid('{([])}'))
    
#方法二，用栈的方法
#1.初始化栈 S。
#2.一次处理表达式的每个括号。
#3.如果遇到开括号，我们只需将其推到栈上即可。这意味着我们将稍后处理它，让我们简单地转到前面的 子表达式。
#4.如果我们遇到一个闭括号，那么我们检查栈顶的元素。如果栈顶的元素是一个 相同类型的 左括号，那么我们将它从栈中弹出并继续处理。否则，这意味着表达式无效。
#5.如果到最后我们剩下的栈中仍然有元素，那么这意味着表达式无效。
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else 88
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
