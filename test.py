# test.py
import sys
import platform
from datetime import datetime

def main():
    print("✅ Python 环境测试成功！")
    print(f"当前时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Python 版本: {platform.python_version()}")
    print(f"操作系统: {platform.system()} {platform.release()}")
    
    # 简单循环测试
    for i in range(1, 6):
        print(f"计数 {i}")

if __name__ == "__main__":
    main()