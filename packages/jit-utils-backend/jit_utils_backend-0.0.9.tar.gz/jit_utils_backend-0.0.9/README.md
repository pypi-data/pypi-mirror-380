# JIT Utils Backend

极态后端工具包 - 一个为后端开发提供便利工具的 Python 包。

## 安装

```bash
pip install jit_utils_backend
```

## 使用方法

### 导入包

```python
# 导入整个包
import jit_utils

# 导入特定功能（从具体的子模块）
from jit_utils.time import now
from jit_utils.string import randomString
from jit_utils.qrcode import Qrcode
from jit_utils.barcode import Barcode

# 导入特定模块
import jit_utils.time
import jit_utils.string
```

## 主要功能

### 1. 时间处理工具

```python
from jit_utils.time import now, today, dayShift, formatNow

# 获取当前时间
current_time = now()

# 获取今天的日期
today_date = today()

# 日期偏移
tomorrow = dayShift(today_date, 1)

# 格式化当前时间
formatted_time = formatNow("%Y-%m-%d %H:%M:%S")
```

### 2. 字符串处理工具

```python
from jit_utils.string import randomString, md5Str, getUuidStr

# 生成随机字符串
random_str = randomString(8)

# MD5 加密
encrypted = md5Str("hello world")

# 生成 UUID
uuid_str = getUuidStr()
```

### 3. 二维码生成

```python
from jit_utils.qrcode import Qrcode

# 创建二维码
qr = Qrcode("https://example.com")

# 获取二维码图片的字节数据
qr_bytes = qr.toByte()

# 获取二维码的 base64 字符串
qr_str = qr.toStr()
```

### 4. 条形码生成

```python
from jit_utils.barcode import Barcode

# 创建条形码
barcode = Barcode("123456789")

# 获取条形码图片的字节数据
barcode_bytes = barcode.toByte()

# 获取条形码的 base64 字符串
barcode_str = barcode.toStr()
```

### 5. 数据验证

```python
from jit_utils.validator import ParamsValidator
from dataclasses import dataclass

@dataclass
class UserParams(ParamsValidator):
    name: str
    age: int
    email: str = ""

# 验证参数
params = UserParams("test_function", name="John", age=25)
```

### 6. 装饰器

```python
from jit_utils.decorator import forward

@forward("module.submodule")
def my_function():
    pass
```

## 模块说明

- **time_utils**: 时间处理相关工具
- **string_utils**: 字符串处理相关工具
- **qrcode**: 二维码生成工具
- **barcode**: 条形码生成工具
- **validator**: 数据验证工具
- **network**: 网络相关工具
- **signature**: 签名相关工具
- **matchTool**: 匹配工具
- **clsTool**: 类工具
- **exceptions**: 异常处理
- **workday_constants**: 工作日常量
- **config**: 配置相关工具

## 依赖包

- requests
- qrcode
- python-barcode
- Pillow
- arrow
- python-dateutil

## 许可证

MIT License

## 作者

JitAi (develop@wanyunapp.com)

## 版本

0.0.5
