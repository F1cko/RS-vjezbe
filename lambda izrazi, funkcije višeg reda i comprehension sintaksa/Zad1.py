kvadriraj = lambda x: x ** 2
zbroji_pa_kvadriraj = lambda a, b: (a + b) ** 2
kvadriraj_duljinu = lambda niz: len(niz) ** 2
pomnozi_i_potenciraj = lambda x, y: (y * 5) ** x
paran_broj = lambda x: True if x % 2 == 0 else None
print(kvadriraj(5))   
print(zbroji_pa_kvadriraj(3, 2)) 
print(pomnozi_i_potenciraj(2, 3)) 
print(kvadriraj_duljinu([1,2,3]))  
print(paran_broj(10))  
    
