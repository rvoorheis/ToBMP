__author__ = 'rvoorheis'

import os
import sys
import getopt


class PrintParameters:
    """
    Obtain runtime parameters
    """
#   wbInputFileName = "input.zpl"   #Name of input ZPL File
#
#   printerIPAddress = "10.80.22.72"          #IP Address of online printer

    wbInputFileName = ""  # Name of input zpl file

    printerIPAddress = ""  # Address of printer to use

    printLabel = False     # Should we print the label too?

    def __init__(self, argv):

        try:
            opts, args = getopt.getopt(sys.argv[1:], 'h:d:p', ['help', 'debug', 'print'])

        except getopt.GetoptError as e:
            print("GetoptError " + str(e))
            self.usage()
            sys.exit(2)
        try:
            if len(opts) >> 0:
                for opt, arg in opts:
                    if opt in ("-h", "--help"):
                        self.usage()
                        sys.exit()
                    elif opt in ('-p', '--print'):
                        self.printLabel = True
                    elif opt in ('-d', '--debug'):
                        _debug = True

            self.wbInputFileName = args[0]
            self.printerIPAddress = args[1]

 #           self.Display_parameters

        except LookupError as e:
            print("Lookup Error " + str(e))
            quit(-4)

        except StandardError as e:
            print("Error! - Standard Error = " + str(e))
            quit(-3)

        except Warning as e:
            print("Warning " + str(e))
            quit(-1)

    def Display_parameters(self):
        print ("Input     = " + self.wbInputFileName)
        print ("Printer IP Addr  = " + self.printerIPAddress)
        if self.printLabel:
            print("Print Label")


    def usage(self):
            print "TB - To BMP"
            print ""
            print "Sends the ZPL file to the designated printer and creates a .bmp of the image that would be printed"
            print " "
            print "TB <input ZPL file Name>   <Ip Address of Printer>"
            print ""
