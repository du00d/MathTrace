import os

'''
This code finds all the images and tokens, group their name into two files with the following format.

file1 "./data_file.txt":
    <img0> 0
    <img1> 1
    <img2> 2
    <img3> 3

file2 "./label_file.txt":
    tokenized formula0
    tokenized formula1
    tokenized formula2
    tokenized formula3
    ....

'''


PATH = '/projectnb/dl523/projects/trace_22/data/processed/'
save_to_data = './data_file.txt'
save_to_label = './label_file.txt'


files = []
with open(save_to_data, 'w') as f, open(save_to_label, 'w') as g:
    cnt = 0
    for idx, file in enumerate(os.listdir(PATH)):
        if(file.endswith('.png')):
            print(str(cnt))
            name = file.split('.')[0]
            png = name +'.png'
            token = name + '.token'

            if os.path.exists(PATH+png) and os.path.exists(PATH+token):

                f.writelines(file.split('.')[0]+ '.png '+ str(cnt))
                f.writelines('\n')
                
                with open(PATH + file.split('.')[0]+ '.token') as t:
                    g.writelines(t.readline())
            cnt += 1
                

