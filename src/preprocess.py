import cv2
import numpy as np


class PreprocessBlocks:

    @staticmethod
    def resize(img, args):
        """이미지 크기 조절: args = [width, height]"""
        return cv2.resize(img, (args[0], args[1]))

    @staticmethod
    def normalize(img, args):
        """픽셀 값 정규화 (0~255 -> 0~1): args = [max_value]"""
        return img / args[0]

    @staticmethod
    def convert_color(img, args):

        mode=args[0].upper()
        if mode == 'GRAY':
            return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #  그레이 로 바꾸기
        elif mode =='LAB':
            return cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        elif mode =='HSV':
            return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        elif mode =="YCRCB":
            return cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
        else:
            return None

    @staticmethod
    def gaussian_blur(img, args):
        """노이즈 제거 (가우시안 블러): args = [kernel_size] (홀수)"""
        k_size = args[0]
        return cv2.GaussianBlur(img, (k_size, k_size), 0)

    @staticmethod
    def padding(img, args):
        """이미지 테두리 추가: args = [top, bottom, left, right, color_value]"""
        t, b, l, r, color = args
        return cv2.copyMakeBorder(img, t, b, l, r, cv2.BORDER_CONSTANT, value=[color, color, color])





