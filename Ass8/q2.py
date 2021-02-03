import lib





X,Y,Z,volume,err=lib.ellipsoid(1,1.5,2,10000)

print("volume of ellipsoid=",volume)
print("Fractional error in volume=",err)

#Output
#volume of ellipsoid= 12.5952
#Fractional error in volume= 0.0022941696155201192

