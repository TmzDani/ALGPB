n = int(input('informe o codigo: '))
res = []
z_str = str(n) 

for i in range(len(z_str)): 
    if n_str[i] == '1':  
        res.append('um') 
    elif n_str[i] == '2':  
        res.append('dois')
    elif n_str[i] == '3':  
        res.append('três') 
    elif n_str[i] == '4':  
        res.append('quatro')  
    elif n_str[i] == '5':  
        res.append('cinco') 
    elif n_str[i] == '6':  
        res.append('seis') 
    elif n_str[i] == '7':  
        res.append('sete') 
    elif n_str[i] == '8':  
        res.append('oito') 
    elif n_str[i] == '9':  
        res.append('nove') 
    else: 
        res.append('zero') 
print(res)