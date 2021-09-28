from PIL import Image
from pylab import *

im = array(Image.open("D:\code\pycharm python\MachineLearn\pic\\01.jpg"))
imshow(im)

x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

plot(x, y, 'r*')

plot(x[:2], y[:2])

print('please click 3 points')
x = ginput(3)
print('your clicked:', x)

title('plotting : "emoire.jpg"')

axis("off")




im1 = array(Image.open("D:\code\pycharm python\MachineLearn\pic\\01.jpg").convert('L'))
figure()
gray()
contour(im1, origin='image')
axis('equal')
axis('off')

figure()
hist(im1.flatten(), 128)

show()