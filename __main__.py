import rasterio
import numpy as np 
import os
import argparse
import time
import sys
import zipfile

class ComposeRaster:

    def __init__(self):
        print('Initializing...')

        self.bandCount=int(args.Band_Count)
        self.dataPath=os.path.join(os.path.dirname(__file__), args.Data_Folder)
        self.outPath=os.path.join(self.dataPath, args.Output_File.append('.tif'))
        self.bandData=[]

    def dataConfig(self):
        print('Validating Data Paths...')

        if os.path.exists(self.dataPath):
            if os.path.exists(self.outPath):
                os.remove(self.outPath)
        else:
            os.mkdir(data_path)
            print('Please Copy Zipped Raster Files To: {}'.format(self.dataPath))
            print('Tool Exit In 5 Seconds')
            time.sleep(5)
            exit()

    def getData(self, zip_file):
        pass

    def listArchives(self):
        print('Listing Data Archives...')

        pattern=re.compile('.zip')
        file_list=re.search(pattern, os.listdir(self.data_path))
        if len(file_list)==self.bandCount:
            if not len(file_list)<2:
                for zip_file in file_list:
                    getData(zip_file)
            else:
                raise ValueError('Multiband Rasters Take 2 Or More Bands')
        else:
            raise ValueError('{} Bands Specified: {} Bands Found'.format(self.bandCount, len(file_list)))

    def writeRaster(self):
        pass


def main():
    compose=ComposeRaster()
    compose.dataConfig()
    compose.listArchives()
    compose.writeRaster()

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--Data_Folder', default='Data', help='Folder Containing Zipped Raster Bands')
    parser.add_argument('Band_Count', help='Number Of Bands To Be Included In The Raster')
    parser.add_argument('Output_File', help='Name of Output Multiband Raster File (Without File Extension)')
    args=parser.parse_args()
    main()