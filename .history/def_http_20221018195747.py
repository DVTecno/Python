list_ip=dict() #Dict {io_addres1:count(ip_addres1),ip_addres2:count(ip_addres2),...}
list_error=dict() #Dict. {status_code:count(status_code1),status_code2:count(status_code2),...}
file_name="log20170630.csv"

#Identifica si en el log hay un HTTP Status Code ded error
def iserror(status_code):
    if (status_code.isnumeric() and int(status_code)>400):
        return True
    return False

#Si la ip ya esta en el log suma uno a la cantidad de veces que se observe
def countIP(ip):
    if ip in list_ip:
        list_ip[ip]+=1
    else:
        list_ip[ip]=1

#Si el HTTP Status Code ya esta en el log suma uno la cantidad de veces que se observe en el error
def countError(error):
    if error in list_error:
        list_error[error]+=1
    else:
        
