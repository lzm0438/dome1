import qrcode

img = qrcode.make('https://cloud.tencent.com/developer/beta/article/1625774')
# img <qrcode.image.pil.PilImage object at 0x1044ed9d0>

with open('test.png', 'wb') as f:
    img.save(f)