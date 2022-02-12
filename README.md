# popups
![PyPI](https://img.shields.io/pypi/v/popups) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/popups) ![GitHub top language](https://img.shields.io/github/languages/top/openutx/popups) ![PyPI - Downloads](https://img.shields.io/pypi/dm/popups?style=plastic) ![GitHub stars](https://img.shields.io/github/stars/openutx/popups?style=social) ![https://blog.csdn.net/flower_drop](https://img.shields.io/badge/csdn-%40flower__drop-orange)
## 安装
- 命令行执行
```
pip install -U popups
```
## 使用

```python
from popups import popup
from popups import UT

# 默认是False状态，使用时需要打开
UT.ENABLE = True
# 图片模版路径，不传则使用popups自带的模版库
IMG_PATH = 'your_tpl_path'
# 单独使用popup时需要传入设备URL，配合utx使用时无需关注
DEVICE = 'Android://127.0.0.1:5037/SJE5T17B17'

popup(tpl=IMG_PATH, devices=DEVICE)
```
