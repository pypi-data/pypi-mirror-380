from ftplib import FTP

def check_connection(func):
    def wrapper(self,*args, **kwargs):
        if not self.connected:
            raise RuntimeError("FTP 연결이 필요합니다.")
        return func(self, *args, **kwargs)

    return wrapper

class FTPNamespace:
    """[FTP] 관련 기능 모음"""
    connected = False

    def __init__(self,parent):
        self.parent = parent

    def connect(self,host, user,passwd):
        try:
            self.ftp = FTP(host)
            self.ftp.login(user=user, passwd=passwd)
            print(f"[FTP] 연결 성공: {host}@{user}")
            self.connected = True
        except Exception as e:
            self.connected = False
            raise ValueError(f"[FTP] 연결 실패: {e}")

    @check_connection
    def ls(self):
        self.ftp.nlst()