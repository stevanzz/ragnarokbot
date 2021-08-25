import win32api

width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)

confidence = 0.8


def get_region():
  region = (1470, 675, 175, 175)
  if width == 1536 and height == 864:
    region = (1470, 675, 175, 175)
  elif width == 1920 and height == 1080:
    region = (1485, 680, 175, 175)

  # print(region)
  return region