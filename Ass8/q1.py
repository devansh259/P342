import lib

rand1=lib.random_walk(100,250)
print("For steps=250 and walks=100:")
print("average displacement in x=",rand1[4])
print("average displacement in y=",rand1[5])
print("average radial displacement=",rand1[2])
print("RMS value=",rand1[3])

rand2=lib.random_walk(500,500)
print("For steps=250 and walks=500:")
print("average displacement in x=",rand2[4])
print("average displacement in y=",rand2[5])
print("average radial displacement=",rand2[2])
print("RMS value=",rand2[3])

rand3=lib.random_walk(500,750)
print("For steps=250 and walks=500:")
print("average displacement in x=",rand3[4])
print("average displacement in y=",rand3[5])
print("average radial displacement=",rand3[2])
print("RMS value=",rand3[3])

rand4=lib.random_walk(500,1000)
print("For steps=250 and walks=500:")
print("average displacement in x=",rand4[4])
print("average displacement in y=",rand4[5])
print("average radial displacement=",rand4[2])
print("RMS value=",rand4[3])

rand5=lib.random_walk(500,1250)
print("For steps=250 and walks=500:")
print("average displacement in x=",rand5[4])
print("average displacement in y=",rand5[5])
print("average radial displacement=",rand5[2])
print("RMS value=",rand5[3])



#Output

#For steps=250 and walks=100:
#average displacement in x= -0.4285086312663815
#average displacement in y= 0.6916993902962707
#average radial displacement= 14.072725413029264
#RMS value= 15.846424088732036

#For steps=500 and walks=500:
#average displacement in x= 0.23697681297703116
#average displacement in y= -0.9871919954990156
#average radial displacement= 20.4051521443709
#RMS value= 22.95385391946089

#For steps=750 and walks=500:
#average displacement in x= -0.8379721882528
#average displacement in y= 1.1672138959788758
#average radial displacement= 24.214991546183164
#RMS value= 27.318380138427

#For steps=1000 and walks=500:
#average displacement in x= 0.15712026676077157
#average displacement in y= 0.2950720463239402
#average radial displacement= 28.894961354475836
# RMS value= 32.42378944073995

#For steps=1250 and walks=500:
#average displacement in x= 1.1986067255746515
#average displacement in y= -0.5016239371813802
#average radial displacement= 31.84001701139064
#RMS value= 35.79296754500416
