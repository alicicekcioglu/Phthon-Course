# bir objenin iterable olması için hazır metolar olan __iter()__ ve __next()__ metodlarının mutlaka kullanılması gerekir.

"""
Iterator Oluşturma
iter() metodu kullanılır ve objenin bir sonraki elemanını almak için next() metodu kullanılır.
"""

liste = [1,2,3,4,5]

iterator = iter(liste)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))