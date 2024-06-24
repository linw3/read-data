from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms

img_path="D:\\code\\python\\pytor\\pythonProject\\hymenoptera_data\\train\\ants\\0013035.jpg"
img=Image.open(img_path)
print(img)

writer=SummaryWriter("logs")

tensor_trans=transforms.ToTensor()  #返回对象
tensor_img=tensor_trans(img)   #img->tensor类的img


writer.add_image("Tensor_img",tensor_img)

writer.close()

