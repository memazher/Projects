from PIL import Image
import os
 
Input_dir = './dataset/Md.Mazher/'
Out_dir = 'dataset/Md.Mazher/'
a = os.listdir(Input_dir)
 
for i in a:
    print(i)
    I = Image.open(Input_dir+i)
    L = I.convert('L')
    L.save(Out_dir+i)