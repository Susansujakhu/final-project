from PIL import Image
import glob
import os

out_dir = 'E:/Hospital data/pngFormat/'
cnt = 0
for img in glob.glob('E:/Hospital data/bmpFormat/*.bmp'):
    Image.open(img).resize((300,300)).save(os.path.join(out_dir, str(cnt) + '_hosp.png'))
    cnt += 1