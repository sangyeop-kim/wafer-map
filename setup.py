from S3 import AWS_s3
from glob import glob
import zipfile
import os


if __name__ == '__main__':
    aws = AWS_s3()
    aws.download('PUBLIC/wafer-map/dataset.zip', 'dataset.zip')
    zip_ = zipfile.ZipFile('dataset.zip')
    zip_.extractall('.')
    zip_.close()
    os.remove('dataset.zip')
    print('complete unzip!!!!!!!!!!!')