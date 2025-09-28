# 📈 agushuju

<div align="center">

**爱股数据 - 专业的A股量化交易数据服务**

[![Python Version](https://img.shields.io/badge/python-2.7%20%7C%203.5+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/agushuju.svg)](https://pypi.org/project/agushuju/)
[![Downloads](https://img.shields.io/pypi/dm/agushuju.svg)](https://pypi.org/project/agushuju/)

*一个集A股、期货于一体的量化交易数据服务平台*

[官网](https://www.agushuju.com/) • [文档](https://www.agushuju.com/doc) • [社区](https://www.agushuju.com/ask) • [QQ群](https://qm.qq.com/cgi-bin/qm/qr?k=224731242) 224731242

</div>

---

## ✨ 特性

- 🐍 **全版本兼容**: 支持 Python 2.7+ 和 Python 3.5+，自动适配依赖版本
- 🚀 **开箱即用**: 简洁的API设计，几行代码即可获取数据
- 📊 **数据处理**: 内置pandas支持，返回DataFrame格式，便于分析
- 🔧 **灵活配置**: 支持环境变量配置，支持自定义API端点
- 📈 **实时数据**: 提供A股、期货等金融数据的实时访问
- 🛡️ **安全可靠**: 支持API密钥管理，支持密钥有效期设置

## 🚀 快速开始

### 安装

```bash
pip install agushuju
```

### 获取API密钥

1. 访问 [官网](https://www.agushuju.com/) 注册账号
2. 进入会员中心，点击"API密钥"
3. 复制您的API密钥

> 💡 **密钥类型说明**：
> - **默认密钥**：用于在线调试，不可删除
> - **自定义密钥**：可设置注释和有效期，便于管理
> 
> 🆘 **遇到问题？** 加入QQ群 **224731242** 获取帮助！
### 基础使用

```python
import agushuju

# 创建API客户端
api = agushuju.api("your_token_here")

# 获取股票基本信息（默认参数）
df = api.stock_basic()
print(df.head())
```

### 高级查询

```python
# 带参数查询（指定条件，返回指定字段）
df = api.stock_basic(
    request={
        "list_status": "L",  # 查询上市股票
        "limit": 100,        # 限制返回数量
        "offset": 0          # 偏移量
    },
    response=["stock_code", "stock_name", "area"]  # 指定返回字段
)

print(f"查询到 {len(df)} 只股票")
print(df.head())
```

### 使用别名导入

```python
# 也可以使用 aigushuju 别名
import aigushuju as agu

api = agu.api("your_token_here")
df = api.stock_basic()
```

## 📚 接口文档

详细的接口参数和返回字段说明，请查看：

👉 **[完整接口文档](https://www.agushuju.com/doc)**

## 💡 使用示例

### 获取股票列表

```python
import agushuju

# 初始化API
api = agushuju.api("your_token_here")

# 获取所有上市股票
stocks = api.stock_basic(
    request={"list_status": "L"},
    response=["stock_code", "stock_name", "area", "industry"]
)

print(f"共找到 {len(stocks)} 只上市股票")
print(stocks.head(10))
```

### 数据分析示例

```python
import pandas as pd

# 获取股票数据
df = api.stock_basic()

# 按地区统计股票数量
area_stats = df['area'].value_counts().head(10)
print("各地区股票数量：")
print(area_stats)

# 按行业统计
industry_stats = df['industry'].value_counts().head(10)
print("\n各行业股票数量：")
print(industry_stats)
```

### 批量查询

```python
# 分页获取数据
all_stocks = []
offset = 0
limit = 1000

while True:
    batch = api.stock_basic(
        request={"limit": limit, "offset": offset},
        response=["stock_code", "stock_name"]
    )
    
    if len(batch) == 0:
        break
        
    all_stocks.append(batch)
    offset += limit
    
    print(f"已获取 {offset} 条记录...")

# 合并所有数据
final_df = pd.concat(all_stocks, ignore_index=True)
print(f"总共获取 {len(final_df)} 条股票记录")
```

## ⚙️ 配置

### 环境变量

您可以通过环境变量设置默认配置，避免在代码中硬编码：

```bash
# Windows
set AGU_TOKEN=your_token_here
set AGU_BASE_URL=https://www.agushuju.com/api

# Linux/macOS
export AGU_TOKEN="your_token_here"
export AGU_BASE_URL="https://www.agushuju.com/api"
```

```python
# 使用环境变量
import agushuju

# 自动从环境变量读取配置
api = agushuju.api()  # 无需传入token
```

## 🔧 兼容性

| Python版本 | 状态 | requests版本 | pandas版本 |
|-----------|------|-------------|-----------|
| Python 2.7 | ✅ 支持 | >= 2.20.0, < 3.0.0 | >= 0.24.0, < 1.0.0 |
| Python 3.5+ | ✅ 支持 | >= 2.25.0 | >= 1.1.0 |

## 📞 支持与社区

- 🌐 **官网**: [https://www.agushuju.com/](https://www.agushuju.com/)
- 📖 **文档**: [https://www.agushuju.com/doc](https://www.agushuju.com/doc)
- 💬 **社区**: [https://www.agushuju.com/ask](https://www.agushuju.com/ask)
- 👥 **QQ群**: 224731242
- 📧 **邮箱**: jinguxun@qq.com

## 📄 许可证

本项目基于 [MIT License](LICENSE) 开源协议。

---

<div align="center">

**⭐ 如果这个项目对您有帮助，请给我们一个星标！**

Made with ❤️ by [安徽爱股科技有限公司](https://www.agushuju.com/)

</div>
