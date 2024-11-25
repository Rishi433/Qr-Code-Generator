import qrcode 
image = qrcode.make("https://www.facebook.com/profile.php?id=100075952280284&mibextid=ZbWKwL")

image.save("mine.png")