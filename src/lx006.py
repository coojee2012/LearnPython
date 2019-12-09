txts = ["今天天气真好","气温18度",'适合旅游']
with open(r"writeAndWrite.txt",'w',encoding="utf8") as f:
    f.write("你好\n")
    f.write("北京")
    f.write("我爱北京天安门\n")
    f.writelines(txts)
with open(r"writeAndWrite.txt",'r',encoding="utf8") as f:
    lines = f.readlines()
    lines = [line.rstrip()+" #"+str(index+1)+"\n" for index,line in enumerate(lines)]
with open(r"writeAndWrite.txt",'w',encoding="utf8") as f:
    f.writelines(lines)
