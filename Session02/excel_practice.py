import pyexcel
a_list_of_dictionaries = [
     {
         "Title": 'Troi dep',
         "Link": "http://google.com.vn"
     },
     {
          "Title": 'Troi dep',
          "Link": "http://google.com.vn"
     },
     {
          "Title": 'Troi dep',
          "Link": "http://google.com.vn"
     },
     {
         "Title": 'Troi dep',
         "Link": "http://google.com.vn"
     }
 ]

pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="Excel_practice.xls")
