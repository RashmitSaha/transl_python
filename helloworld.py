from translate import Translator
trans_fr=Translator(to_lang="fr")
trans_it=Translator(to_lang="it")
trans_ru=Translator(to_lang="ru")
original_file=open("hello world.txt",'r')
translated_file=open("translated_hello world.txt",'w')
original_text=original_file.read()
translated_text=trans_ru.translate(original_text)
translated_file.write(translated_text)
original_file.close()
translated_file.close()

with open("translated_hello world.txt",'r') as f:
    text=f.read()
    print(text)
    
