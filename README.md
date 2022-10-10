# popups
![PyPI](https://img.shields.io/pypi/v/popups) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/popups) ![GitHub top language](https://img.shields.io/github/languages/top/openutx/popups) [![Downloads](https://pepy.tech/badge/monitors)](https://pepy.tech/project/monitors)  ![https://blog.csdn.net/flower_drop](https://img.shields.io/badge/csdn-%40flower__drop-orange)

## 安装
- 命令行执行
```
pip install -U popups
```
## 使用

```python
from popups.dismiss import popup, UT

# 默认是False状态，使用时需要打开
UT.ENABLE = True
# 图片模版路径，不传则使用popups自带的模版库
IMG_PATH = 'your_tpl_path'
# 是否启用系统弹窗处理
UT.SYS = True
# 是否启用APP弹窗处理
UT.APP = False
# 是否是iOS系统
UT.iOS = True
# 循环执行次数，默认为1次
UT.LOOP = 1
# 超时时间，默认为5秒
UT.TIMEOUT = 5
# 单独使用popup时需要传入设备URL，配合utx使用时无需关注
DEVICE = 'Android://127.0.0.1:5037/SJE5T17B17'

popup(devices=DEVICE)
```
## 
- 配合`utx`使用效果更好
