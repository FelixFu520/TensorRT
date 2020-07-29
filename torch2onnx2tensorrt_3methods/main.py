import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
from TensorRTNet import TensorRTNet
import torch

if __name__ == '__main__':
    test = TensorRTNet()
    print("第一种方式：通过加载权重，构建引擎（需要根据模型搭建TensorRT网络结构）")
    test.toTensorRT('../models/threeMnist.pth')
    print("第二种方式：通过解析onnx，构建引擎（不需要搭建TensorRT网络结构）")
    test.loadONNX2TensorRT('../models/threeMnist.onnx')
    print("第三种方式：通过加载engine，构建引擎（不需要搭建TensorRT网络结构）")
    test.loadEngine2TensorRT("../models/threeMnist.engine")
