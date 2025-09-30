import pandas as pd
import chardet
import os
import sys
import argparse
import json
import re

__version__ = "0.2.3"


def load_config(config_file=None):
    """
    加载配置文件
    
    参数:
    config_file: 配置文件路径，如果为None则尝试加载默认配置文件
    
    返回:
    配置字典
    """
    default_config = {
        "amount_columns": [],  # 需要修改金额格式的列名
        "date_columns": {}     # 需要修改日期格式的列名及目标格式
    }
    
    # 如果没有指定配置文件，尝试加载默认配置文件
    if config_file is None:
        config_file = "config.json"
        if not os.path.exists(config_file):
            print(f"未找到配置文件 {config_file}，使用默认配置")
            return default_config
    
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
            print(f"成功加载配置文件: {config_file}")
            return config
    except Exception as e:
        print(f"加载配置文件失败: {e}，使用默认配置")
        return default_config


def detect_file_encoding(file_path, sample_size=10000):
    """
    检测文件的编码格式

    参数:
    file_path: 文件路径
    sample_size: 采样大小（字节数）

    返回:
    检测到的编码格式
    """
    try:
        with open(file_path, "rb") as file:
            raw_data = file.read(sample_size)
            result = chardet.detect(raw_data)
            encoding = result["encoding"]
            confidence = result["confidence"]

            print(f"检测到文件编码: {encoding} (置信度: {confidence:.2f})")

            # 如果置信度较低或检测结果为None，使用常见的中文编码作为备选
            if encoding is None or confidence < 0.7:
                print("编码检测置信度较低，尝试使用常见中文编码")
                common_encodings = ["gbk", "gb2312", "utf-8", "latin1"]
                return common_encodings[0]  # 优先尝试gbk

            return encoding
    except Exception as e:
        print(f"编码检测错误: {e}，使用默认编码gbk")
        return "gbk"


def format_amount(value):
    """
    格式化金额为保留两位小数
    
    参数:
    value: 输入值
    
    返回:
    格式化后的金额字符串
    """
    if pd.isna(value) or value == "":
        return value
    
    try:
        # 尝试转换为浮点数并保留两位小数
        amount = float(value)
        return f"{amount:.2f}"
    except (ValueError, TypeError):
        # 如果转换失败，尝试清理字符串中的非数字字符（除小数点外）
        cleaned_value = re.sub(r'[^\d.-]', '', str(value))
        try:
            amount = float(cleaned_value)
            return f"{amount:.2f}"
        except (ValueError, TypeError):
            print(f"警告: 无法将值 '{value}' 转换为金额格式")
            return value


def format_date(value, target_format):
    """
    格式化日期为指定格式
    
    参数:
    value: 输入日期值
    target_format: 目标格式，如 'YYYY-MM-DD' 或 'YYYY-MM-DD HH:mm:ss'
    
    返回:
    格式化后的日期字符串
    """
    if pd.isna(value) or value == "":
        return value
    
    # 检查是否是特殊日期值 '9999/12/31' (表示无限期)
    if str(value).strip() == '9999/12/31':
        # 直接根据目标格式返回对应的字符串
        if target_format == 'YYYY-MM-DD':
            return '9999-12-31'
        elif target_format == 'YYYY-MM-DD HH:mm:ss':
            return '9999-12-31 00:00:00'
        elif target_format == 'YYYY/MM/DD':
            return '9999/12/31'
        elif target_format == 'YYYY/MM/DD HH:mm:ss':
            return '9999/12/31 00:00:00'
        else:
            # 对于其他格式，保持原值
            return value
    
    # 将目标格式转换为pandas支持的格式
    format_mapping = {
        'YYYY-MM-DD': '%Y-%m-%d',
        'YYYY-MM-DD HH:mm:ss': '%Y-%m-%d %H:%M:%S',
        'YYYY/MM/DD': '%Y/%m/%d',
        'YYYY/MM/DD HH:mm:ss': '%Y/%m/%d %H:%M:%S'
    }
    
    pandas_format = format_mapping.get(target_format, target_format)
    
    try:
        # 尝试多种常见的日期格式进行解析
        date_formats = [
            '%Y/%m/%d %H:%M',    # 原始格式
            '%Y/%m/%d',          # 只有日期
            '%Y-%m-%d %H:%M:%S', # 标准格式
            '%Y-%m-%d',          # 标准日期格式
            '%d/%m/%Y %H:%M',    # 日/月/年格式
            '%d/%m/%Y',          # 日/月/年日期格式
            '%m/%d/%Y %H:%M',    # 月/日/年格式
            '%m/%d/%Y'           # 月/日/年日期格式
        ]
        
        parsed_date = None
        for fmt in date_formats:
            try:
                parsed_date = pd.to_datetime(value, format=fmt, errors='raise')
                break
            except (ValueError, TypeError):
                continue
        
        # 如果以上格式都不匹配，尝试自动解析
        if parsed_date is None:
            parsed_date = pd.to_datetime(value, errors='coerce')
        
        if pd.isna(parsed_date):
            print(f"警告: 无法解析日期值 '{value}'")
            return value
        
        return parsed_date.strftime(pandas_format)
    except Exception as e:
        print(f"日期格式化错误: {e}，值: '{value}'")
        return value


def convert_csv_format(input_file, output_file=None, config_file=None):
    """
    转换CSV文件中的格式

    参数:
    input_file: 输入CSV文件路径
    output_file: 输出CSV文件路径（可选，如未提供则自动生成）
    config_file: 配置文件路径（可选）
    """
    # 加载配置
    config = load_config(config_file)
    amount_columns = config.get("amount_columns", [])
    date_columns = config.get("date_columns", {})
    
    print(f"配置加载完成:")
    print(f"  金额列: {amount_columns}")
    print(f"  日期列: {date_columns}")

    # 如果未提供输出文件路径，自动生成
    if output_file is None:
        file_dir = os.path.dirname(input_file)
        file_name = os.path.basename(input_file)
        name, ext = os.path.splitext(file_name)
        output_file = os.path.join(file_dir, f"{name}-output{ext}")

    # 自动检测输入文件编码
    input_encoding = detect_file_encoding(input_file)
    print(f"使用编码读取文件: {input_encoding}")

    try:
        # 读取CSV文件（使用检测到的编码）
        df = pd.read_csv(input_file, encoding=input_encoding)
    except UnicodeDecodeError as e:
        print(f"使用编码 {input_encoding} 读取失败: {e}")
        print("尝试使用其他常见编码...")

        # 尝试其他常见编码
        alternative_encodings = ["gbk", "gb2312", "utf-8", "latin1", "iso-8859-1"]
        for alt_encoding in alternative_encodings:
            if alt_encoding == input_encoding:
                continue
            try:
                df = pd.read_csv(input_file, encoding=alt_encoding)
                print(f"成功使用编码: {alt_encoding}")
                input_encoding = alt_encoding
                break
            except UnicodeDecodeError:
                continue
        else:
            raise Exception("无法找到合适的编码读取文件，请手动指定编码")

    # 处理金额列
    for col in amount_columns:
        if col in df.columns:
            print(f"处理金额列 '{col}'...")
            df[col] = df[col].apply(format_amount)
        else:
            print(f"警告: 配置的金额列 '{col}' 不存在于CSV文件中")

    # 处理日期列
    for col, target_format in date_columns.items():
        if col in df.columns:
            print(f"处理日期列 '{col}'，目标格式: {target_format}...")
            df[col] = df[col].apply(lambda x: format_date(x, target_format))
        else:
            print(f"警告: 配置的日期列 '{col}' 不存在于CSV文件中")

    # 保存转换后的CSV文件（强制使用UTF-8编码）
    try:
        df.to_csv(output_file, index=False, encoding="utf-8")
        print(f"转换完成！输出文件: {output_file} (UTF-8编码)")
    except Exception as e:
        print(f"保存文件时出错: {e}")
        # 如果UTF-8保存失败，尝试UTF-8-SIG（带BOM的UTF-8）
        try:
            df.to_csv(output_file, index=False, encoding="utf-8-sig")
            print(f"转换完成！输出文件: {output_file} (UTF-8-SIG编码)")
        except Exception as e2:
            print(f"UTF-8-SIG保存也失败: {e2}")
            # 最后尝试原始编码
            df.to_csv(output_file, index=False, encoding=input_encoding)
            print(
                f"转换完成！输出文件: {output_file} (使用输入文件编码: {input_encoding})"
            )


def main():
    """主函数，处理命令行参数"""
    parser = argparse.ArgumentParser(description="转换CSV文件中的格式")
    parser.add_argument("input_file", help="输入CSV文件路径")
    parser.add_argument("create_config", action="store_true", help="创建示例配置文件")
    parser.add_argument("-o", "--output", help="输出CSV文件路径（可选）")
    parser.add_argument("-c", "--config", help="配置文件路径（可选）")

    # 解析命令行参数
    args = parser.parse_args()

    # 如果指定了创建配置文件，则创建并退出
    if args.create_config:
        create_sample_config()
        return

    # 检查输入文件是否存在
    if not os.path.exists(args.input_file):
        print(f"错误：输入文件 '{args.input_file}' 不存在")
        sys.exit(1)

    # 调用转换函数
    convert_csv_format(args.input_file, args.output, args.config)


def create_sample_config():
    """创建示例配置文件"""
    sample_config = {
        "amount_columns": [
            "金额",
            "价格",
            "费用"
        ],
        "date_columns": {
            "交易时间": "YYYY-MM-DD HH:mm:ss",
            "数据日期": "YYYY-MM-DD",
            "创建时间": "YYYY/MM/DD HH:mm:ss",
            "更新日期": "YYYY/MM/DD"
        }
    }
    
    config_filename = "config.json"
    
    try:
        with open(config_filename, 'w', encoding='utf-8') as f:
            json.dump(sample_config, f, ensure_ascii=False, indent=4)
        print(f"已创建示例配置文件: {config_filename}")
        print("请根据您的CSV文件结构修改此配置文件。")
    except Exception as e:
        print(f"创建配置文件失败: {e}")


# 使用示例
if __name__ == "__main__":
    # 如果有命令行参数，使用命令行参数
    if len(sys.argv) > 1:
        main()
    else:
        # 否则使用交互式输入（兼容旧版本）
        input_csv = input("请输入输入文件路径: ").strip().strip('"')

        if not os.path.exists(input_csv):
            print(f"错误：文件 '{input_csv}' 不存在")
            sys.exit(1)

        output_option = (
            input("请输入输出文件路径（直接回车将自动生成）: ").strip().strip('"')
        )
        output_csv = output_option if output_option else None
        
        config_option = (
            input("请输入配置文件路径（直接回车使用默认配置）: ").strip().strip('"')
        )
        config_file = config_option if config_option else None

        convert_csv_format(input_csv, output_csv, config_file)