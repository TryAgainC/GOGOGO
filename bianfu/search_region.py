import pyautogui
image_path = "img.png"  # 你要查找的图像文件路径
location = pyautogui.locateOnScreen(image_path)

if location:
    print(f"图像位于坐标：{location}")
else:
    print("图像未找到")