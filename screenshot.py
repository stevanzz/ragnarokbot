import pyautogui
import numpy as np
from PIL import Image, ImageDraw
from utils import get_region


def crop_to_circle(img):
  npImage = np.array(img)
  h, w = img.size

  # Create same size alpha layer with circle
  alpha = Image.new('L', img.size, 0)
  draw = ImageDraw.Draw(alpha)
  draw.pieslice([0, 0, h, w], 0, 360, fill=255)

  # Convert alpha Image to numpy array
  npAlpha = np.array(alpha)

  # Add alpha layer to RGB
  npImage = np.dstack((npImage, npAlpha))

  return Image.fromarray(npImage)


def screenshot_image(filename):
  screenshot_image = pyautogui.screenshot(region=get_region())
  crop_to_circle(screenshot_image).save(filename)
