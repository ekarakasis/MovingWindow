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

import numpy as np
from scipy.signal import get_window
from InputCheck.InputCheckDecorators import acceptedTypes, acceptedValues

allowedWindows = [
    'box',
    'gaussian',
    'nuttall',
    'hanning',
    'hann',
    'hamming',
    'blackman',
    'blackmanharris'
]

functionType = type(np.mean)

# ****************************
enableChecks = True # <-- change it to False in order to deactivate the MovingWindow function's arguments check
# ****************************

# helpful call that will be used in the InputCheck decorators
# for argument type and value checking
class chkCmds:
    noCheck = {'command': 'noCheck'}
    
    @staticmethod
    def MinV(minValue):
        return {'minValue': minValue}

    @staticmethod
    def MaxV(maxValue):
        return {'maxValue': maxValue} 

    @staticmethod
    def RngV(rangeValue):
        return {'range': rangeValue}

    @staticmethod
    def SetV(setV):
        return {'set': setV}

