import pyramid
import Archimed

def main():
    print("выберите 1 или 2 ")
    print("1 - oбъем пирамиды ")
    print("2 - проверка плавучести ")
    choice = input("ваш выбор ")
    if choice == "1":
        pyramid.calculate_pyramid_volume()
    elif choice == "2":
        Archimed.check_buoyancy()
    else:
        print("такого варианта нет ")

if __name__ == "__main__":
    main()
