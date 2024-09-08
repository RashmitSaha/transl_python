from translate import Translator
lang=input("Enter language you want to translate: ")
translator=Translator(to_lang=lang)
original_file=open("Input file.txt",'w')
text=input("Enter the text: ")
original_file.write(text)
translated_file=open("Translated file.txt",'w')
translated_text=translator.translate(text)
translated_file.write(translated_text)
translated_file.close()
original_file.close()

with open("Translated file.txt",'r') as f:
	output=f.read()
	print(output)
