import sys;

numbers = ' '.join(c if c.isdigit() else ' ' for c in sys.argv).split()
def road_array(num):
    
    if 3 > len (num) > 1 and num[0] != "0" and num[1] != "0":
        
        n, m = map(int, num)
        i = 1
        while True:
            print(i, end='')
            i = 1 + (i + m - 2) % n
            if i == 1:
                break
        print()
    elif  num[0] == '0' or num[1] == '0':
         print("Ошибка ввода: Один из аргументов равeн нулю")
    else:
        print("Ошибка ввода: Введите размер массива и шаг интервала числами через пробел в качестве аргумента.")
   
if __name__ == "__main__":
    road_array(numbers)
    