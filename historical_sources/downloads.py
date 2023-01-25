import sysconfig
import gdown
import shutil

cwd = str(sysconfig.get_paths()["purelib"]) + '/historical_sources'

def download_results():
    url = "https://drive.google.com/drive/folders/1C8XPmpCFkuHmKT2O4vjhsPSHgBSFkZ4g?usp=share_link"
    gdown.download_folder(url, quiet=True, use_cookies=False)

download_results()
shutil.move('results_final',cwd)
