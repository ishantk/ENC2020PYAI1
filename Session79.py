"""
    Pytorch Hub
    Reference Link: https://pytorch.org/hub/research-models
    Reference Link for Image Classification: https://pytorch.org/docs/stable/torchvision/models.html#classification

    Exploring GoogleNet
    Reference Link: https://pytorch.org/hub/pytorch_vision_googlenet/

    Its a model with over 1000 classes :)

"""
# We need 2 libraries to work with
# pip install torch
# pip install torchvision

import torch
from torchvision import models
from torchvision import transforms

from PIL import Image

print("MODELS")
print(dir(models))

print("USING GoogLeNet")
model = models.googlenet(pretrained=True)
summary = model.eval()
print("MODEL SUMMARY")
print(summary)

# input_image = Image.open("husky.jpeg") # read as numpy array
# input_image = Image.open("car.jpg") # read as numpy array
# input_image = Image.open("bikes.jpg") # read as numpy array
input_image = Image.open("ibis.jpg") # read as numpy array

# With pytorch transform API we are Pre-Processing the Image i.e. between 0's and 1's to feed to the network for predictions
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.299, 0.224, 0.255])
])

# pre-processed and transformed it to Tensor (PyTorch Array)
input_tensor = transform(input_image)

# create batch out of tensor
input_batch = input_tensor.unsqueeze(0)

# if my system supports GPU Processing
if torch.cuda.is_available():
    input_batch = input_batch.to('cuda')
    model.to('cuda')

# for Model to predict we need not to do back feed :)
with torch.no_grad():
    output = model(input_batch)

print("Confidence Scores for the Image over 1000 classes")
print(output[0])
print("We have", len(output[0]), "Confidence Scores for GoogleNet Classes")
print("SOFTMAX PROBABILITIES")
print(torch.nn.functional.softmax(output[0], dim=0))

file = open("googlenet_classes.txt")

labels = [line.strip() for line in file.readlines()]

# Extract the Index with Max Confidence Score
_, index = torch.max(output, 1)
percentage = torch.nn.functional.softmax(output, dim=1)[0] * 100
print("Index {} with Max Percentage Score {}".format(index, percentage[index[0]].item()))
print("LABEL:", labels[index[0]])




