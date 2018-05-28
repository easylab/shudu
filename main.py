import numpy as np 

def isok(state):
	if np.sum(state) != 45*9:
		return False 
	# print(state)
	if (np.sum(state, axis=0)==45).sum()!=9 or (np.sum(state, axis=1)==45).sum()!=9:
		return False
	for i in range(0, 7, 3):
		for j in range(0, 7, 3):
			t = np.unique(state[i:i+3, j:j+3])
			if len(t)!=9 or np.sum(t) != 45:
				return False 

	return True


def shudu(old_state):
	# print('dive into  loop')
	'''输入old_state 输出new_state'''
	if isok(old_state):
		print(old_state)
		return True

	xs, ys = np.where(old_state==0)
	if len(xs) == 0:
		return False

	# print(xs, ys)
	x,y = xs[0], ys[0]

	# print(x,y)

	# possible values
	values = set(np.arange(1,10)) - set(old_state[x,:]) - set(old_state[:,y])
	xgrid, ygrid = x//3, y//3

	nine = set(np.unique(old_state[3*xgrid:3*xgrid+3, 3*ygrid:3*ygrid + 3]))# - {0}
	values = values - nine 

	for v in values:
		old_state[x,y] = v  # old -> new state
		if shudu(old_state): # if 为真 则找到一组合适的表
			return True
	
	old_state[x,y] = 0
	return False


s = np.loadtxt('tmp.txt')
s = s.astype(np.int8)
if shudu(s):
	# print(s)
	pass
else:
	print("False")
