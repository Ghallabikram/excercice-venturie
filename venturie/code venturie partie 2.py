from IPython import display
from PIL import Image
from PIL import ImageDraw
img =Image.open('./image.PNG')
I1=ImageDraw.Draw(img)
I1.text((320, 214),"D1=200m", fill=(255, 0, 0))
I1.text((373, 330),"V1="+str(V1),fill=(255,0,0))
I1.text((1246, 239),"alpha="+str(alpha),fill=(255,0,0))
I1.text((773, 287),"L="+str(L),fill=(255,0,0))
I1.text((1230, 256),"V2="+str(V2),fill=(255,0,0))
img.save("./image.PNG")
img.save("./result.PNG")
display.Image("./result.PNG")
