                                e4=sda2[e2:e3]
                                
                                block=block+1 
                                
                                if assxw==e3%12 or assxw==e3%10:
                                            if e4=="1":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4=""  
                                       
                                      
                                            if e4=="1":
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""   
                                               
                                            elif e4=="1" and e3== e3%10:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                
                                            elif e4=="1" and e3== e3%11:
                                                sda3=sda3+"0"
                                                e4="1"
                                                e4=""
                                                
                                                    
                                            elif e4=="1":
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                
                                            elif e4=="0":
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""
                                                    
                                                    
                                            if e4=="0":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4="" 
                                            elif e4=="1":
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""   
                                               
                                            elif e4=="1" and e3== e3%3:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                
                                            elif e4=="1" and e3== e3%2:
                                                sda3=sda3+"0"
                                                e4="1"
                                                e4=""
                                                
                                                    
                                            elif e4=="1":
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                
                                            elif e4=="0":
                                                sda3=sda3+"1"
                                                e4="1"
                                                e4=""
                                    
                                    
                                    
                                            elif e4=="1" and e3== e3%9:
                                                    sda3=sda3+"0"
                                                    e4="1"
                                                    e4=""
                                                
                                            elif e4=="1" and e3== e3%8:
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4=""
                                                
                                                    
                                            elif e4=="1" and e3 ==e3%1:
                                                    sda3=sda3+"0"
                                                    e4="0"
                                                    e4=""
                                                    
                                            elif e4=="1" and e3 ==e3%1:
                                                    sda3=sda3+"0"
                                                    e4="1"
                                                    e4=""
                                                    
                                                    
                                                    
                                            elif e4=="0":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4="" 
                                            elif e4=="1":
                                                sda3=sda3+"1"
                                                e4="1"
                                            if assxw==e3%2 or assxw==e3%10:
                                            	if e4=="1":
            	                                    sda3=sda3+"0"
            	                                    e4="0"
            	                                    e4=""  
                                               
                                              
            	                                if e4=="1":
            	                                    
            		                           
                                             

                                
                                                   if e4=="1" and e3== e3%7:
                                                    	sda3=sda3+"0"
                                                    	e4="0"
                                                    	e4=""
                                                        
                                                   elif e4=="1" and e3== e3%16:
                                                        sda3=sda3+"0"
                                                        e4="1"
                                                        e4=""
                                                    
                                                   elif e4=="1" and e3== e3%15:
                                                    	sda3=sda3+"0"
                                                    	e4="0"
                                                    	e4=""
                                                        
                                                   elif e4=="1" and e3== e3%14:
                                                        sda3=sda3+"0"
                                                        e4="1"
                                                        e4=""
                                                        
                                               
                                                   elif e4=="1" and e3== e3%13:
                                                    	sda3=sda3+"0"
                                                    	e4="0"
                                                    	e4=""

                                
                                if e4=="1" and e3== e3%9+assxw:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                
                                elif e4=="1" and e3== e3%8+assxw:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                elif e4=="1" and e3== e3%7+sw2:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="1" and e3== e3%8+assxw:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                elif e4=="1" and e3== e3%7+sw2:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="1" and e3== e3%6+sw2:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""   
                                
                                elif e4=="1" and e3== e3%7+sw1:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="1" and e3== e3%6+sw1:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                elif e4=="1" and e3== e3%7+sw:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="1" and e3== e3%6+sw:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                
                                elif e4=="1" and e3== e3%5+sw:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                elif e4=="1" and e3== e3%2+sw7:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4="" 
                                elif e4=="1" and e3== e3%2+sw6:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4="" 
                                
                                elif e4=="1" and e3== e3%18+sw6:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""	
                                elif e4=="1" and e3== e3%18+sw6:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                elif e4=="1" and e3== e3%17+sw6:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                    
   
                                elif e4=="1" and e3== e3%4+sw4:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                    
                           
                                elif e4=="1" and e3== e3%3+sw4:
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""                                  
                                elif e4=="1" and e3== e3%4+sw:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                    
                           
                                elif e4=="1" and e3== e3%3+sw:
                                	sda3=sda3+"0"
                                	e4="0"
                                elif e4=="1" and e3== e3%23+n or e4=="1" and e3== e3%23+n1 or e4=="q" and e3== e3%23+n2:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""	
                                 
                                elif e4=="1" and e3== e3%22+n1:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                                                        
                                elif e4=="1" and e3== e3%2+sw:
                                    sda3=sda3+"0"
                                    e4="1"
                                    e4=""
                                    
                                        
                                elif e4=="1":
                                	sda3=sda3+"0"
                                	e4="0"
                                	e4=""
                                    
                                elif e4=="0":
                                    sda3=sda3+"1"
                                    e4="1"
                                    e4=""          
          
 
	                                                  
                                e2=e2+1
                                e3=e3+1

                                e4=""
                          
                                if e3==cvf:
                                    e2=0
                                    e3=1
                                    
                                    cvf=sw
                                    cvf=sw1
                                    cvf=sw2
                                    cvf=sw3
                                    sw=sw+n+3
                                    sw1=sw1+n+4
                                    sw2=sw2+n+1
                                    sw3=sw3+n+3
                                    
                                    sw4=sw4+n
                                    
                                    n=n+7
                                    
                                    sw5=sw4+n
                                    
                                    n1=n1+5
                                    
                                    sw5=sw4+n1
                                    
                                    sw4=sw4+n1
                                    
                                    sw=sw+n+3
                                    sw1=sw1+n1+4
                                    sw2=sw2+n1+1
                                    sw3=sw3+n1+3
                                    
                                    sw5=sw4+n
                                    
                                    n1=n1+5
                                    
                                    sw6=sw4+n2
                                    
                                    sw6=sw6+n2
                                    
                                    sw=sw+n+3
                                    sw1=sw1+n2+1
                                    sw2=sw2+n2+3
                                    sw3=sw3+n2+2
                                    
                                    n2=n2+8
                                    
                                    n3=n3+2
                                    sw7=n3
                                    
                             
                                if cvf==lenf5*8+4:
                                    sw=sw+1
                                    cvf=c
                                    cvf1=cvf1+1
                                     
                                    c=c+2
