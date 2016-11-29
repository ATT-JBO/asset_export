import argparse
import att_event_engine.att as att
import csv
import datetime
import dateutil.parser


def valid_date(s):
    try:
        dateVal = dateutil.parser.parse(s)
        return s
    except:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--asset", help="The id of the asset who's data needs to be exported", required=True)
parser.add_argument("-u", "--user", help="The username to connect with", required=True)
parser.add_argument("-p", "--password", help="The password for the user", required=True)
parser.add_argument("-o", "--output", help="The name of the output file, default = export.csv", default='export.csv')
parser.add_argument("-s", "--start", help="start date of the query (default = 1900-1-1", default="1900-1-1", type=valid_date)
parser.add_argument("-e", "--end", help="end date of the query (default = now()", default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), type=valid_date)
args = parser.parse_args()


iot = att.HttpClient()
iot.connect_api(args.user, args.password, "api.allthingstalk.io")

done = False
page = 0
with open(args.output, 'wb') as fp:
    writer = csv.writer(fp)  # , delimiter=';'
    while not done:
        res = iot.get_history(args.asset, args.start, args.end, page)
        writer.writerows([[rec["at"], rec["data"]] for rec in res['data'] if rec])
        page += 1
        done = 'next' not in res['links']

print ("done")