import openpyxl
import pandas



class DataManager:

    def get_from_excel(self,name,sheet_name):
        path = '../data/'+name+'.xlsx'
        df = pandas.read_excel(path,sheet_name=sheet_name)#读取指定Excel文件的指定标签页数据
        data = df.values.tolist()#将读取到的数据转换成二维列表
        return data

data_manager=DataManager()
if __name__=='__main__':
    data_manager.get_from_excel('test_opcart_demo','test_01_reg')