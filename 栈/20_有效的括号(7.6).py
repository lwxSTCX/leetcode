class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 如果配对的话，则全部替换为空，然后如果s为空则为true,否则为false
        #python提交 运行时间64ms，内存消耗12.7MB
        while '{}' in s or '()' in s or '[]' in s:
            s=s.replace('{}','')
            s=s.replace('()','')
            s=s.replace('[]','')
        return s == ''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #python提交下面的一起匹配的，超时了
        while '{}' in s or '()' in s or '[]' in s:
            s=s.replace('/\{\}|\(\)|\[\]/g','')
        return s == ''


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #排除一下为( )的情况
        #消耗与第一种相差不大
        while '{}' in s or '()' in s or '[]' in s:
            s=s.replace(' ','')
            s=s.replace('{}','')
            s=s.replace('()','')
            s=s.replace('[]','')
        return s == ''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #这种是先看小括号，再看中括号，再看大括号，因为数学{[()]}合法，而({[]})等等不合法
        #python提交 运行时间56ms，内存消耗12.9MB
        while True:
            m = s.replace('{}','',1).replace('[]','',1).replace('()','',1)
            if m == s: #如果m与是相等，表示未匹配到
                return s == ''
            else: #否则表示匹配到了，赋值给s，进行重新匹配
                 s = m

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #以上均只考虑全括号的情况
        #如果括号合法，那么必然成对存在，否则false
        #python运行时间16ms，内存消耗13MB
        li=list(s)
        n=len(li)
        i=0
        if n==0:
            return True
        if n%2==1:
            return False
        while i<n-1 and li!='':
            #通过对比括号直接的acsii码进行判断，左右括号的ascii码相差1或者2
            if ord(li[i])==ord(li[i+1])-1 or ord(li[i])==ord(li[i+1])-2:
                del li[i:i+2] #然后删除这一部分的括号
                n-=2 #括号字符串的长度减少2
                i-=1 #然后从匹配到的括号的前一个括号继续匹配
            else:
                i+=1 #否则匹配下一个括号
        return not li #返回不是合法的

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #用了栈
        #python 运行时间20ms，内存消耗12.7MB
        if len(s)%2 == 1: #奇数偶数判断
            return False
        d={'(':')','[':']','{':'}'}
        stack=[] #建立空栈
        for char in s:
            if char in s: #左括号先入栈
                stack.append(char)
            else:
                if not stack or d[stack.pop()]!=char: #没入栈就出栈，或者出栈元素不匹配当前元素
                    return False
        return True if not stack else False #没有入栈直接返回False

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return False
        stack=[]
        stack.append(s[0])
        dict = ['()','[]','{}']
        for c in s[1:]:
            stack.append(c)
            if len(stack) == 1:
                continue
            if stack[-2]+stack[-1] in dict:
                stack.pop()
                stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False


#官方答案
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
"""
复杂度分析

时间复杂度：O(n)O(n)，因为我们一次只遍历给定的字符串中的一个字符并在栈上进行 O(1)O(1) 的推入和弹出操作。
空间复杂度：O(n)O(n)，当我们将所有的开括号都推到栈上时以及在最糟糕的情况下，我们最终要把所有括号推到栈上。例如 ((((((((((。
"""

class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False
        return len(stack) == 1
    # python3 解法，运行时间40ms，内存消耗13.5MB


class Solution:
    def isValid(self, s: str) -> bool:
        #python3解法 运行时间44ms,内存消耗13.7MB
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if stack and i in dic:
                if stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return not stack

"""
代码中我们使用了哈希表来判断是否能够形成括号，从而决定进行入栈操作还是出栈操作。

复杂度分析
时间复杂度：O(N)
O(N)。遍历了一遍字符串。
空间复杂度：O(N)
O(N)。最坏情况下，假如输入是(((((((，栈的大小将是输入字符串的长度。
"""











