from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import atexit

def check_init(func):
    def wrapper(self,*args, **kwargs):
        if not self.initd:
            raise RuntimeError("초기화 설정이 필요합니다.")
        return func(self, *args, **kwargs)

    return wrapper

class CrawlingNamespace:
    driver = None
    initd = False

    def __init__(self, parent):
        self.parent = parent

    def init(self, headless: bool = False, secret: bool = False,
             window_size: str = "800,600", auto_quit: bool = True,
             fast: bool = True, cache: str = None, user_agent: str = None):
        """
        Selenium 브라우저 초기화 클래스
        Args:
            headless (bool): True → 백그라운드 실행(창 안뜸), False → 일반 모드
            secret (bool): True → 시크릿 모드
            window_size (str): 브라우저 창 크기 (기본 800x600)
            auto_quit (bool): True → 파이썬 종료 시 브라우저 자동 종료
            fast (bool): True → 이미지 로딩 비활성화 (빠른 실행)
            cache (str): 캐시 폴더 경로 (예: 'c:/cache/user1')
            user_agent (str): 사용자 정의 User-Agent
        """
        options = Options()
        options.add_argument(f"--window-size={window_size}")
        options.add_argument("--disable-features=ChromeWhatsNewUI")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        # headless 모드
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")

        # 시크릿 모드
        if secret:
            options.add_argument("--incognito")

        # 빠른 모드 (이미지 로딩 차단)
        if fast:
            prefs = {"profile.managed_default_content_settings.images": 2}
            options.add_experimental_option("prefs", prefs)

        # 캐시 폴더 지정
        if cache:
            options.add_argument(f"--user-data-dir={cache}")
            options.add_argument(f"--disk-cache-dir={cache}")

        # User-Agent 지정
        if user_agent:
            options.add_argument(f"user-agent={user_agent}")

        options.add_experimental_option("detach", True)

        # 브라우저 실행
        self.driver = webdriver.Chrome(options=options)
        self.initd = True

        if auto_quit:
            atexit.register(self.quit)

    @check_init
    def open(self, url):
        self.driver.get(url)

    @check_init
    def quit(self):
        self.driver.quit()