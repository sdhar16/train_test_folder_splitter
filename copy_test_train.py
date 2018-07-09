import os
import shutil
import sys
import argparse
import numpy as np
from random import shuffle
from sklearn.model_selection import train_test_split
if __name__ == '__main__':
    source = 'filtered_faces'
    # testsize = float(args.testsize)
    
    dirs = os.listdir(source)
    data = []
    label = []
    for d in dirs:
        dir_struct = os.listdir(os.path.join(source,d))
        if(len(dir_struct)<5):
            continue
        for i in dir_struct:
            data.append(os.path.join(source,d,i))
            label.append(d)
    X_train,X_test,y_train,y_test = train_test_split(data,label,test_size = 0.2,stratify = label)
    print(os.path.split(os.path.split(X_train[0])[0])[1])
    for i in X_train:
        if(not os.path.exists(os.path.join('train',os.path.split(os.path.split(i)[0])[1]))):
            os.mkdir(os.path.join('train',os.path.split(os.path.split(i)[0])[1]))
        shutil.copy(i,os.path.join('train',os.path.split(os.path.split(i)[0])[1]))
    for i in X_test:
        if(not os.path.exists(os.path.join('val',os.path.split(os.path.split(i)[0])[1]))):
            os.mkdir(os.path.join('val',os.path.split(os.path.split(i)[0])[1]))
        shutil.copy(i,os.path.join('val',os.path.split(os.path.split(i)[0])[1]))
        # for f in dir_struct:
        #     # print(np.random.rand(1))
        #     if(np.random.rand(1)<=testsize):
        #         if(not os.path.exists(os.path.join(test_src,d))):
        #             os.mkdir(os.path.join(test_src,d))
        #         shutil.copy(os.path.join(source,d,f),os.path.join(test_src,d,f))
        #     else:
        #         if(not os.path.exists(os.path.join(train_src,d))):
        #             os.mkdir(os.path.join(train_src,d))
        #         shutil.copy(os.path.join(source,d,f),os.path.join(train_src,d,f))


