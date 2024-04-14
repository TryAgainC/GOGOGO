import pyautogui


# 截取屏幕的特定区域（例如，截取左上角100x100像素的区域）
region = pyautogui.screenshot(region=(100,200,300,500))
# 将特定区域的截图保存为文件
region.save("code.png")
# Box(left=681, top=856, width=106, height=43)