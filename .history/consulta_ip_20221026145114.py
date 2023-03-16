list_ip=dict()        #dict.{pi_addres1:count(ip_addres1,ip_addres2:count(ip_addres2),...}
list_error=dict()     #dict.status_code:count(status_code1),code2:count(status-code),...}

file_name='log20170630.csv'

#Identifica si en el log hay un HTTP Status Code de error
def iserror(status_code):
    if (status_code.isnumeric() and int(status_code)>400):
        return True
    return False

#Si la ip ya esta en el log suma uno a la cantidad de veces que se observe la ip
def countIP(ip):
    if ip in list_ip:
        list_ip[ip]+=1
    else:
        list_ip[ip]=1

#Si el HTTP Status Code ya esta en log suma uno a la cantidad de veces que se le observe el error
def countError(error):
    if error in list_error:
        list_error[error]+=1
    else:
        list_error[error]=1

print(f"Procesando fichero de log {file_name}...")
with open(file_name,'r') as logfile:
    for line in logfile:
        evento=line.split(sep=',')
        countIP(evento[0])
        if iserror([7][0:3]):
            countError(evento[7][0:3])

print('Lista de direcciones IP')
print(list_ip)
print('\n\n')
print('Lista de codigos de error')




