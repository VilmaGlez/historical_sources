import sysconfig
import gdown
import shutil

cwd = str(sysconfig.get_paths()["purelib"]) + '/historical_sources'

def download_results(default=True,link=None):
    if default is True:
        url = "https://drive.google.com/drive/folders/1VLjR9oBWR8FoyTEsQbDGqbtQS8uEJ4u_?usp=share_link"
        gdown.download_folder(url, quiet=True, use_cookies=False)
        url1 = "https://drive.google.com/drive/folders/1smyfEMsWFzUtmVeRL64Yv5MnFB_hvqk9?usp=share_link"
        gdown.download_folder(url1, quiet=True, use_cookies=False)
        shutil.move('results_final',cwd)
        shutil.move('datasets',cwd)
    else:
        gdown.download_folder(link, quiet=True, use_cookies=False)



