from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

BG = Image.open("myfont/bg.png")
sizeOfSheet = BG.width
gap, _ = 0, 0
allowedChars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.-?!() 1234567890'

def writee(char):
    global gap, _
    if char == '\n':
        pass
    else:
        char.lower()
        cases = Image.open("myfont/%s.png" % char)
        BG.paste(cases, (gap, _))
        size = cases.width
        gap += size
        del cases

def letterwrite(word):
    global gap, _
    if gap > sizeOfSheet - 95 * (len(word)):
        gap = 0
        _ += 200
    for letter in word:
        if letter in allowedChars:
            if letter.islower():
                pass
            elif letter.isupper():
                letter = letter.lower()
                letter += 'upper'
            elif letter == '.':
                letter = "fullstop"
            elif letter == '!':
                letter = 'exclamation'
            elif letter == '?':
                letter = 'question'
            elif letter == ',':
                letter = 'comma'
            elif letter == '(':
                letter = 'braketop'
            elif letter == ')':
                letter = 'braketcl'
            elif letter == '-':
                letter = 'hiphen'
            writee(letter)

def worddd(Input):
    wordlist = Input.split(' ')
    for i in wordlist:
        letterwrite(i)
        writee('space')

if __name__ == '__main__':
    try:
        with open('..\project_image\\text-to-handwritten\\textinput.txt', 'r') as file:
            data = file.read().replace('\n', '')
        l = len(data)
        nn = len(data) // 900
        chunks, chunk_size = len(data), len(data) // (nn + 1)
        p = [data[i:i + chunk_size] for i in range(0, chunks, chunk_size)]

        for i in range(0, len(p)):
            worddd(p[i])
            writee('\n')
            BG.save('..\project_image\\text-to-handwritten\%dhandwritten.png' % i)
            BG1 = Image.open("myfont/bg.png")
            BG = BG1
            gap = 0
            _ = 0
    except ValueError as E:
        print("{}\nTry again".format(E))


output_pdf = '..\project_image\\text-to-handwritten\image_handwritten.pdf'
text_list = []  # List to store the text content

# Assuming 'p' is the list of text chunks
for i, chunk in enumerate(p):
    # Split the chunk into lines with a maximum line length of 80 characters
    lines = [chunk[j:j+80] for j in range(0, len(chunk), 80)]
    text_list.extend(lines + ['\n'])

# Create a PDF
c = canvas.Canvas(output_pdf, pagesize=letter)

# Set font properties
font_name = "Helvetica"
font_size = 12
c.setFont(font_name, font_size)

# Set initial y-coordinate
y_coordinate = 700

# Loop through each text chunk and add it to the PDF
for text_chunk in text_list:
    c.drawString(50, y_coordinate, text_chunk)  # Adjust the coordinates as needed
    y_coordinate -= font_size+8  # Move to the next line

# Save the PDF
c.save()

