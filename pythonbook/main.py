
import pyttsx3
import PyPDF2
book = open('new.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
page = pdfreader.getPage(7)
text = page.extractText()
print(text)
play = pyttsx3.init()
play.say(text)
play.runAndWait()
