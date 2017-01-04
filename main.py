def read_file():
    dict_data = {}
    with open("nginx.log") as data:  # Reading the .log file
        for line in data:
            line = line.split('"')  # spliting with '"'
            time_line = line[6].split(' ')
            time_took = 0
            url_line = line[1].split(' ')
            try:
                url = url_line[1]
            except:
                url = url_line[-1]
            try:
                time_took = float(time_line[2])
            except ValueError:
                pass
            if url not in dict_data:
                dict_data[url] = [1, time_took]
            else:
                dict_data[url][0] += 1
        print dict_data
        for key, value in dict_data.items():
            print "\n" + ">> " + key + ": " + str(value) + "\n" + "=" * 35


read_file()
