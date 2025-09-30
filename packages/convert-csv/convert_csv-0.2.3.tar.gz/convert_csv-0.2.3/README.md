# CSV格式转换工具

一个简单易用的CSV文件格式转换工具，可以帮助您批量处理CSV文件中的金额和日期格式。

## 功能特点

- 🔄 **自动编码检测** - 自动识别CSV文件的字符编码
- 💰 **金额格式化** - 将金额统一格式化为两位小数
- 📅 **日期格式化** - 将日期转换为指定格式
- ⚙️ **配置文件驱动** - 通过简单配置指定需要处理的列
- 🎯 **智能处理** - 自动处理特殊日期值（如9999/12/31）

## 安装要求

- Python 3.8 或更高版本
- 需要安装的Python库：
  - pandas
  - chardet

## 快速开始

### 方法一：命令行使用（推荐）

1. **创建示例配置文件**
   ```bash
   convert-csv create_config
   ```

2. **编辑配置文件**
   打开生成的 `config.json` 文件，根据您的CSV文件结构进行修改。

3. **运行转换**
   ```bash
   convert-csv 输入文件.csv
   ```

### 方法二：交互式使用

直接运行程序，按提示输入信息：
```bash
convert-csv
```

## 配置文件说明

配置文件为JSON格式，包含两个主要部分：

### 金额列配置
```json
{
  "amount_columns": ["金额", "价格", "费用"]
}
```

### 日期列配置
```json
{
  "date_columns": {
    "交易时间": "YYYY-MM-DD HH:mm:ss",
    "数据日期": "YYYY-MM-DD",
    "创建时间": "YYYY/MM/DD HH:mm:ss"
  }
}
```

### 支持的日期格式
- `YYYY-MM-DD` - 年-月-日
- `YYYY-MM-DD HH:mm:ss` - 年-月-日 时:分:秒
- `YYYY/MM/DD` - 年/月/日
- `YYYY/MM/DD HH:mm:ss` - 年/月/日 时:分:秒

## 使用示例

### 基本用法
```bash
# 使用默认配置
convert-csv data.csv

# 指定输出文件
convert-csv data.csv -o output.csv

# 指定配置文件
convert-csv data.csv -c my_config.json
```

### 完整示例
```bash
# 1. 创建配置文件
convert-csv create_config

# 2. 编辑配置文件，设置需要处理的列
# 3. 运行转换
convert-csv sales_data.csv -c config.json -o sales_data_processed.csv
```

## 配置文件示例

```json
{
  "amount_columns": [
    "销售金额",
    "成本价格",
    "运费"
  ],
  "date_columns": {
    "订单日期": "YYYY-MM-DD",
    "发货时间": "YYYY-MM-DD HH:mm:ss",
    "创建日期": "YYYY/MM/DD"
  }
}
```

## 输出说明

- 程序会自动在输入文件同目录下生成输出文件
- 输出文件名格式：`原文件名-output.csv`
- 输出文件统一使用UTF-8编码

## 常见问题

### 1. 程序提示"编码检测置信度较低"
这是正常现象，程序会自动尝试使用常见的中文编码（GBK、GB2312等）继续处理。

### 2. 某些日期无法正确转换
请检查原始数据的日期格式是否规范，如有特殊格式可能需要手动处理。

### 3. 金额格式不正确
确保金额列中只包含数字、小数点和负号，其他字符会被自动过滤。

### 4. 找不到配置文件
如果没有指定配置文件，程序会在当前目录查找 `config.json`，如果不存在则使用默认配置。

## 技术支持

如果您遇到问题：
1. 检查CSV文件是否可以正常打开
2. 确认配置文件中的列名与CSV文件中的列名完全一致
3. 查看程序输出的警告信息，了解具体问题

## 版本信息

当前版本：v0.2.3

---

💡 **提示**：首次使用时建议先使用 `create_config` 参数创建示例配置文件，然后根据您的实际需求进行修改。