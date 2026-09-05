import os

PROJECT_ROOT  = r"D:\Quant\Multi_factor_project"
DATA_RAW      = os.path.join(PROJECT_ROOT, "data", "raw")
DATA_CLEAN    = os.path.join(PROJECT_ROOT, "data", "clean")
FACTORS_DIR   = os.path.join(PROJECT_ROOT, "factors")
OUTPUT_DIR    = os.path.join(PROJECT_ROOT, "output")

# 请在环境变量中设置 TUSHARE_TOKEN，或直接在本地的 config.py 中填入你的token
# 本文件仅作为配置模板，不包含真实token
TUSHARE_TOKEN = os.environ.get("TUSHARE_TOKEN", "your_token_here")