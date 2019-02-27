from gentextfile import oat
from gentextfile import zipdir
from gentextfile import gcs_upload_file
from gentextfile import gcs_dowload_file
import zipfile
import argparse

if __name__ == "__main__":

    #ag = argparse.ArgumentParser()
    #ag.add_argument('--version', type=str, default="1.0.0")
    #args = ag.parse_args()

    #if args.version:
    #    version = args.version
    #oat("C:/Users/Anuchit/Desktop/kowoatkowoatz", version)

    #zipf = zipfile.ZipFile('C:/Users/Anuchit/Desktop/kowoatz.zip', 'w')
    #zipdir('C:/Users/Anuchit/Desktop/kowoatkowoatz', zipf)

    gcs_bucket = "dmp_recommendation_dev"
    gcs_dowload_file(gcs_bucket, "kowoatz/abc.zip", "C:/Users/Anuchit/Desktop/defg.zip")

    #1. Bucketname 2. path/of/localfile 3.path/of/remotefile
    gcs_upload_file(gcs_bucket, "C:/Users/Anuchit/Desktop/defg.zip", "kowoatz/defg.zip")