import sys
import os
import configs_ISR as configs
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))
from common import list_pdf_v2

save_dir = "./data/ISR/"

list_pdf_v2(configs, save_dir)
