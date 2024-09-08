from translate import Translator
print("TRANSLATE IN THE FOLLOWING LANGUAGES: ")
print("1.French")
print("2.Spanish")
print("3.Russian")
print("4.Italian")
print("5.Portuguese")
print("6.German")
print("7.Japanese")
print("8.Korean")
choice=int(input("Enter a choice: "))
if choice==1:
    translator=Translator(to_lang="fr")
elif choice==2:
    translator=Translator(to_lang="es")
elif choice==3:
    translator=Translator(to_lang="ru")
elif choice==4:
    translator=Translator(to_lang="it")
elif choice==5:
    translator=Translator(to_lang="pt")
elif choice==6:
    translator=Translator(to_lang="de")
elif choice==7:
	translator=Translator(to_lang="ja")
elif choice==8:
	translator=Translator(to_lang="ko")
else:
    print("Exiting since you haven't made any concrete choice.")

original_file=open("poem.txt",'r')
translated_file=open("translated_poem.txt",'w')
original_text=original_file.read()
translated_text=translator.translate(original_text)
translated_file.write(translated_text)
original_file.close()
translated_file.close()

with open("translated_poem.txt",'r') as f:
    text=f.read()
    print(text)
