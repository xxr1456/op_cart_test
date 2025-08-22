import os
from  multiprocessing import Pool


class RunManager:
    def __init__(self):
        foldr_path = '../report/result'
        if len(os.listdir(foldr_path))>0:
            for file_name in os.listdir(foldr_path):
                file_path = os.path.join(foldr_path,file_name)
                os.remove(file_path)

    def run_pytest(self,file):
        cmd = f"pytest {os.path.abspath(file)} --alluredir ../report/result"
        os.system(cmd)

    def run_and_create_report(self):
        files = ["../Test/test.py", "../Test/test01.py"]
        with Pool(3) as pool:
            pool.map(self.run_pytest,files)
        os.path.abspath(__file__)
        os.system('allure generate --clean ../report/result -o ../report/html')


if __name__=='__main__':
    RunManager().run_and_create_report()


