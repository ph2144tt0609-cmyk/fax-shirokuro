from PIL import Image, ImageDraw
def icon(n):
    im = Image.new("RGB", (n, n), (31, 111, 139))
    d = ImageDraw.Draw(im)
    m = n * 0.22
    d.rounded_rectangle([m, n*0.16, n-m, n*0.84], radius=n*0.05, fill=(255, 255, 255))
    for i, w in enumerate([0.56, 0.48, 0.52, 0.36]):
        y = n*(0.30 + i*0.12)
        d.rectangle([n*0.30, y, n*(0.30+w*0.72), y+n*0.045], fill=(20, 24, 27))
    return im
for s in (180, 192, 512):
    icon(s).save(f"icon-{s}.png")
