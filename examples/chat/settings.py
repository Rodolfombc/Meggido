file = open("connection.txt","r")
for line in file.readlines():
    line = line.strip()
    if line.startswith("#"): continue

    try:
        line = line.split(" = ")
        if line[0] == "ip":
            ip = line[1][1:-1]
        elif line[0] == "port":
            port = int(line[1])
    except:
        print("Invalid line: \""+line+"\"!")
file.close()

client_timeout_connect = 5.0
client_timeout_receive = 10.0

scrollback = 100
