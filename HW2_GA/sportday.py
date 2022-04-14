from scipy.io import loadmat

x = loadmat('HR1.mat')
print(x['dep'])
print(x['sex'])
