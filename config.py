from validate_email import validate_email
import logging
import sys

logger = logging.getLogger()

def get_config(args):
    l, m, to = args.latent_factors, args.method.lower(), args.to

    if m not in ['auto', 'sgd', 'als', 'adagrad']:
        logger.critical('Unknown solver. Quiting...')
        sys.exit(1)

    for email in to:
        if not validate_email(email):
            logger.critical('Invalid email {}'.format(email))
            sys.exit(1)
    return vars(args)
