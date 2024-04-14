import threading
import requests
# 定义文件路径
file_path = 'proxy.txt'

# 定义一个函数，用于在每个线程中处理文件的一行
def process_line(line, thread_id):
    url = 'https://www.ipuu.net/ipuu/user/getIP'

    proxy = {

        # 'https' : '114.231.45.36:8089'
        # 'https': '41.231.37.76:3128'
        'https': line
    }
    try:
        rp = requests.get(url=url, proxies=proxy, timeout=15).text
        print(rp, line)
    except:
        pass  # 打印线程ID和对应的行内容

# 定义一个函数，用于读取文件并分发给线程处理
def read_file_and_process(file_path, num_threads):
    # 创建一个线程列表
    threads = []
    # 创建一个锁，用于同步线程间的输出
    lock = threading.Lock()

    # 打开文件
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()  # 读取所有行到列表中

        # 创建并启动指定数量的线程
        for i, line in enumerate(lines):
            thread = threading.Thread(target=process_line, args=(line.strip(), i + 1))
            thread.start()
            threads.append(thread)

    # 等待所有线程完成
    for thread in threads:
        thread.join()

# 主函数
def main():
    # 指定线程数量
    num_threads = 6
    # 调用函数，读取文件并在多个线程中处理
    read_file_and_process(file_path, num_threads)

if __name__ == "__main__":
    main()