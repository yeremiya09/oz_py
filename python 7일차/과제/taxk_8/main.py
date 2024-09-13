# main.py

import mymath

def main():
    # 삼각형 넓이 계산
    base = 5.0
    height = 10.0
    triangle_area = mymath.triangle_area(base, height)
    print(f"삼각형 넓이: {triangle_area}")

    # 원의 넓이 계산
    radius = 7.0
    circle_area = mymath.circle_area(radius)
    print(f"원의 넓이: {circle_area:.2f}")

    # 직육면체의 부피 계산
    length = 4.0
    width = 3.0
    height = 6.0
    rectangular_prism_volume = mymath.rectangular_prism_volume(length, width, height)
    print(f"직육면체의 부피: {rectangular_prism_volume}")

if __name__ == "__main__":
    main()
