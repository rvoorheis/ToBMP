__author__ = 'rvoorheis'
# -*- encoding: UTF-8 -*-
"""
Requires Python27 and zebra.
"""
#import PrintParameters
import os
from StringIO import StringIO
import sys
import PrintParameters
from zebra.io.unity import SocketConnection
from zebra.proto.parser.grf import parse_grf_to_image

def main(argv):
    # coding=utf-8

    import os
    global debug  # debug flag

    debug = False

    try:
        parms = PrintParameters.PrintParameters(argv)
        parms.Display_parameters()

        fileName = parms.wbInputFileName
        
        file = open(fileName, 'r')

        Label = file.read()
        # print (Label)
        # print Label.__len__()

        # Need to strip off any trailing "^XA^IDR:GED42000.GRF^FS^XZ" strings
        Done = False
        while not Done:
            LabelLength = Label.__len__()
            if LabelLength > 26:

                while Label[LabelLength - 1] == "\n":
                    Label = Label[0:LabelLength-1]
                    LabelLength = LabelLength - 1
                #end loop

                if Label[LabelLength - 26:LabelLength - 20] == "^XA^ID" and Label[LabelLength - 6:LabelLength] == "^FS^XZ":
                    Label = Label[0:LabelLength-27]
                else:
                    Done = True
                #end if

            else:
                Done = True
            #end if

        #end loop:

#       print (Label[0:LabelLength-4])

        if parms.printLabel:
            Label = Label[0:LabelLength - 4] + ('^HCY, , , , ,Y^XZ')
        else:
            Label = Label[0:LabelLength - 4] + ('^HCN, , , , ,Y^XZ')
        # print (Label)
        labelname = fileName[:fileName.__len__() - 4] + '.bmp'

        createBMP(labelname, Label, parms.printerIPAddress)

    except LookupError as e:
        print("Lookup Error " + str(e))
        quit(-2)

    except NameError as e:
        print("Error! - Invalid Filename = " + str(e))
        quit(-3)

    except StandardError as e:
        print("Error! - Standard Error = " + str(e))
        quit(-3)

    except Warning as e:
        print("Warning " + str(e))
        quit(-1)

    return True

def createBMP (lname, LABEL, ipAddr):

    printer = SocketConnection(ipAddr, 9100)

    printer.send(LABEL)

    grf_data = printer.collect_sincelast(2.0, 60.0)
    _, printer_img = parse_grf_to_image(StringIO(grf_data))

    printer_img.save(lname, 'BMP')
    printer.disconnect()
    print (lname + ' created')

    return()

if __name__ == "__main__":
    main(sys.argv[1:])