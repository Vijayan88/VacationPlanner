import os
import json
import tempfile
import time
class CollectLatLongDetails(object):
    
    DEFAULT_MAX_NO_RECORDS = 10000
    
    @classmethod
    def create(cls, data_store_path=None, max_no_records=1):
        print 'Creating an instance of ', __name__
        cls.data_loc = data_store_path
        # buffer
        cls.input_records = list()
        if not os.path.isdir(data_store_path):
            cls.data_loc = os.getcwd()
        if not max_no_records or max_no_records < cls.DEFAULT_MAX_NO_RECORDS:
            cls.max_no_records = cls.DEFAULT_MAX_NO_RECORDS
        else:
            cls.max_no_records = max_no_records
    
    @classmethod
    def save(cls, data):
        try:
            json_obj = json.loads(data)
            if len(cls.input_records) > cls.max_no_records:
                # write buffer into local storage
                file_name = os.path.join(cls.data_loc,str(time.time()))
                print json_obj
                with open(file_name, "w+") as geo_data:
                    for row in cls.input_records:
                        geo_data.write(json.dumps(row))
                        geo_data.write('\n')
                print 'saving data at ', file_name
                geo_data.close()
                cls.input_records = list()  # clear buffer
            cls.input_records.append(json_obj)
            print 'Saved successfully'
            return 'Saved successfully'
        except ValueError as json_err:
            print 'Not able to read json data', str(json_err)
            return 'Not able to read json data', str(json_err)
        except IOError as io_err:
            print 'Something wrong with creating file', str(io_err)
            return 'Something wrong with creating file', str(io_err)