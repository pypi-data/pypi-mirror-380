import logging
logger=logging.getLogger('Well Analysis')
logging.getLogger('sixgill').setLevel(logging.WARNING)
logging.getLogger('sixgill.core').setLevel(logging.WARNING)
logging.getLogger('sixgill.core.run_or_start_simulation').setLevel(logging.ERROR)
logging.getLogger('manta.server.manager').setLevel(logging.WARNING)