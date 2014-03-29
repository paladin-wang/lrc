af=open("lrc.lrc",'r')
bf=open("lrc.txt",'w')
a=af.readlines()
for i in a:
    bf.write(i[10:])
    print i[10:]
af.close()
bf.close()

