


def GetBblCouner():
    fileName = "bblProfiling.log"
    bblCounter = dict()
    with open(fileName, "r") as f1:
        for line in f1:
            counter = line[15:-1]
            counter = int(counter)
            addr = line[0:8]
            addr = str.upper(addr)
            bblCounter[addr] = counter
    print "Read [%s] complited!" % fileName
    return bblCounter


def FiltLowerThanTenTimes():
    fileName = "bblTracing.log"
    outFileName = "bbl.log"
    outLower = "lower.log"        # Log lower than 10 times
    fd = open("Error.log", "w")   # Log error
    fo = open(outLower, "w")
    bblCounter = GetBblCouner()
    f2 = open(outFileName, "w")
    debug_i = 0
    i = 0
    c1 = 0
    c2 = 0
    times = 0
    strBuf = ""
    with open(fileName, "r") as f1:
        for line in f1:
            c1 += 1
            i += 1
            addr = line[0:8]
            addr = str.upper(addr)
            try:
                counter = bblCounter[addr]
                tmp = "%08s: %d" % (addr, counter)

                if counter < 10: 
                    fo.write(tmp + "\n")
                    continue
                c2 += 1
                
                strBuf += tmp + "\n"
                if i >= 100000 :
                    times  += 1
                    f2.write(strBuf)
                    f2.flush()
                    var = "Read:[%06d], Write:[%06d], WriteTimes:[%04d]" % (c1, c2, times)
                    print var
                    i = 0
                    strBuf = ""
                
            except Exception as exp:
                debug_i += 1
                log = "[%04dth]: Block [%s] is not in dict!\n" % (debug_i, addr)
                fd.write(log)
                if debug_i % 10000 == 0 : fd.flush()
    fd.write(debug_i)
    fd.close()
    f2.close()
    fo.close()
    print "Read total line: %d. " % c1
    print "Write total line: %d. " % c2
    print "Write to file [%s] completed!"


def Main():
    #try:
        print "Staring..."
        FiltLowerThanTenTimes()
        print "Finish!"
    #except Exception as exp:
        print "Error: " + str(exp)
    #input("Press any key to continue.")


Main()