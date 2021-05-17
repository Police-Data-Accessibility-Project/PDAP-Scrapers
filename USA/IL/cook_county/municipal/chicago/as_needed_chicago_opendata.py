import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper2

save_url = [
    ["foia_log/police/", "https://data.cityofchicago.org/resource/wjkc-agnm.csv"],
    ["foia_log/police_board/", "https://data.cityofchicago.org/resource/9pd8-s9t4.csv"],
    ["foia_log/ipra", "https://data.cityofchicago.org/resource/gzxp-vdqf.csv"],
    ["foia_log/cpl/", "https://data.cityofchicago.org/resource/n379-5uzu.csv"],
]
save_folder = "./data/"

# Optional argument `save_subfolder` allows saving in a subfolder
# Optional argument `sleep_time` should be set to the site's crawl-delay,
# which can be found in their robots.txt file_name, default time is 1
opendata_scraper2(save_url, save_folder, sleep_time=1, socrata=True)
