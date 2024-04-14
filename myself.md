1.怎么在linux上安装chrome：
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get update
sudo apt install ./google-chrome-stable_current_amd64.deb
查看安装是不是成功了，版本是什么：
google-chrome --version

2.怎么在linux上安装chromedriver：
sudo mv chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver
from selenium import webdriver
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

3.linux上用selenium，最好用无头运行：
chrome_options = Options()
chrome_options.add_argument("--headless")  # 运行无头版本的Chrome
chrome_options.add_argument("ignore-certificate-erros")  # 忽略证书错误
chrome_options.add_argument("--no-sandbox")  # 在无沙盒模式下运行
chrome_options.add_argument("--disable-dev-shm-usage")  # overcome limited
service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service,options=chrome_options)
