from dataclasses import dataclass


@dataclass
class Dataset:
    id: str

    @classmethod
    def upload_dataframe(cls, _transport, dataframe, name):
        return cls(_transport.upload_dataframe(dataframe, name))

    @classmethod
    def upload_csv(cls, _transport, pathname, name):
        return cls(_transport.upload_csv(pathname, name))

    @classmethod
    def upload_excel(cls, _transport, pathname, sheet_name, name):
        return cls(_transport.upload_excel(pathname, sheet_name, name))
