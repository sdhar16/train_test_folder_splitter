import os
import shutil
import sys
import argparse
import numpy as np
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--testdir","-test",help="Test directory")
    parser.add_argument("--traindir","-train",help="Train directory")
    parser.add_argument("--sourcedir","-src",help="Source directory")
    parser.add_argument("--testsize","-testsize",help="Testing size  0<=size<=1")
    args = parser.parse_args()
    test_src = args.testdir
    train_src= args.traindir
    source = args.sourcedir
    testsize = float(args.testsize)
    dirs = os.listdir(source)
    for d in dirs:
        for f in os.listdir(os.path.join(source,d)):
            if(np.random.rand(1)<=testsize):
                if(not os.path.exists(os.path.join(test_src,d))):
                    os.mkdir(os.path.join(test_src,d))
                shutil.copy(os.path.join(source,d,f),os.path.join(test_src,d,f))
            else:
                if(not os.path.exists(os.path.join(train_src,d))):
                    os.mkdir(os.path.join(train_src,d))
                shutil.copy(os.path.join(source,d,f),os.path.join(train_src,d,f))


