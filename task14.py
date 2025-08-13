
import csv
import openpyxl

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#HfO2_TiN_fixed_NK.csv
#06_12_24_HfO2_TiN_5nm.csv
#pre_list=list()
#post_list=list()

with open("06_12_24_HfO2_TiN_5nm.csv", "r" , newline = '') as f:
    pre = (csv.reader(f,delimiter=","))
    
    with open("06_12_24_HfO2_TiN_5nm.csv", "r" , newline = '') as f:
        post = (csv.reader(f,delimiter=","))
        
        #nnn = 49
        nn = 49 # количество_выводимых_точек
        #n = nn + 4
        n2 = nn + 3
        
        s = 20 # количество_выводимых_слоев
        
        i = 0
        x = 0
        
        i2=0
        x2=0 
        
        #pre_list=list()
        line=list()
        newl = list()
        
        #book=openpyxl.Workbook()
        book = openpyxl.open("text.xlsx")    
        #sheet=book.active
        #sheet = book.worksheets[1]
        sheet = book["Лист4"]
        
        i3 = 2
        i4 = 2
        
        i5 = 2
        j = 0
        j2 = 0
        float(j2)
        
        j3 = 0
        
        r = 0
        
        #line_bt = 0.0 
        #(float(line_bt))
        xx = list()
        yy = list()
        zz = list()
        zzz = list()
        
        
        
        max = 0.0
        min = 1000000.0
        
        for line , newl in zip(pre,post):
            
            
            if i in range(0,4):       
            
                if 'Company:' in line  and i == 0:    
                    x += 1
                    print("x = ",x)
            
            line_bt = 0.1 
            (float(line_bt)) 
            
            if x == 1 and i > 3:
                print(line[0],line[1],line[2],line[7],line[8])
                
                
                
                line2 = [int(line[0])]
                line3 = [float(line[1])]
                line4 = [float(line[2])]
                
                line5 = [float(line[8])]
                line6 = [float(line[7])]
                
                #xx.append(line3)
                for p in line3:
                    xx.append(p)
                for p2 in line4:
                    yy.append(p2)
                    
                line_bt = line5[0]
                
                sheet["A"+str(i3)].value = (line2[0])
                sheet["B"+str(i3)].value = (line3[0])
                sheet["C"+str(i3)].value = (line4[0])
                
                sheet["G"+str(i3)].value = (line5[0])
                sheet["H"+str(i3)].value = (line6[0])
                
                i3 += 1
                print("i = ",i)
                
                print("line_bt = ",line_bt)
                
                
            if x == 0:
                print(line[0],line[2],line[9])
                
                sheet["G"+str(i3)].value = ''.join(line[2])
                sheet["H"+str(i3)].value = ''.join(line[9])
                 
                i3 += 1    
                print("i = ",i)  
                  
            i += 1
            
                    
            #===========================================
            
            newl_bt = 0.1 
            (float(newl_bt))
            
               
            if i2 in range(0,4):       
            
                if 'Company:' in (newl)  and i2 == 0:
                    x2 += 1
                    print("x2 = ",x2)
            
            
            if x2 == 1 and i2 > 3:
                print(newl[0],"|",newl[1],"|",newl[2],"|",newl[7],"|",newl[8])
                
                newl2 = [int(newl[0])]
                newl3 = [float(newl[1])]
                newl4 = [float(newl[2])]
                
                newl5 = [float(newl[8])]
                newl6 = [float(newl[7])]
                
                newl_bt = newl5[0]


                sheet["A"+str(i4)].value = (newl2[0])
                sheet["B"+str(i4)].value = (newl3[0])
                sheet["C"+str(i4)].value = (newl4[0])
                
                sheet["J"+str(i4)].value = (newl5[0])
                sheet["K"+str(i4)].value = (newl6[0])
                
                i4 += 1
                
                #if i2 > n2:
                #    break 
                
                print("newl_bt = ",newl_bt)
                
            
            if x2 == 0 and i2 <= (n2 + 4):
                print(newl[0],newl[2],newl[9])
                
                sheet["J"+str(i4)].value = ''.join(newl[2])
                sheet["K"+str(i4)].value = ''.join(newl[9])
                
                i4 += 1    
                print("i2 = ",i2)
                
            i2 += 1
           
        
            if i > 4 and i2 > 4 :
                sheet['N1'] = "DELTA BT"
                
                bt = [((line_bt) + (newl_bt))]
                print ("bt = ",bt)
                for bt2 in bt:
                    sheet["N"+str(i5)].value = bt2
                    
                    
                    
                er = ([((line_bt) + (newl_bt) + (bt2)) * 3])
                print ("er = ",er)
                
                
                for er2 in er:
                    if max < er2:
                        max = er2
                    if min > er2:
                        min = er2
                    sheet["D"+str(i5)].value = er2
                    zz.append(er2)    
                
                 
                    
                j3 += 1
                i5 += 1
                
                
                if i2 > n2:
                    break 
        
        print("max = ",max)
        print("min = ",min)
        
                
        print("x = ",xx) 
        print("y = ",yy)
        print("z = ",zz) 
        
        max = float(input("введите_Максимум "))
        min = float(input("введите_Минимум "))
         
        #zzz = list() 
        #k = 0.0  
        
        k2 = 0.0
        #k2 = float(k2)
        #k2 = list()
        
        
        
        l = 0 
         
        for k in zz:
            
            if k < min:
                k = min
                zzz.append(k)
                
            if k > max:
                k = max
                zzz.append(k)
            
                
            if k >= min and k <= max:
                zzz.append(k)
            
            l += 1
            print("l = ",l)    
            print("k = ",k)
            
        print("zzz = ",zzz)      
            
        fig, ax = plt.subplots()
        c2 = ax.tricontourf(xx, yy, zzz, s , cmap = "bwr")
        plt.colorbar(c2)
        plt.savefig("myplot.png", dpi = 100)
        img = openpyxl.drawing.image.Image('myplot.png')
        sheet.add_image(img, "Q10")            
                
        
                
        
       
        
        
        
        
        
        i7 = 2
        i8 = 1

        sheet['B1'] = 'X (mm)'
        sheet['C1'] = 'Y (mm)'
        sheet['A1'] = 'Number'
        sheet['D1'] = 'ER А/мин'
    
        sheet['F1'] = 'PRE'
        sheet['I1'] = 'POST'
        
        sheet['G1'] = 'layer_2_thickness(A)'
        sheet['H1'] = 'nGOF'
        
        sheet['J1'] = 'layer_2_thickness(A)'
        sheet['K1'] = 'nGOF'

        sheet['R1'] = 'PRE'
        sheet['S1'] = 'POST'
        sheet['T1'] = 'ER А/мин'

        sheet['Q2'] = 'СРЗНАЧ'
        sheet['Q3'] = '3 сигма, %'
        sheet['Q4'] = 'Мин'
        sheet['Q5'] = 'Макс'
        sheet['Q6'] = 'Сигма'
        sheet['Q7'] = 'Сигма%'
        
        sheet['R2'].value = '=SUM(D2:D50)'
        sheet['R3'].value = '=R7*3'
        sheet['R4'].value = '=MIN(D2:D50)'
        sheet['R5'].value = '=MAX(D2:D50)'
        sheet['R6'].value = '=СТАНДОТКЛОН.В(D2:D50)'
        sheet['R7'].value = '=D2/D50*100' 

        sheet['S2'].value = '=SUM(G2:G50)'
        sheet['S3'].value = '=S7*3'
        sheet['S4'].value = '=MIN(G2:G50)'
        sheet['S5'].value = '=MAX(G2:G50)'
        sheet['S6'].value = '=СТАНДОТКЛОН.В(G2:G50)'
        sheet['S7'].value = '=G2/G50*100'
        
        sheet['T2'].value = '=SUM(J2:J50)'
        sheet['T3'].value = '=J7*3'
        sheet['T4'].value = '=MIN(J2:J50)'
        sheet['T5'].value = '=MAX(J2:J50)'
        sheet['T6'].value = '=СТАНДОТКЛОН.В(J2:J50)'
        sheet['T7'].value = '=J2/J50*100'
        
        
        book.save("text.xlsx")
        #book.save("result_book2.xlsx")
        book.close