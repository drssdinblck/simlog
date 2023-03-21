import simlog.log


simlog.log.info('This is an info text')
simlog.log.warn('This is a warning')
simlog.log.error('This is an error')

try:
    raise AssertionError('Nasty Exception')
except AssertionError as error:
    simlog.log.error(error)
