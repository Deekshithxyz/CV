from PIL import Image
import pytesseract
import re

def replace_chars(text):
 list_of_numbers = re.findall(r'\d+',text)
 result_number = ''.join(list_of_numbers)
 return result_number


file1 = open('output.txt', 'w')
im = Image.open("pan2.jpg")
text = pytesseract.image_to_string(im, lang='eng')
i = text.find('Card')
pan_num = text[(i+5):(i+15)] 
numbers = replace_chars(text)
dob = numbers[4:12]
file1.write(pan_num)
file1.write('\n')
file1.write(dob)
file1.close()


