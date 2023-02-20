with open("futbolcular.txt","r",encoding="utf-8") as file:
    gs = list()
    fb = list()
    bjk = list()

    for satir in file:
        satir = satir[:-1]
        satir_elemnları = satir.split(",")
        if satir_elemnları[1] == "Fenerbahçe":
            fb.append(satir + "\n")
        elif satir_elemnları[1] == "Galatasaray":
            gs.append(satir + "\n")
        else:
            bjk.append(satir + "\n")
    with open("gs.txt","w",encoding="utf-8")as file1:
        for i in gs:
            file1.write(i)
    with open("fb.txt","w",encoding="utf-8")as file2:
        for i in fb:
            file2.write(i)
    with open("bjk.txt","w",encoding="utf-8")as file3:
        for i in bjk:
            file3.write(i)