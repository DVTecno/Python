from ftplib import FTP

server='ftp.dlptest.com'
user='dlpuser'
password='rNrKYTX9g7z3RgJRmxWuGHbeu>'
dir='movies'
ftp_connection=FTP(server)
result=ftp_connection.login(user,password)
print(f"{result}")
result=ftp_connection.mkd('movies')
print(f"Crear directorio {result}")
ftp_connection.cwd(dir)
print(f"Cambia al directorio {result}")
with open('movies.csv','rb') as movies_file:
    result=ftp_connection.storbinary('Stor movies.csv',fp=movies_file)
    print(result)


result=ftp_connection.cwd('/cities')
print(f"Cambia al directorio {result}")
with open('uscites.csv','wb') as cities_file:
    result=ftp_connection.retrbinary('RETR uscites.csv',cities_file.write)
    print(result)    
    

