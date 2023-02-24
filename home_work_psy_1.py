# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 15:28:28 2023

@author: Jacky
"""

import numpy as np

class Image_calculator:
  def __init(self):
      self.img1 = img1
      self.img2 = img2
      self.ch = ch
      self.scale = scale

  def Add(self):
      img1_ch = self.img1[:,:,self.ch]
      Img2_ch = self.img2[:,:,self.ch]
      result = np.add(img1_ch,img2_ch)
      return result

  def Subtract(self):
      img1_ch = self.img1[:,:,self.ch]
      img2_ch = self.img2[:,:,self.ch]
      result = np.subtract(img1_ch,img2_ch)
      return result

  def Multiply(self):
      img1_ch = self.img1[:,:,self.ch]
      result = np.multiply(img1_ch,self.scale)
      return result

  def Divide(self):
      img1_ch = self.img1[:,:,self.ch]
      result = np.divide(img1_ch,self.scale)
      return result
     

ImgA = img.imread(images_path + '/siemens_aunt.png')
ImgA_arr = np.array(ImgA)
ImgB = img.imread(images_path + '/siemens_aunt.png')
ImgB_arr = np.array(ImgB)
ch = 1
const = 3
I = Image_calculator()
I.img1 = ImgA_arr
I.img2 = ImgB_arr
I.ch = ch
I.scale = const

I.Add()
I.Subtract()
I.Multiply()
I.Divide()

# ====================================================================

import cv2 
import numpy as np

class Image_Calculator:
    def __init__(self, img1, img2):
        self.img1 = img1
        self.img2 = img2
        
    def add(self, ch1, ch2):
        img1_channels = cv2.split(self.img1)
        img2_channels = cv2.split(self.img2)
        img1_ch = img1_channels[ch1]
        img2_ch = img2_channels[ch2]
        result = cv2.add(img1_ch, img2_ch)
        return result
    
    def subtract(self, ch1, ch2):
        img1_channels = cv2.split(self.img1)
        img2_channels = cv2.split(self.img2)
        img1_ch = img1_channels[ch1]
        img2_ch = img2_channels[ch2]
        result = cv2.subtract(img1_ch, img2_ch)
        return result
    
    def multiply(self, ch1, ch2):
        img1_channels = cv2.split(self.img1)
        img2_channels = cv2.split(self.img2)
        img1_ch = img1_channels[ch1]
        img2_ch = img2_channels[ch2]
        result = cv2.multiply(img1_ch, img2_ch)
        return result
    
    def divide(self, ch1, ch2):
        img1_channels = cv2.split(self.img1)
        img2_channels = cv2.split(self.img2)
        img1_ch = img1_channels[ch1]
        img2_ch = img2_channels[ch2]
        result = cv2.divide(img1_ch, img2_ch)
        return result
    
file_location_path_1 = "D:\\dataset\\shl_img\\shl_img\\new_1.png"
img1 = cv2.imread(file_location_path_1)

file_location_path_2 = "D:\\dataset\\shl_img\\shl_img\\new_2.png"
img2 = cv2.imread(file_location_path_2)

img_calculator = Image_Calculator(img1, img2)

result = img_calculator.add(0,0)
result = img_calculator.subtract(0,0)
result = img_calculator.multiply(0,0)
result = img_calculator.divide(0,0)

cv2.imshow("result", result)
