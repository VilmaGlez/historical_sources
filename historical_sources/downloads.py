import sysconfig
import gdown
import shutil

cwd = str(sysconfig.get_paths()["purelib"]) + '/historical_sources'

def download_results(default=True,link=None):
    if default is True:
        url = "https://drive.google.com/drive/folders/1vPt_QbACi960J8Ocy6iIWfUcd76a7Vrr?usp=share_link"
        gdown.download_folder(url, quiet=True, use_cookies=False)
        url1 = "https://drive.google.com/drive/folders/10q0jIksGyZ0PmxWIwkBx4a8X02ufVpVS?usp=share_link"
        gdown.download_folder(url1, quiet=True, use_cookies=False)
        shutil.move('results_final',cwd)
        shutil.move('datasets',cwd)
    else:
        gdown.download_folder(link, quiet=True, use_cookies=False)



