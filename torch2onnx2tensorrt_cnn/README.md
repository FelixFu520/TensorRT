# Introduction
源项目：https://github.com/zwqnju/PyTorch_ONNX_TensorRT    

## 一、环境
0. Ubuntu 16.06
1. CUDA 10.0
2. cuDNN 7.6
3. Python 3.5
4. TensorRT 7.0

### pip list
```
root@ubuntu:~# pip list
Package              Version               
-------------------- ----------------------
absl-py              0.9.0                 
appdirs              1.4.3                 
attrs                19.3.0                
backcall             0.1.0                 
bleach               3.1.3                 
cachetools           4.0.0                 
certifi              2019.11.28            
chardet              3.0.4                 
command-not-found    0.3                   
cycler               0.10.0                
decorator            4.4.2                 
defusedxml           0.6.0                 
entrypoints          0.3                   
google-auth          1.11.3                
google-auth-oauthlib 0.4.1                 
grpcio               1.27.2                
idna                 2.9                   
importlib-metadata   1.5.0                 
ipykernel            5.1.4                 
ipython              7.9.0                 
ipython-genutils     0.2.0                 
ipywidgets           7.5.1                 
jedi                 0.16.0                
Jinja2               2.11.1                
jsonschema           3.2.0                 
jupyter              1.0.0                 
jupyter-client       6.0.0                 
jupyter-console      6.1.0                 
jupyter-core         4.6.3                 
kiwisolver           1.1.0                 
language-selector    0.1                   
Mako                 1.1.2                 
Markdown             3.2.1                 
MarkupSafe           1.1.1                 
matplotlib           3.0.3                 
mistune              0.8.4                 
nbconvert            5.6.1                 
nbformat             5.0.4                 
notebook             6.0.3                 
numpy                1.18.2                
oauthlib             3.1.0                 
onnx                 1.6.0                 
onnx-tensorrt        0.1.0                 
onnxruntime          1.2.0                 
pandocfilters        1.4.2                 
parso                0.6.2                 
pexpect              4.8.0                 
pickleshare          0.7.5                 
Pillow               7.0.0                 
pip                  20.0.2                
prometheus-client    0.7.1                 
prompt-toolkit       2.0.10                
protobuf             3.11.3                
ptyprocess           0.6.0                 
pyasn1               0.4.8                 
pyasn1-modules       0.2.8                 
pycuda               2019.1.2              
pycurl               7.43.0                
Pygments             2.6.1                 
pygobject            3.20.0                
pyparsing            2.4.6                 
pyrsistent           0.15.7                
python-apt           1.1.0b1+ubuntu0.16.4.2
python-dateutil      2.8.1                 
python-debian        0.1.27                
python-systemd       231                   
pytools              2020.1                
pyzmq                19.0.0                
qtconsole            4.7.1                 
QtPy                 1.9.0                 
requests             2.23.0                
requests-oauthlib    1.3.0                 
rsa                  4.0                   
Send2Trash           1.5.0                 
setuptools           46.0.0                
six                  1.10.0                
ssh-import-id        5.5                   
tensorboard          2.1.1                 
tensorrt             7.0.0.11              
terminado            0.8.3                 
testpath             0.4.4                 
torch                1.2.0                 
torchvision          0.4.0                 
tornado              6.0.4                 
traitlets            4.3.3                 
typing-extensions    3.7.4.1               
ufw                  0.35                  
unattended-upgrades  0.1                   
urllib3              1.25.8                
wcwidth              0.1.8                 
webencodings         0.5.1                 
Werkzeug             1.0.0                 
wheel                0.29.0                
widgetsnbextension   3.5.1                 
zipp                 1.2.0
```
