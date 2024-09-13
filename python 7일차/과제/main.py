# main.py

from animals.mammals import Dog
from animals.birds import Eagle

def main():
    # Dog 객체 생성 및 정보 출력
    dog = Dog(name="Buddy", breed="Golden Retriever")
    print(dog)

    # Eagle 객체 생성 및 정보 출력
    eagle = Eagle(name="Harpy", wingspan=2.5)
    print(eagle)

if __name__ == "__main__":
    main()
