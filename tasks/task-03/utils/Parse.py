import sys
import getopt


class Parse:
    INIT = 2

    def __init__(self):

        if len(sys.argv[1:]) == 0:
            self._help()
            sys.exit()

        self.params = {
            'rho': None,
            'theta': None,
            'threshold': None,
            'take': None,
        }
        self.filename = sys.argv[Parse.INIT - 1]

        argv = sys.argv[Parse.INIT:]
        opts, args = getopt.getopt(argv, '-h', ['help', 'rho=', 'theta=', 'threshold=', 'take=',])
        self._get_opts(opts)
        self._get_args(args)

    def get(self, key):
        if key in self.params.keys():
            return self.params[key]

        return None

    def get_valid_parameters(self, context='accumulator'):
        keys = ['rho', 'theta',]

        if context == 'detector':
            keys = ['threshold', 'take',]

        return {key: value for key, value in self.params.items() if value is not None and key in keys}

    def _help(self):
        print('Exemplos de uso:')
        print('    python main.py images/test_01.png 180 180 30')
        print('    python main.py images/test_01.png --rho=180 --theta=180 --threshold=30')
        print('    python main.py images/test_01.png --rho=180 180 --threshold=30')
        print()
        print('Parâmetros:')
        print('    -h --help     Exibe os parâmetros aceitos pelo script')
        print('    --rho=<valor para rho>')
        print('    --theta=<valor para theta>')
        print('    --threshold=<valor para threshold>')
        print('    --take=<valor que limita a quantidade de linhas> (Esse parâmetro excluí o threshold)')
        pass

    def _get_opts(self, opts):
        for opt, arg in opts:
            if opt in ['-h', '--help']:
                self._help()
                sys.exit()

            self.params[opt[2:-1]] = int(arg)

    def _get_args(self, args):
        keys_empty = [key for key, value in self.params.items() if value is None]

        for arg in args:
            if len(keys_empty) == 0:
                pass

            self.params[keys_empty.pop(0)] = int(arg)
