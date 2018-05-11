import numpy as np
class Perceptron(object):
	"""
	eta:学习率
	n_iter:权重向量的训练次数
	w_：神经分叉权重向量
	errors_:用于记录神经元判断出错次数
	"""
	def __int__(self,eta=0.01,n_iter=10):
		self.eta=eta
		self.n_iter=n_iter
		pass

	def fit(self,x,y):
		"""
		输入训练数据，培养神经元，x输入样本向量，y对应样本分类
		x:shape[n_samples,n_features]
		x:[[1,2,3],[4,5,6]]
		n_samples:2
		n_features:3
		y:[1,-1]		
		"""
		"""
		初始化权重向量为0
		加一是应为前面算法提到的W0，也就是步调函数的阈值
				"""
		slef.w_=np.zero(1+x.shape[1])
		self.errors_=[]

		for _ in range(self.n_iter):
			errors_=0
			"""
			x:[[1,2,3],[4,5,6]]
			y:[1,-1]
			zip(x,y)=[[1,2,3,1],[4,5,6,-1]]
			"""
			for xi, target in zip(x,y):
				"""
				update=eta*(y+y')
				"""
				update=self.eta*(target-slef.predict(xi))
				"""
				xi是一个向量
				update*xi等价：
				ΔW(1)=x[1]*update,ΔW(2)=x[2]*update,ΔW(3)=x[3]*update,
				"""
				self.w_[1:]+=update*xi
				self.w_[0]+=update

				error +=int(update!=0.0)
				self.errors_.append(error)
				pass
			pass

	def net_input(self,x):
		"""
		z=w0*1+w!*x1+...+Wn*xn
		"""
		return np.dot(x,self.w_[1:]) + self.w_[0]
		pass

	def predict(self,x):
		return np.where(self.net_input(x)>=0.0,1,-1)





		

