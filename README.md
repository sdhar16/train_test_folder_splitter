The python scripts help in splitting the dataset into traing and testing for the following diretory structure

source/  
-------->/class1  
---------------->data1.jpg  
---------------->data2.jpg  
---------------->data3.jpg  
--------->/class2  
---------------->data1.jpg  
  
into   
  
Train/  
-------->/class1  
---------------->data1.jpg training  
---------------->data2.jpg training  
---------------->data3.jpg training  
--------->/class2  
---------------->data1.jpg training  
  
and  
  
Test/  
-------->/class1  
---------------->data1.jpg testing  
---------------->data2.jpg testing  
---------------->data3.jpg testing  
--------->/class2  
---------------->data1.jpg testing  
  
Use the following flags  
-src SOURCE_FOLDER  
-test TEST_FOLDER  
-train TRAIN_FOLDER  
-testsize TEST_RATIO (between 0 and 1)  