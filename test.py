import numpy as np 

def isok(state):
	if np.sum(state) != 45*9:
		return False 
	if (np.sum(state, axis=0)==9).sum()!=9 or (np.sum(state, axis=1)==9).sum()!=9:
		return False
	for i in range(0, 7, 3):
		for j in range(0, 7, 3):
			t = np.unique(state[i:i+3, j:j+3])
			if len(t)!=10:
				return False 
	return True 


def shudu(old_state):
	print('dive in to  loop')
	'''输入old_state 输出new_state'''
	if isok(old_state):
		print(old_state)
		return True

	# print(old_state)
	xs, ys = np.where(old_state==0)

	for x, y in zip(xs, ys):
		print(x,y)
		values = set(np.arange(1,10)) - set(old_state[x,:]) - set(old_state[:,y])
		nine = set(np.unique(old_state[x//3:x//3+3, y//3:y//3 + 3]))# - {0}
		values = values - nine 
		# values = np.unique(values)
		for v in values:
			old_state[x,y] = v  # old -> new state
			# print(x,y,v,values)
			if shudu(old_state): # if 为真 则成功
				return True
			old_state[x,y] = 0
		return False
	return False



s = np.loadtxt('tmp.txt')
s = s.astype(np.int8)
if shudu(s):
	print(s)
