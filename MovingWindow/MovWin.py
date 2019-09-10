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

# MovingWindow
# ============
#
# In this module, a moving (or sliding, or rolling) window algorithm for
# filtering/processing signals is implemented. It has been created in
# order to serve as a tool in 1D signal processing. There are many
# different situations (find envelopes, trends, smooth or even normalize a
# signal) where a sliding window along with a properly selected metric
# (mean, max, min, rms, std, etc.) will do a great job.
#
# Dependencies
# ~~~~~~~~~~~~
#
# This module depends on three different packages:
#
#   * NumPy
#   * SciPy 
#   * InputCheck
#
# The first two packages are known to everyone interested in data science.
# Something like:
#
#   `pip install <packageName>`
#
# or
#
#   `conda install <packageName>`
#
# if you use Anaconda or Miniconda will do the job.
#
# For the installation of the third package please read the corresponding
# `README.md <https://github.com/ekarakasis/InputCheck/blob/master/README.md>`__
#
# Installation
# ~~~~~~~~~~~~
#
# To install this package just download the repository from GitHub or by
# using the following command line:
#
#   `git clone https://github.com/ekarakasis/MovingWindow`
#
# Afterwards, go to the local root folder, open a command line and run:
#
#   `pip install .`
#
# **NOTE:** *Do not forget the dot punctuation mark (“.”) in the end of
# the “pip install .” command*
#
# Run the Tests
# -------------
#
# To run the tests just go to the *root/MovingWindow/tests* folder, open a
# command line and write:
#
#   `python test_all.py`
#
# License
# -------
#
# This project is licensed under the MIT License.

import sys
sys.path.append('../')
sys.path.append('../../')

from MovingWindow import allowedWindows
from MovingWindow import get_window, np
from MovingWindow import acceptedTypes, acceptedValues, functionType, enableChecks, chkCmds


def SlidingWindow(signal, windowSize, step=1):
    """A generator, which results in the sliding window values

    Parameters
    ----------
    signal : numpy.ndarray
        The actual signal we want to process.

    windowSize : int
        The size of the moving/sliding window.
    
    step : int
        The step that determines the overlap percentage of 
        two consecutive windows.

    Yields
    ------
    numpy.ndarray
        The moving window values.
    """

    # a pad is created in order to deal with potential edges issues
    signal = np.pad(signal, (int((windowSize-1)/2),
                             int((windowSize-1)/2)), 'reflect')

    numOfChunks = int(((len(signal)-windowSize)/step)+1)

    for i in range(0, numOfChunks*step, step):
        yield signal[i:i+windowSize]


@acceptedTypes(np.ndarray, int, int, functionType, str, bool, typesCheckEnabled = enableChecks)
@acceptedValues(
    chkCmds.noCheck, 
    chkCmds.MinV(2), 
    chkCmds.MinV(1), 
    chkCmds.noCheck,
    chkCmds.SetV(allowedWindows), 
    chkCmds.noCheck,
    valueCheckEnabled = enableChecks,
)
def MovingWindow(signal, windowSize=16, step=1, metric=np.mean, window='box', normalizedWindow=False):
    """Applies a moving window-based processing on the input signal.

    In this function, a moving (or sliding, or rolling) window algorithm for
    filtering/processing signals is implemented. It has been created in
    order to serve as a tool in 1D signal processing. 

    Parameters
    ----------
    signal : numpy.ndarray
        The actual signal we want to process.

    windowSize : int
        The size of the moving window. This input must have value greater 
        than or equal to 2.

    step : int
        Determines the overlap percentage of two consecutive windows. 
        This input must have value greater than or equal to 1.

    metric : <class 'function'>
        A function which is applied to each window 
        (e.g. for a *moving average* the metric must be <np.mean\>).

    window : str
        The window type we want to apply. The allowed window types are:

            * box
            * gaussian
            * nuttall
            * hanning
            * hann
            * hamming
            * blackman
            * blackmanharris

    normalizedWindow : bool
        When this flag is True, the selected window (e.g. hann) is 
        normalized so as the sum of its elements to be equal to 1.

    Raises
    ------
    TypeError
        If any input has different type.
    ValueError
        If any input has value different than the expected.

    Returns
    -------
    numpy.ndarray    
        The function returns a moving window-based processed signal.
    """    
    
    # we want the window size to be odd number like 3, 5, 7, etc.
    if windowSize % 2 == 0:
        windowSize = windowSize + 1

    if window == 'box':
        WT = get_window('boxcar', windowSize, fftbins=False)
    elif window == 'gaussian':
        WT = get_window(('gaussian', windowSize/6), windowSize, fftbins=False)
    else:
        WT = get_window(window, windowSize, fftbins=False)

    if normalizedWindow:
        WT = WT / np.sum(WT)

    out = []
    outa = out.append    
    for item in SlidingWindow(signal, windowSize, step):        
        # here we apply the window and then the metric
        outa(metric(item*WT))

    return np.array(out) 