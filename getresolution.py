import win32api

width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
print("Width =", width)
print("Height =", height)
