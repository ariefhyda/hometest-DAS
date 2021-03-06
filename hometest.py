# ==========================#
#          -HOME TEST-      #
#         ARIF HIDAYAH      #
#  arifhidayah22@gmail.com  #
# ==========================#

from itertools import permutations
from itertools import combinations_with_replacement 
import numpy as np
import sys

# DASAR PEMIKIRAN
# cari semua peluang kombinasi angka, kemudian setiap peluang angka di lakukan peluang operasi


#Menampung hasil olahan
arrResult=[]
arrTextResult=[]

#fungsi mencari nilai terdekat
def findNearest():
    x = 24 #set deafult nilai patokan
    arr = np.array(arrResult) 
    # hitung selisih array
    difference_array = np.absolute(arr-x)

    # temukan indeks elemen minimum dari array
    index = difference_array.argmin()
    # buka tag komen dibawah ini untuk melihat nilai terdekat dengan 24
    print("Elemen terdekat dengan nilai yang diberikan adalah : ", arr[index])
    print("Hasilnya : ",arrTextResult[index])


#fungsi melakukan operasi
def getMath(math,data):
    text = str(data[0])+str(math[0])+str(data[1])+str(math[1])+str(data[2])+str(math[2])+str(data[3])
    try:
        nilai = eval(text)
    except ZeroDivisionError:
        nilai = 0    
    arrResult.append(nilai)
    arrTextResult.append(text)

    string = text
    string = "("+string[0:3]+")"+string[3:7]
    # #print(string)
    try:
        nilai = eval(string)
    except ZeroDivisionError:
        nilai = 0    
    arrResult.append(nilai)
    arrTextResult.append(string)
    string = "("+string[0:7]+")"+string[7:9]
    #print(string)
    try:
        nilai = eval(string)
    except ZeroDivisionError:
        nilai = 0    
    arrResult.append(nilai)
    arrTextResult.append(string)

    string = text
    string = string[0:2]+"("+string[2:5]+")"+string[5:7]
    #print(string)
    try:
        nilai = eval(string)
    except ZeroDivisionError:
        nilai = 0    
    arrResult.append(nilai)
    arrTextResult.append(string)
    string = "("+string[0:7]+")"+string[7:9]
    #print(string)
    try:
        nilai = eval(string)
    except ZeroDivisionError:
        nilai = 0    
    arrResult.append(nilai)
    arrTextResult.append(string)

    string = text
    string = string[0:2]+"("+string[2:5]+")"+string[5:7]
    #print(string)
    try:
        nilai = eval(string)
    except ZeroDivisionError:
        nilai = 0    
    arrResult.append(nilai)
    arrTextResult.append(string)
    string = string[0:2]+"("+string[2:9]+")"
    #print(string)
    try:
        nilai = eval(string)
    except ZeroDivisionError:
        nilai = 0    
    arrResult.append(nilai)
    arrTextResult.append(string)

    string = text
    string = string[0:4]+"("+string[4:7]+")"
    #print(string)
    try:
        nilai = eval(string)
    except ZeroDivisionError:
        nilai = 0    
    arrResult.append(nilai)
    arrTextResult.append(string)
    string = string[0:2]+"("+string[2:9]+")"
    #print(string)
    try:
        nilai = eval(string)
    except ZeroDivisionError:
        nilai = 0    
    arrResult.append(nilai)
    arrTextResult.append(string)


#fungsi melakukan pengacakan operasi
def randomMath(data):
    interMath1 = combinations_with_replacement(['*','-','+','/'], r=3)
    interMath2 = permutations(['*','-','+','/'], r=3)

    for index,math in enumerate(list(interMath1),1):
        getMath(math,data)
        # print(math)
    for index,math in enumerate(list(interMath2),1):
        getMath(math,data)
        # print(math)
 

def main():
    print('Masukan 4 angka (1-9)')
    data_list = []

    i = 1
    while i < 5:
        print('Angka ke-',i, end=': ')
        x = input()
        if x.isnumeric():
            x= int(x)
            if x !=0 and x<10 :
                data_list.append(x)
                i += 1
            else:
                print('inputan harus 1-9.')
        else:
            print('inputan anda bukan angka.')
        
    # randomMath('a')
    # penggunaan permutation
    permutasi = permutations(data_list)
    
    # loop untuk mengetahui hasil dari fungsi permutation 
    for index, data in enumerate(list(permutasi), 1):
        randomMath(data)

    print("Input User : ",data_list)
    findNearest()

    # for index, data in enumerate(list(arrResult), 1):
    #     print(data)

    # for index, data in enumerate(list(arrTextResult), 1):
    #     print(data)

if __name__ == "__main__":
    sys.exit(main())
