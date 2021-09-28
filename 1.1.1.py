from PIL import Image
import os
def get_imlist(path):
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

filelist = get_imlist("D:\code\pycharm python\MachineLearn\pic")

for infile in filelist:
    outfilepath = os.path.splitext(infile)[0]
    if not os.path.exists(outfilepath):
        os.makedirs(outfilepath)
    
    outfile = outfilepath + '\img.jpg'
    if infile != outfile:
        try:
            pil_im = Image.open(infile)
            #pil_im.thumbnail((128,64))
            pil_im = pil_im.crop((100,100,200,200))
            pil_im.save(outfile)
        except IOError:
            print("Can not convert", infile) 
