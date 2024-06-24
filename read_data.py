from torch.utils.data import Dataset
from PIL import Image  #读取图片
import os

class MyDataset(Dataset):

    def __init__(self,root_dir,label_dir): #初始化类——为类提供全局变量，提供后面函数需要的量
        self.root_dir = root_dir  #self可以指定类里面的全局变量
        self.label_dir = label_dir
        self.path=os.path.join(self.root_dir,self.label_dir)  #获取图片的路径地址  并且可以拼接两个地址
        self.file_list=os.listdir(self.path)  #获取图片下所有的地址（列表）

    def __getitem__(self, idx):    #idx——编号
        img_name=self.file_list[idx]  #获取其中的每一个
        img_item_path=os.path.join(self.root_dir,self.label_dir,img_name) #获取每一个的相对地址
        img = Image.open(img_item_path)  #读取图片
        label=self.label_dir
        return img,label
    def __len__(self):
        return len(self.file_list)   #获取列表长度

root_dir="dataset/train"
ants_label_dir="ants"
bees_label_dir = "bees"
ants_dataset= MyDataset( root_dir, ants_label_dir)
bees_dataset = MyDataset(root_dir, bees_label_dir)

train_dataset=ants_dataset+bees_dataset




