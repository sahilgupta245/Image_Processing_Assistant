# import the following libraries
# will convert the image to text string
import pytesseract	

# adds image processing capabilities
from PIL import Image	

# converts the text to speech
import pyttsx3		

#translates into the mentioned language
from googletrans import Translator	

# opening an image from the source path
imagepath=input("Drag and drop the Image ->")
print(imagepath)
img = Image.open(imagepath)	

# describes image format in the output
print(img)						
# path where the tesseract module is installed
pytesseract.pytesseract.tesseract_cmd ='D:\PROJECTS\mini_project_Image_manipulation\Project_image\Project_image\Tesseract-OCR\tesseract.exe'
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)
# write text in a text file and save it to source path
with open('abc.txt',mode ='w') as file:	
	
				file.write(result)
				print(result)
				
p = Translator()					
# translates the text into german language
k = p.translate(result,dest='german')	
print(k)
engine = pyttsx3.init()

# an audio will be played which speaks the test if pyttsx3 recognizes it
engine.say(k)							
engine.runAndWait()
