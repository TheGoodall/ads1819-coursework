
def good_expression(expression):

    class pair():
        def __init__(self):
            self.left_op = 0
            self.right_op = 0
            self.min_op = 0
    
    stack = [pair()]

    queue = []

    priority = {"+":1, "*":2}


    


    

    for index, char in enumerate(expression):
        if char in [str(i) for i in range(10)]:
            pass

        elif char == "+" or char == "*":
            value = priority[char]
            if stack[-1].min_op == 0:
                stack[-1].min_op = value
            elif value < stack[-1].min_op:
                stack[-1].min_op = value
            
        elif char == "(":
            stack.append(pair())
            if index-1 >= 0:
                stack[-1].left_op = priority.get(expression[index-1], 0) 

            
        elif char == ")":
            p = stack.pop()
            if index+1 < len(expression):
                p.right_op = priority.get(expression[index+1], 0) # returns value or 0
            
            # at this point p has been generated and is a pair of brackets with a left_op, min_op and right_op
            
            if p.left_op == 0 and p.right_op == 0:
                return False
            if p.min_op == 0:
                return False
            if not (p.min_op < p.left_op or p.min_op < p.right_op):
                return False


    return True


            


            





#####################################################
def testq3():
    assert good_expression("1+2+3+4") 
    assert not good_expression("(1+2+3+4)") 
    assert good_expression("(1+2)*3+4") 
    assert not good_expression("((1+2))*3+4") 
    assert good_expression("1+2*3+4") 
    assert not good_expression("1+(2*3)+4") 
    assert good_expression("1*2+3+4")  
    assert not good_expression("1*2+(3+4)") 
    print ("all original tests passed")
    
#####################################################
    assert good_expression('1*(2+3)+4')  # Good expression
    assert not good_expression('1+(2+3)+4')  # Bad expression
    assert not good_expression('1+(2*3)+4')  # Bad expression
    assert not good_expression("1*2+(3+4)")  # Bad expression
    assert not good_expression('((1+2))*3+4')  # Bad expression
    assert not good_expression('(1+2+3+4)')  # Bad expression
    assert good_expression('1+2+3+4')  # Good expression
    assert not good_expression('((2+3)*3)*6')  # Bad expression
    assert good_expression('3+(4+5)*(6+7)')  # Good expression
    assert good_expression('3*(4+5)*(6+7)')  # Good expression
    assert not good_expression('3+(4+5)+(6+7)')  # Bad expression
    assert not good_expression('1*(2*3)*(4*5)')  # Bad expression
    assert not good_expression('(1+((2*3)*4)+5)+(6)*7*8+9)')  # Bad expression
    assert not good_expression('1+(2+(2+(4+2)*(4*4+2))*5)')  # Bad expression
    assert not good_expression('(2)*2')  # Bad expression
    assert good_expression("1+2+3+4")  # Good expression
    assert not good_expression("(1+2+3+4)")  # Bad expression
    assert good_expression("(1+2)*3+4")  # Good expression
    assert not good_expression("((1+2))*3+4")  # Bad expression
    assert good_expression("1+2*3+4")  # Good expression
    assert not good_expression("1+(2*3)+4")  # Bad expression
    assert good_expression("1*2+3+4")  # Good expression
    assert not good_expression("1*2+(3+4)")  # Bad expression
    assert not good_expression('1+(2*(3+(4*(5+(6*(7+(8*(9+(9+1)))))))))')  # Bad expression
    assert good_expression('1*(2+3)*(4+5)*(6+7)')  # Bad expression
    assert not good_expression('1*(2*3)')  # Bad expression
    print('All new tests passed!!')
testq3()