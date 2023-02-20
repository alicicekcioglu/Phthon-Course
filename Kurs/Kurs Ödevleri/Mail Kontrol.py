def e_posta_kontrol():
    girdi = input("mail: ")
    while not (("."in girdi) and ("@" in girdi)):
        print("Hatalı e-posta adresi.")
        girdi = input("mail: ")
    else:
        print("E posta doğru.")

e_posta_kontrol()