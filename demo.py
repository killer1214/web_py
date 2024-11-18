from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 设置Edge选项
edge_options = Options()
edge_options.add_argument('--start-maximized')  # 最大化窗口
# edge_options.add_argument('--headless')  # 无头模式（如果需要）

# 初始化Edge浏览器
driver = webdriver.Edge(options=edge_options)

try:
    # 打开bilibili
    driver.get("https://www.bilibili.com")
    
    # 等待页面加载完成（等待搜索框出现）
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "nav-search-input"))
    )
    
    # 页面停留一段时间以便查看
    time.sleep(10)
    
except Exception as e:
    print(f"发生错误: {e}")
finally:
    driver.quit()