#  ==================================================================================
#
#  Copyright (c) 2018, Evangelos G. Karakasis
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#
#  ==================================================================================

import sys
sys.path.append('../')
sys.path.append('../../')

import unittest
from MovWin import np
from MovWin import MovingWindow

class Tests_MovingWindow(unittest.TestCase):
    signal_ndarray = np.array(list(range(100)))
    signal_wrong = [1, 2, 3, 'some txt']
    signal_list = list(range(100))
    signal_string = 'this is a dummy text used for unit testing'

    def test_MovingWindow_01_signal(self):
        MovWinParams = {
            'signal': self.signal_ndarray,
            'windowSize': 16,
            'step': 1,
            'metric': np.mean,
            'window': 'box',
            'normalizedWindow': False,
        }

        # ndarray signal
        signal_p = MovingWindow(**MovWinParams)
        # wrong signal
        with self.assertRaises(TypeError):
            MovWinParams.update({'signal': self.signal_wrong})
            signal_p = MovingWindow(**MovWinParams)
        # ndarray signal
        MovWinParams.update({'signal': self.signal_ndarray})
        signal_p = MovingWindow(**MovWinParams)
        # string signal
        with self.assertRaises(TypeError):
            MovWinParams.update({'signal': self.signal_string})
            signal_p = MovingWindow(**MovWinParams)
   

    def test_MovingWindow_02_windowSize(self):
        MovWinParams = {
            'signal': self.signal_ndarray,
            'windowSize': 16,
            'step': 1,
            'metric': np.mean,
            'window': 'box',
            'normalizedWindow': False,
        }

        # very small window size
        with self.assertRaises(ValueError):
            MovWinParams.update({'windowSize': 1})
            signal_p = MovingWindow(**MovWinParams)
        # negative window size
        with self.assertRaises(ValueError):
            MovWinParams.update({'windowSize': -10})
            signal_p = MovingWindow(**MovWinParams)
        # zero window size
        with self.assertRaises(ValueError):
            MovWinParams.update({'windowSize': 0})
            signal_p = MovingWindow(**MovWinParams)
        # extremely large window size
        # and of course extremely large run time :)
        MovWinParams.update({'windowSize': 1000000})
        signal_p = MovingWindow(**MovWinParams)
        # wrong windowSize type - string
        with self.assertRaises(TypeError):
            MovWinParams.update({'windowSize': 'some text'})
            signal_p = MovingWindow(**MovWinParams)
    

    def test_MovingWindow_03_metric(self):
        MovWinParams = {
            'signal': self.signal_ndarray,
            'windowSize': 16,
            'step': 1,
            'metric': np.mean,
            'window': 'box',
            'normalizedWindow': False,
        }

        # wrong metric - string
        with self.assertRaises(TypeError):
            MovWinParams.update({'metric': '123'})
            signal_p = MovingWindow(**MovWinParams)
        # wrong metric - number
        with self.assertRaises(TypeError):
            MovWinParams.update({'metric': 321})
            signal_p = MovingWindow(**MovWinParams)
        # wrong metric - empty list
        with self.assertRaises(TypeError):
            MovWinParams.update({'metric': []})
            signal_p = MovingWindow(**MovWinParams)
        # wrong metric - incorrect list
        with self.assertRaises(TypeError):
            MovWinParams.update({'metric': [1, 2, 'asd']})
            signal_p = MovingWindow(**MovWinParams)
    

    def test_MovingWindow_04_window(self):
        MovWinParams = {
            'signal': self.signal_ndarray,
            'windowSize': 16,
            'step': 1,
            'metric': np.mean,
            'window': 'box',
            'normalizedWindow': False,
        }

        # wrong window type - string
        with self.assertRaises(ValueError):
            MovWinParams.update({'window': 'dummy'})
            signal_p = MovingWindow(**MovWinParams)
        # wrong window type - number
        with self.assertRaises(TypeError):
            MovWinParams.update({'window': 123})
            signal_p = MovingWindow(**MovWinParams)


    def test_MovingWindow_05_step(self):
        MovWinParams = {
            'signal': self.signal_ndarray,
            'windowSize': 16,
            'step': 1,
            'metric': np.mean,
            'window': 'box',
            'normalizedWindow': False,
        }

        # wrong step type - string
        with self.assertRaises(TypeError):
            MovWinParams.update({'step': 'some text'})
            signal_p = MovingWindow(**MovWinParams)
        # wrong step type - zero value
        with self.assertRaises(ValueError):
            MovWinParams.update({'step': 0})
            signal_p = MovingWindow(**MovWinParams)
        # wrong step type - negative
        with self.assertRaises(ValueError):
            MovWinParams.update({'step': -1})
            signal_p = MovingWindow(**MovWinParams)


    def test_MovingWindow_06_normalizedWindow(self):
        MovWinParams = {
            'signal': self.signal_ndarray,
            'windowSize': 16,
            'step': 1,
            'metric': np.mean,
            'window': 'box',
            'normalizedWindow': False,
        }

        # wrong normalizedWindow type - string
        with self.assertRaises(TypeError):
            MovWinParams.update({'normalizedWindow': 'some text'})
            signal_p = MovingWindow(**MovWinParams)
        # wrong normalizedWindow type - number
        with self.assertRaises(TypeError):
            MovWinParams.update({'normalizedWindow': 32})
            signal_p = MovingWindow(**MovWinParams)

if __name__ == '__main__':
    unittest.main()
