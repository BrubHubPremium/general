"""
Created on Wed Sep 12 10:13:21 2018

@author: Anibal Solon
"""

def anicor(matrix1, matrix2):
    d1 = matrix1.shape[-1]
    d2 = matrix2.shape[-1]

    def zscore(data, axis):
        data -= data.mean(axis=axis,keepdims=True)
        data /= data.std(axis=axis,keepdims=True)
        return np.nan_to_num(data, copy=False)

    assert d1 == d2
    assert matrix1.ndim <= 2
    assert matrix2.ndim <= 2

    matrix1 = zscore(matrix1.astype(float), matrix1.ndim - 1) / np.sqrt(d1)
    matrix2 = zscore(matrix2.astype(float), matrix2.ndim - 1) / np.sqrt(d2)

    if matrix1.ndim >= matrix2.ndim:
        r = np.dot(matrix1, matrix2.T)
    else:
        r = np.dot(matrix2, matrix1.T)
       
    r = np.clip(r, -1.0, 1.0)

    return r
