# 14 minutes and 6 trials
def isValid(s):
	stack=[0]
	for x in s:
		if x=='}' and stack[len(stack)-1]=='{':
			stack.pop(len(stack)-1)
		elif x==']' and stack[len(stack)-1]=='[':
			stack.pop(len(stack)-1)
		elif x==')' and stack[len(stack)-1]=='(':
			stack.pop(len(stack)-1)
		else:
			stack.append(x)
	if len(stack)==1:
		print(True)
		return True
	else:
		print(False)
		return False
s = "()[]{}"
isValid(s)