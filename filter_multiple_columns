if __name__ == '__main__':
    from pandas import DataFrame, Series
    from random import randint
    from time import time

    def filter(df, dct):
        """

        :param df: DataFrame for filtering
        :param dct: dict (keys = column of DataFrame, values = filter str)
        :return: filtered DataFrame
        """
        result = Series(data=[True for item in range(df.shape[0])])
        for item in dct:
            x = df[item].astype('str').str.contains(dct.get(item))
            result = result & x
        return df[result]

    t_start = time()
    size = 100 # shape of DataFrame

    dct = dict({'first': '1', 'second': '1', 'third': '1'}) # dict for filter

    lst_data = [[randint(0,1), randint(0,1), randint(0,1)] for i in range(size)] # data for DataFrame for filtering
    lst_column = ['first', 'second', 'third'] # column of DataFrame
    df = DataFrame(data=lst_data, columns=lst_column) # DataFrame for filtering
    print(filter(df, dct=dct)) # filtered

    print(time() - t_start)
