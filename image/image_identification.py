#!/usr/bin/env python
# -*- coding: utf-8 -*-

#sudo pip install pytesseract
#sudo apt-get install tesseract-ocr
#https://www.cnblogs.com/chenbjin/p/4147564.html


from PIL import Image
import pytesseract
text = pytesseract.image_to_string(Image.open('/home/qwt/Downloads/test1.png'),lang='chi_sim')
print text