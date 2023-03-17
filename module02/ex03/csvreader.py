

class CsvReader():

    # with __init__(...) as x:
    #     # here, calling x is the same as __enter__
    ## after the with block, __exit__ is called.
 
    def __init__(self, filename=None, sep=",", header=False, skip_top=0, skip_bottom=0):
        
        self.file_obj = open(filename, 'r')
        if sep == "":
            raise ValueError
        self.sep = sep
        self.header = header
        if skip_top < 0 or skip_bottom < 0:
            raise ValueError
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        
        # utils
        self.header_data = []
        self.data = []

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """

        self.header = self.getheader()        
        lines = self.file_obj.readlines()

        for line in lines[slice(self.skip_top, len(lines) - self.skip_bottom - 1)]:
            self.data.append(line[:-1].split(self.sep))

        return self.data

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if self.header and len(self.header_data) == 0:
            self.header_data = str(self.file_obj.readline())[:-1].split(self.sep)
            if self.skip_top == 0:
                self.skip_top = 1
            
        return self.header_data

if __name__ == "__main__":

    with CsvReader("addresses.csv", ",", True) as file:
        data = file.getdata()
        header = file.getheader()
        print(f"data: {data}")
        print(f"header: {header}")

    with CsvReader("addresses.csv", ",", False, 1, 1) as file:
        data = file.getdata()
        header = file.getheader()
        print(f"data: {data}")
        print(f"header: {header}")

    with CsvReader("crash_catalonia.csv", ",", True, 1, 2) as file:
        data = file.getdata()
        header = file.getheader()
        print(f"data: {data}")
        print(f"header: {header}")
