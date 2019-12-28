try:

    from google.cloud import storage
    import pandas as pd
    import io
    from io import BytesIO
except Exception as e:
    print("Some Modules are Misisng {}".format(e))


class DF(object):

    def __init__(self, df):
        """
        object to Compress Pandas Dataframe into Object
        :param df: Pandas DataFrame
        """
        self.data = df


class Stack(object):
    """
    Stack Data Structure
    """

    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.data ==[]:
            return None
        else:
            return self.data.pop()

    def isEmpty(self):
        return self.data == []


class GCPCsvHunt(object):

    def __init__(self, bucketName = '', path=''):
        """

        :param bucketName: String
        :param path: Path to your Json File
        """
        self.path = path
        self.storage_client = storage.Client.from_service_account_json(self.path)
        self.bucketName = bucketName
        self.bucket = self.storage_client.get_bucket(self.bucketName)
        self.stack = Stack()

    def getAllCSV(self, prefix=''):

        """

        :return: Stack Object
        """

        filename = list(self.bucket.list_blobs(prefix=prefix))          # Finds all File

        for name in filename:                                           # Iterate over all Files
            if '.csv' in str(name.name):                                # Search for csv

                print("Crawling on File {} ...........".format(name.name))

                blop = self.bucket.blob(blob_name = "{}".format(name.name))

                data = blop.download_as_string()

                df = pd.read_csv(io.BytesIO(data), encoding='utf-8', sep=",")

                obj = DF(df)

                self.stack.push(obj)
            else:
                pass

        return self.stack


# if __name__ == "__main__":
#
#     pathToJsonFile = 'JSON FILE '
#     BucketName = 'BUCKET NAME '
#     prefix = ''             # Searches in Outer Directory
#
#     obj = GCPCsvHunt(path=pathToJsonFile, bucketName=BucketName)
#
#     data = obj.getAllCSV(prefix=prefix)         # Return list of Objects
#
#     df1 = data.pop()                            # Pop the First Pandas Object
#     print(df1.data)                             # Print Pandas Data Frame
#











