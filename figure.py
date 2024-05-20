"""
figure 모듈

이 모듈은 선(Line) 클래스와 다양한 도형의 면적을 계산하는 함수들을 포함하고 있습니다.

클래스:
    Line: 특정 길이를 가진 선을 나타내는 클래스입니다.

함수:
    area_square(line): 길이를 입력받아 정사각형의 넓이를 구하는 함수입니다.
    area_circle(line): 길이를 입력받아 원의 넓이를 구하는 함수입니다.
    area_regular_triangle(line): 길이를 입력받아 정삼각형의 넓이를 구하는 함수입니다.
    """
import math

class Line:
    """
    특정 길이를 가진 선을 나타내는 클래스입니다.

    type:
    length : float
        선의 길이입니다.
    """
    def __init__(self, length=1):
        """
        주어진 길이로 Line 객체를 생성하는 생성자입니다.

        Args:
        length (float, optional): 선의 길이입니다. 기본값은 1입니다.
        """
        
        if((type(length)==int or type(length)==float) and length>0):
            self.__length=length
        else:
            self.__length=1

    def set_length(self, length):
        """
        선의 길이를 설정하는 메서드입니다.

        Args:
        length (float): 선의 새 길이입니다.
        """
        if((type(length)==int or type(length)==float) and length>0):
            self.__length=length
            
    def get_length(self):
        """
        선의 길이를 반환하는 메서드입니다.

        Returns:
        float: 선의 길이를 반환합니다.
        """
        return self.__length
    
def area_square(line):
    """
    길이를 입력받아 정사각형의 넓이를 구하는 함수입니다.

    Args:
    line (Line): 정사각형의 한 변의 길이입니다.

    Returns:
    float: 정사각형의 넓이를 반환합니다.
    """
    return line.get_length() ** 2
    
def area_circle(line):
    """
    길이를 입력받아 원의 넓이를 구하는 함수입니다.

    Args:
    line (Line): 반지름의 길이입니다.

    Returns:
    float: 원의 넓이를 반환합니다.
    """
    return line.get_length() ** 2 * math.pi
    
def area_regular_triangle(line):
    """
    길이를 입력받아 정삼각형의 넓이를 구하는 함수입니다.

    Args:
    line (Line): 정삼각형의 한 변의 길이입니다.

    Returns:
    float: 정삼각형의 넓이를 반환합니다.
    """
    return line.get_length() ** 2 *math.sqrt(3)/4

