import os

def CreateDirectory(path):
    if not os.path.exists(path):
        os.makedirs(path)

        
def WriteToFile2(path, data, response):
    fullPath = os.path.join(path, data);
    with open(fullPath,'wb')as f:
        f.write(response.content);