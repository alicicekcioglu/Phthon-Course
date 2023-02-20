boy = float(input("Lütfen boyunuzu metre cinsinden giriniz: "))
kilo = int(input("Lütfen kilonuzu giriniz: "))
bmi = kilo / boy ** 2

if bmi < 18.5:
    print(f"Vücut kitle endeksin: {bmi}\nVücut kitle endeksiniz ideal kilonun altında. Biraz yemek ye :)")
elif bmi >= 18.5 and bmi <= 24.9:
    print(f"Vücut kitle endeksin: {bmi}\nVücut kitle endeksiniz ideal.")
elif bmi >= 25 and bmi <= 29.9:
    print(f"Vücut kitle endeksin: {bmi}\nVücut kitle endeksiniz ideal kilonun üzerinde.")
elif bmi >= 30:
    print(f"Vücut kitle endeksin: {bmi}\nVücut kitle endeksiniz ideal kilonun üzerinde. Diyet yapmayı düşünebilirsin :(.")
