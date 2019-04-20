# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

import requests
import shutil

@click.command()
@click.argument('output_filepath', type=click.Path(exists=True))
def main(output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('Getting data from web')   
    
    urls  = ["https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data/downloads/GlobalLandTemperaturesByMajorCity.csv/2", 
             "https://www.kaggle.com/carrie1/ecommerce-data/downloads/ecommerce-data.zip/1"
             ]
             
    files = ['GlobalLandTemperaturesByMajorCity.csv', 
             'ecommerce-data.zip']

    for i in range (len(files)):
        r = requests.get(urls[i], stream=True)
        if r.status_code == 200:
            with open(output_filepath+"/"+files[i], "wb") as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()