# Allow module to have flexibility - can be used standalone or used by other modules

import module
print(__name__)

module.hello()
if __name__ == '__main__':
    print('Running this module directly')
else:
    print("Running other module indirectly")