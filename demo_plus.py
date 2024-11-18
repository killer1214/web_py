from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class BilibiliBot:
    def __init__(self):
        # 设置Edge选项
        self.options = Options()
        self.options.add_argument('--start-maximized')
        
        # 添加更友好的User-Agent
        self.options.add_argument('user-agent=Mozilla/5.0 (compatible; BilibiliBot/1.0; +http://example.com/bot)')
        
        # 添加延迟，避免频繁请求
        self.request_delay = 3  # 秒
        
        # 初始化浏览器
        self.driver = webdriver.Edge(options=self.options)
        self.wait = WebDriverWait(self.driver, 10)
    
    def respect_robots_txt(self, url):
        """检查URL是否允许访问"""
        disallowed_paths = [
            '/account/', '/audio/', '/history/', '/member/',
            '/message/', '/mylist/', '/pay/', '/reply/',
            '/video/', '/watchlater/', '/activity/'
        ]
        for path in disallowed_paths:
            if path in url:
                return False
        return True
    
    def open_url(self, url):
        """安全地打开URL"""
        if self.respect_robots_txt(url):
            self.driver.get(url)
            time.sleep(self.request_delay)
        else:
            raise Exception("该URL不允许访问，根据robots.txt规则")
    
    def open_bilibili(self):
        """打开bilibili首页"""
        self.open_url("https://www.bilibili.com")
    
    def search_video(self, keyword):
        """搜索视频"""
        search_box = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "nav-search-input"))
        )
        search_box.clear()
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)
    
    def click_login(self):
        """点击登录按钮"""
        login_btn = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "header-login-entry"))
        )
        login_btn.click()
    
    def scroll_page(self):
        """滚动页面"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    
    def close(self):
        """关闭浏览器"""
        self.driver.quit()

# 使用示例
if __name__ == "__main__":
    bot = BilibiliBot()
    try:
        # 打开B站
        bot.open_bilibili()
        time.sleep(2)
        
        # 搜索视频
        bot.search_video("Python教程")
        time.sleep(2)
        
        # 滚动页面
        bot.scroll_page()
        time.sleep(2)
        
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        bot.close()