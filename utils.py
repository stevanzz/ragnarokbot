import win32api


confidence = 0.8


def get_region():
  width = win32api.GetSystemMetrics(0)
  height = win32api.GetSystemMetrics(1)
  default_region = (1470, 675, 175, 175)
  if width == 1536 and height == 864:
    return (1470, 675, 175, 175)
  elif width == 1920 and height == 1080:
    return (1485, 680, 175, 175)
  else:
    return default_region