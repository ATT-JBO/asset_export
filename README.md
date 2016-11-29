# asset export
A command line tool for exporting raw asset data to csv file format

## Installation

- copy the files to a directory
- run `pip install -r requirements.txt`

## usage
- view all the application arguments and explenation:  
`python export.py -h`
- export all the data for an asset:  
`python export.py -a {assetId} -u {username} -p {pwd}`
- export data between a date range:
`python export.py -a {assetId} -u {username} -p {pwd} - s YYYY-MM-DD hh::mm:sss - e YYYY-MM-DD hh::mm:sss`
- specify the name of the output file:
`python export.py -a {assetId} -u {username} -p {pwd} -o {filename}`

Note: hh:mm:ss are optional for the date arguments.

##Current limitations
Only assets with simple data formats (integer, number, boolean, string) will be exported correctly at the moment. Json objects and arrays will be exported as json data.
