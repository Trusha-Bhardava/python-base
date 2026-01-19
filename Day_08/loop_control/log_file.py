# this is log file example
#automating log file

log_file= [
    "INFO : operation sucess",
    "ERROR : file not found",
    "DEBUG : Connection Established",
    "ERROR : Database connection failed"
]

for line in log_file:
    if "ERROR" in line:
        print(line)