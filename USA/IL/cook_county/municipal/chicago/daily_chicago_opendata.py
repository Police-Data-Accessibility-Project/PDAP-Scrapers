import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from common import opendata_scraper2

save_url = [
    ["crimes/2001-present/", "https://data.cityofchicago.org/resource/ijzp-q8t2.csv"],
    ["arrests/", "https://data.cityofchicago.org/resource/dpt3-jri9.csv"],
]

save_folder = "./data/"

# Optional argument `save_subfolder` allows saving in a subfolder
# Optional argument `sleep_time` should be set to the site's crawl-delay,
# which can be found in their robots.txt file_name, default time is 1
opendata_scraper2(save_url, save_folder, sleep_time=1, socrata=True)
