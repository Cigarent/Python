from math import factorial

def answer(seq):
    if len(seq) <= 2:
        return 1
    else:
        return helper(seq)
    # your code here

def helper(seq):
    if len(seq) < 2:
    	return len(seq)
    else:
         left = [x for x in seq if x>seq[0]]
	 right = [x for x in seq if x<seq[0]]
	 return helper(left)*helper(right)*combination((len(left)+1)*len(right),len(right))

def combination(n,k):
    numerator=factorial(n)
    denominator=(factorial(k)*factorial(n-k))
    answer=numerator/denominator
    return answer
