r = open("DC.txt", "r")
w = open("mapped.txt","w")

num = 0
for line in r:
	data = line.strip().split("	")
	if len(data) == 49:
		        ID,BATHRM,HF_BATHRM,HEAT,AC,NUM_UNITS,ROOMS,BEDRM,AYB,YR_RMDL,EYB,STORIES,SALEDATE,PRICE,QUALIFIED,SALE_NUM,GBA,BLDG_NUM,STYLE,STRUCT,GRADE,CNDTN,EXTWALL,ROOF,INTWALL,KITCHENS,FIREPLA$$IREPLACES,USECODE,LANDAREA,GIS_LAST_MOD_DTTM,SOURCE,CMPLX_NUM,LIVING_GBA,FULLADDRESS,CITY,STATE,ZIPCODE,NATIONALGRID,LATITUDE,LONGITUDE,ASSESSMENT_NBHD,ASSESSMENT_SUBNBHD,CENSUS_TRACT,CENSUS,$CENSUS_BLOCK,WARD,SQUARE,X,Y,QUADRANT=data
	w.write("{0}\t{1}\n".format(PRICE,SQUARE)
