import operator
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        operands = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}

        for t in tokens:
            if t in operands:
                num1 = float(stack.pop())
                num2 = float(stack.pop())
                res = int(operands[t](num2,num1))
                stack.append(str(res))
            else:
                stack.append(t)

        return int(float(stack[-1]))