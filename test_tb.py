from torch.utils.tensorboard import SummaryWriter  #可以绘制图像

writer=SummaryWriter("logs")  #创建类实例
#writer.add_image()
#y=2x
for i in range(100):
    writer.add_scalar("y=2x",2*i,i)    #标题名   y轴  x轴   训练新的可以新建一个子文件  会自动拟合
writer.close()
