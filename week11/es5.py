#spellcheck

fp_text=open("testo.txt", "r")
set_voc=set()
for word in fp_voc:
    set_voc.add(word)
fp_voc.close()
print(set_voc)1
print(set_txt)
fp_text=open("testo.txt", "r")
for line in fp_text:
    for word in line.split():
        set_txt.add(word.strip(!?:.;,))
fp_text.close()

for item in set_txt.difference(set_voc):
    print(item)