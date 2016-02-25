from __future__ import print_function
import matplotlib as mpl
mpl.use('Agg') # Don't open display

import matplotlib.pyplot as plt
import numpy as np
import io
import logging
import graphlab as gl
from datetime import datetime
from termcolor import colored, cprint
import mailer
import os
import json

logger = logging.getLogger()

def run(conf):
    to = conf['to']
    method = conf['method']
    latent_factors = list(range(1,conf['latent_factors']+1))
    path = conf['path']
    plot_filename = str(datetime.utcnow())

    logger.info('Reading ratings.csv ...')
    movies = gl.SFrame.read_csv(os.path.join(path, 'ratings.csv'),
            column_type_hints=[int,int,float,int])
    logger.info('Reading complete')

    data = []
    logger.info('Training model ...')
    for i in latent_factors:
        m = gl.recommender.factorization_recommender.create(movies,
                                                     user_id='userId',
                                                     item_id='movieId',
                                                     target='rating',
                                                     num_factors=i,
                                                     solver=method,
                                                     verbose=False)
        logger.info('Processing... {0}'.format(i))
        rmse = m.get('training_rmse')
        data.append(rmse)

    plt.plot(latent_factors, data)
    plt.xlabel('Number of latent factors')
    plt.ylabel('RMSE')
    plt.title('Number of latent factors in comparsion with RMSE')

    logger.info('Saving plot to disc ...')
    plt.savefig('{0}.svg'.format(plot_filename))
    logger.info('Save complete')

    buf = io.BytesIO()
    plt.savefig(buf, format = 'svg')
    buf.seek(0)

    mail = mailer.Mailer(os.path.join('./Credentials','credentials.json'))
    mail.send(
            toaddrs=to,
            fromaddrs='christopher.lillthors@gmail.com',
            subject='Recommender engine',
            body='Method used = {0}\nLatent_factors = {1}'.format(method,
                len(latent_factors)),
            payload=('{0}.svg'.format(plot_filename), buf))
