import pickle
import numpy as np

model = pickle.load(open('D:/AIthon/12_Bit-Lords_3-main/analysis.pkl', 'rb'))
dummy = np.array([1,60,2014,7,20,2014,7,20,2014,8,1,34165,76871.25,2.25,0,3503,19461.76])

value = model.predict(dummy.reshape(1,-1))
print(value[0])