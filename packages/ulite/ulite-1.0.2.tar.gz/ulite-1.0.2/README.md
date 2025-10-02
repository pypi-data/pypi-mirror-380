# ulite.py

- 轻量化ui框架
- 支持构建基于flask的webui


# 安装
```
git clone https://gitee.com/zlols/ulite.py
pip install -e ulite.py
```

# 用法

```
import ulite
import random

ui = ulite.createUI(backends='flask', port=5001)
ui.root.addChild(
    ulite.Button(text='hello').subscribeEvent('click', lambda e: e.target.setAttributes(text=random.randint(0,100)))
    )
ui.show(openbrowser=True)
```

# 小贴士
- 使用nuitka打包时需要添加静态文件打包参数`--include-package-data=ulite`
