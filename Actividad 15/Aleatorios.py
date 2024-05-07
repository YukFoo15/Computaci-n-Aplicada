import os

MAX = 5

def genale ():
    nums = []
    for i in range (MAX):
        nums.append(random.randint(100,1000))
    return nums

def sumalistas (l1, l2):
    ls = []
    for i in range (MAX):
        ls.append(l1[i] + l2[i])
    return ls


os.system("clear")
nums1 = genale()
nums2 = genale()
lsuma = (nums1, nums2)

print(f"Lista de los {len(nums1)} números obtenidos: \n {nums1}")
print(f"Segunda lista de los {len(nums2)} números obtenidos: \n {nums2}")
print(f"Suma de {len(lsuma)} términos de las listas: \n {lsuma}")