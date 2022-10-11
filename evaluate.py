import can
import csv
import sys

def main(argv):
    filename = sys.argv[1]
    log = can.BLFReader(filename)
    log = list(log)

    log_output = []

    for msg in log:
        msg = str(msg)
        log_output.append(['0',msg[11:27],'0x'+msg[41:44],msg[76:99].replace(" ", "")])

    outFile = filename.replace('.blf', '.can')
    with open(outFile, "w", newline='') as f:
        writer = csv.writer(f,delimiter=',', quotechar='', quoting=csv.QUOTE_NONE)
        writer.writerows(log_output)

if __name__ == "__main__":
   main(sys.argv[1:])