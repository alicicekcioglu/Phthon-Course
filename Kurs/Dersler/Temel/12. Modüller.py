"""
import math # modülü içe aktarır. Modülün tüm foksiyonları kullanılabilir.
from math import * bu şekilde çekersek fonksiyon öncesinde modül adını yazmaya gerek kalmaz
from math import floor,ceil.... sadece ismi yazılan fonksiyonları çeker
print(dir(math)) # Modülün içerisindekileri gösterir.
print(help(math)) # modülün ne işe yaradığını dösterir.
"""
import math
print(math.factorial(5))