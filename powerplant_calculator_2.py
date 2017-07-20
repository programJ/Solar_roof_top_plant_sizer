import sys
import math
import texttable as tt
from texttable import Texttable, get_color_string, bcolors

#########################################################################################################################################Input parameters
global EN_cons			#kWh/year
global Rs_cons			#rs/year
global area_bool
global Avbl_area		#sq. ft
global Rs_kWh			#Rs/kWh
global EN_purchase_rate
global place
global state
global Irradiation 		#kWh/m2/day
global Dsrd_size
global Instl_rate		#rs/kW
global Depr_rate		#%compund growth
global EN_rate_incrmt		#% compund growth
global Govt_subsidy		#boolen
global ctrl_gov_percentage
global S_Govt_subsidy		#boolen
global Panel_efficiency		#%
global hours_in_day
global days_in_year
global years_of_operation
global show_type



EN_cons = 0			#kWh/year
Rs_cons = 0			#rs/year
area_bool = True		#bollen
Avbl_area = 0			#sq. ft
Rs_kWh = 7.00			#Rs/kWh
EN_purchase_rate = 3.22		#Rs/kWh
place = "surat"			#city
state = "Gujarat"		#state
Irradiation = 5.35 		#kWh/m2/day
Dsrd_size = 0.00		#kW
Instl_rate = 69000.00		#rs/kW
Depr_rate = 7.00		#%compund growth
EN_rate_incrmt = 3.00		#%compund growth
Govt_subsidy = True		#boolen
ctrl_gov_percentage = 30.00	#%
S_Govt_subsidy = True		#boolen
Panel_efficiency = 15.00	#%
hours_in_day = 6.00		#hours
days_in_year = 360.00		#days
years_of_operation = 25.00	#years
show_type = "normal"

#################################################################################################################################################Supportive
def find( str , cmmd ):
	if cmmd in str:
		return True
	else:
		return False

def float2(x):
	return float("{0:.2f}".format(x))

def comma(x):
	return ("{:,}".format(x))

def round5(x):
	a=int(x)
	b=float(x)-a
	if (b>0.75):
		x=a+1.0
	elif (b>0.25):
		x=a+0.5
	else:
		x=a
	return x
	
def printc(c,string):
	if (c == 'b'):
		x=bcolors.BLUE
	elif (c == 'r'):
		x=bcolors.RED
	elif (c == 'y'):
		x=bcolors.YELLOW
	elif (c == 'g'):
		x=bcolors.GREEN
	elif (c == 'w'):
		x=bcolors.WHITE			
	print (get_color_string(x,string))

def is_number(s):
	try:
		float(s)
		return True
		
	except ValueError:
		return False	

def input_number():
	while 1:				
		ki=input()									#type of variable
		if (ki == ''):
			return ki								
		elif (not is_number(ki)):
			printc ('r', "please give NUMERICAL input : ")
			continue
		else:
			return ki
		
def input_str():
	while 1:				
		ki=input()									#type of variable
		if (ki == ''):
			return ki								#type of variable
		elif (is_number(ki)):
			printc ('r', "please give input in ENGLISH ALPHABETS: ")
			continue
		else:
			return str(ki)		
		


################################################################################################################################################Initiatation
def adv_init():									#to change defaults only
	print ("Welcome to Advance settings")
	print ("To change the value of the corresponding name shown, enter the VALUE.\t\t\tTo skip (retain the value) press ENTER")
	print ("To start the advance setup press ENTER")
	while 1:
		ki=str(input_str())
		if ki=='':
			break
		else:
			printc ('r',"Press ENTER to continue")
	
	global Rs_kWh			
	global EN_purchase_rate
	global place
	global state
	global Irradiation 		
	global Instl_rate		
	global Depr_rate		
	global EN_rate_incrmt		
	global Govt_subsidy	
	global ctrl_gov_percentage
	global S_Govt_subsidy	
	global Panel_efficiency		
	global hours_in_day
	global days_in_year
	global years_of_operation

	
	
	########################################################################################
	##Rs_kWh
	printc ('y',"Rs per kWh consumed :")
	printc ('w',"Current electricity cost which you are paying, selling rate of provider")
	printc ('b',"Current value : "+str(Rs_kWh)+" Rs/kWh")
	while 1:
		ki=input_number()
		if ki=='':
			break
		else:
			Rs_kWh = float(ki)
			break			
	
	##ENergy purchase rate
	printc ('y',"Rs per kWh at which excess generated energy will be purchased by provider")
	printc ('w',"Excess electricity purchase rate of provider as per goverment policy")
	printc ('b',"Current value : "+str(EN_purchase_rate)+" Rs/kWh")
	while 1:
		ki=input_number()
		if ki=='':
			break
		else:
			EN_purchase_rate = float(ki)
			break
	
	##state
	printc ('y',"State where the plant belongs")
	printc ('w',"Name of state")
	printc ('b',"Current value : "+str(state))
	while 1:
		ki=str(input_str())
		if ki=='':
			break
		else:
			state = str(ki)
			break	
	
	##city
	printc ('y',"Place of your expected plant")
	printc ('w',"Name of city")
	printc ('b',"Current value : "+str(place))
	while 1:
		ki=str(input_str())
		if ki=='':
			break
		else:
			place = str(ki)
			break	
	
	##Irradiation
	printc ('y',"Irradiation at Place of your expected plant (in kWh per sq.mt per day)")
	printc ('w',"Total Energy insolation on unit area in a day")
	printc ('b',"Current value : "+str(Irradiation)+" kWh per sq.mt per day" )
	while 1:
		ki=input_number()
		if ki=='':
			break
		elif (float(ki) > 0):
			Irradiation = float(ki)
			break
		elif (float(ki) == 0):
			print ("It's not profitable to generate electricity from photovoltanic cells with insolation from artificial light source. Please enter non-zero positive value")
			continue	
		else:
			print ("Irradiation can not be negative. Please enter a non-zero positive value")	
			continue		
	
	##Instl_rate
	printc ('y',"Installation cost per kW (in Rs per kW)")
	printc ('w',"Average cost of a unit plant")
	printc ('b',"Current value : "+str(Instl_rate)+" Rs per kW" )
	while 1:
		ki=input_number()
		if ki=='':
			break
		elif (float(ki) >= 0):
			Instl_rate = float(ki)
			break
		else:
			print ("You have entered negative value. Please enter a Non-negative value")	
			continue
			
	##Depr_rate
	printc ('y',"Depriciation rate (in %)")
	printc ('w',"Depriciation rate or bank interest rate, or possible gain through some other source")
	printc ('b',"Current value : "+str(Depr_rate)+"%" )
	while 1:
		ki=input_number()
		if ki=='':
			break
		elif (float(ki) >= 0):
			Depr_rate = float(ki)
			break
		else:
			print ("You have entered negative value. \nIf it is intentional press ENTER\nIf you want to change the value type the right value again")
			Depr_rate = float(ki)
			continue	
	
	##EN_rate_incrmt
	printc ('y',"Electrivity price increment rate (in %)")
	printc ('w',"Increment in Electricity rate (consumption) yearly as compound increment")
	printc ('b',"Current value : "+str(EN_rate_incrmt)+"%" )
	while 1:
		ki=input_number()
		if ki=='':
			break
		elif (float(ki) >= 0):
			EN_rate_incrmt = float(ki)
			break
		else:
			print ("You have entered negative value. \nIf it is intentional press ENTER\nIf you want to change the value type the right value again")
			EN_rate_incrmt = float(ki)
			continue	
			
	##Govt_subsidy
	printc ('y',"Want to take benefit of goverment policy or not?")
	printc ('w',"Central government gives "+str(ctrl_gov_percentage)+"% subsidy for domestic solar roof top plants.\nIf don't want to be beneficiery type 'no' or 'False'")
	printc ('b',"Current value : "+str(Govt_subsidy))
	while 1:
		ki=input_str()
		if ki=='':
			break
		else:
			if (ki == 'no' or ki == 'False'): 
				Govt_subsidy = False
				break
			else:
				print ("I think you mis-spelled. Please Type your answer again)")
				continue
	
	if (Govt_subsidy):	
		##ctrl_gov_percentage
		printc ('y',"Subsidy Given by Central Government (in % of Installation cost)")
		printc ('b',"Current value : "+str(ctrl_gov_percentage)+"%" )
		while 1:
			ki=input_number()
			if ki=='':
				break
			else:
				ctrl_gov_percentage = float(ki)
				break
		
		printc ('y',"Want to take benefit of State goverment policy or not?")
		printc ('w',"State goverment policy is complex, and have less benifits")
		printc ('b',"Current value : "+str(S_Govt_subsidy))
		while 1:
			ki=input_str()
			if ki=='':
				break
			else:
				if (ki == 'no' or ki == 'False'): 
					S_Govt_subsidy = False
					break
				else:
					print ("I think you mis-spelled. Please Type your answer again)")
					continue
		
	
	##Panel_efficiency		
	printc ('y',"Panel efficiency (in %)")
	printc ('b',"Current value : "+str(Panel_efficiency)+"%" )
	while 1:
		ki=input_number()
		if ki=='':
			break
		elif (float(ki) > 0):
			Panel_efficiency = float(ki)
			break
		elif (float(ki) == 0):
			print ("It's impossible to use solar panels with zero efficiency. Please enter non-zero positive value")
			continue	
		else:
			print ("It's not profitable to use panels with negative efficiency. Please enter a non-zero positive value")	
			continue					
	
	##hours_in_day		
	printc ('y',"Effective no. of plant operation hours in a day (in hours)")
	printc ('b',"Current value : "+str(hours_in_day)+" hours in a day" )
	while 1:
		ki=input_number()
		if ki=='':
			break
		elif (float(ki) > 0):
			hours_in_day = float(ki)
			break
		elif (float(ki) == 0):
			print ("Please enter non-zero number of hours")
			continue	
		else:
			print ("Please enter a non-zero positive number of hours")	
			continue
			
	##days_in_year		
	printc ('y',"Effective no. of plant operation days in a year (in days)")
	printc ('b',"Current value : "+str(days_in_year)+" days in a year" )
	while 1:
		ki=input_number()
		if ki=='':
			break
		elif (float(ki) > 0):
			days_in_year = float(ki)
			break
		elif (float(ki) == 0):
			print ("Please enter non-zero number of days")
			continue	
		else:
			print ("Please enter a non-zero positive number of days")	
			continue											 					
			
	##years_of_operation		
	printc ('y',"No. of expected plant operation years (in years)")
	printc ('b',"Current value : "+str(years_of_operation)+" years" )
	while 1:
		ki=input_number()
		if ki=='':
			break
		elif (float(ki) > 0):
			years_of_operation = int(ki)
			break
		elif (float(ki) == 0):
			print ("Please enter non-zero number of years")
			continue	
		else:
			print ("Please enter a non-zero positive number of years")	
			continue				
	###############################################################################
	

def init():									#set initials
	global EN_cons
	global Rs_cons
	global Avbl_area
	global area_bool
	global dsrd_invst_bool
	global dsrd_invst
	EN_cons=0.00
	Rs_cons=0.00
	Avbl_area=0.00
	area_bool=True
	dsrd_invst_bool=True
	dsrd_invst=0.00
	#energy consumption setup
	print ("We reqire some information from you. Please give correct information in order to get better results.")
	print ("Do you want to proceed to setup?")
	print ("ENTER to proced\t\t\tType NO to exit")
	while 1:
		ki=str(input_str())
		if find(ki,'no'):
			print ("\n\n\tWe would like to see you again, Thank you")
			sys.exit()
		elif ki=='':
			break
			
	while 1:	
		cons_bool = False	
		print ("\n\nElectricity consumption setup--------------------")
		print ("\nEnter monthly electricity consumption (Rs/month) : \t\t(To enter in kWh/month, press ENTER)")
		Rs_cons_month_tmp = input_number()
		if (Rs_cons_month_tmp == ""):
			print ("Enter Monthly consumption in Units (kWh/month) : ")
			EN_cons_month_tmp = input_number()
			if (EN_cons_month_tmp == ''):
				printc ('r', "You have skipped to input consumption in any form. \n Conumption is being taken to be zero")
				EN_cons = 0
				Rs_cons = 0
			elif (float(EN_cons_month_tmp) > 0):
				EN_cons = float(float(EN_cons_month_tmp) *12.00)
				Rs_cons = float(EN_cons * Rs_kWh)	
		else:
			Rs_cons = float(float(Rs_cons_month_tmp) * 12.00)
			EN_cons = float(Rs_cons / Rs_kWh)
		
		#Area setup
		print ("\n\nArea setup---------------------------------------")
		if (int(Rs_cons) == 0 or int(EN_cons) == 0):
			printc ('r',"As consumption is zero, you must enter maximum available area or maximum investment.")
			cons_bool = True		#true when cons = 0
	
		print ("\nEnter maximum available area (Square feet) : \t\t(To skip, press ENTER)")
		area_tmp = input_number()
		if (area_tmp == "" or area_tmp == '0'):
			area_bool = False
		else:
			area_bool = True
			Avbl_area = float(area_tmp)
		#Investment setup
		print ("\n\nInvestment setup---------------------------------")
		print ("\nEnter Investment you want to make (in Rs) : \t\t(If you have no preference, press ENTER)")
		dsrd_invst_tmp = input_number()
		if (dsrd_invst_tmp == "" or dsrd_invst_tmp == 0):
			dsrd_invst_bool = False
		else:
			dsrd_invst_bool = True
			dsrd_invst = float(dsrd_invst_tmp)
			
		if (cons_bool and not area_bool and not dsrd_invst_bool):
			printc ('r',"Please enter atleast one of the three : Consumption, Area or Investment")
			continue
		else:
			break		
		
	print ("Thank you for your inputs----------------------------")	
	return

def print_defaults():					#Printing default data
	printc ('g',"\n\tYearly electricity consumption is "+str(float2(EN_cons))+" kWh")
	printc ('g',"\tYearly consumption bill is "+str(comma(float2(Rs_cons)))+" Rs.")
	if (area_bool):
		printc ('g',"\tAvailable area is "+str(float2(Avbl_area))+" sq. ft.")
	if (dsrd_invst_bool):
		printc ('g',"\tYour investment limit is "+str(comma(float2(dsrd_invst)))+" Rs.")	
	printc ('g',"\tElectricity rate is "+str(Rs_kWh)+" Rs/kWh")
	printc ('g',"\tElectricity purchase rate is "+str(EN_purchase_rate)+" Rs/kWh")
	printc ('g',"\tElectricity rate increment is "+str(EN_rate_incrmt)+"% yearly")
	printc ('g',"\tPlace is set to be "+str(place)+", "+str(state)+" which has irradiation of "+str(Irradiation)+" kWh/m2/day")
	if (Dsrd_size != 0):
		printc ('g',"\tdesired plant is "+str(Dsrd_size)+" kW")
	printc ('g',"\tPresent installation cost is "+str(Instl_rate)+" Rs/kW")
	if (Govt_subsidy != 0):
		printc ('g',"\tCentral government gives "+str(ctrl_gov_percentage)+"% subsidy on installation cost")
	printc ('g',"\tDepriciation rate is "+str(Depr_rate)+"%")
	printc ('g',"\tPanel efficiency is "+str(Panel_efficiency)+"%")
	printc ('g',"\tProductive hours in a day are "+str(hours_in_day)+" hours")
	printc ('g',"\tProductive days in a year are "+str(days_in_year)+" days")
	printc ('g',"\tProductive years of operation are "+str(years_of_operation)+" years")			
			

def presentation(show_type,max_kw,reqr_kw,kw_d=0):				#presenting the calculations values
	global tab1
	tab1 = tt.Texttable()
	
	head_tab1 = ['Plant size (kW)', 'Required Area (sq. ft.)', 'Installation Cost (Rs.)','Depriciated amount (Rs.)','Electricity Bill benefit (Rs.)','Excess Energy income (Rs.)','Final amount (Rs.)','Gross Benefit (Rs.)','Apparent interest rate (%)','Pay back period (years)']
	tab1.header(head_tab1)
	tab1.set_cols_width([8,8,13,13,13,13,13,13,8,8])
	tab1.set_cols_align(['r','r','r','r','r','r','r','r','r','r'])
	#tab1.set_deco(tab1.HEADER | tab1.VLINES)
	
	if (kw_d == 0):
		kw_d = max_kw
			
	#adding rows with different kW
	if (show_type == "small"):
		kw=1
		mkw=max_kw		
	elif (show_type == "unique"):
		kw=kw_d#max_kw
		mkw=kw_d#max_kw
	elif (show_type == "normal"):
		kw=reqr_kw
		mkw=max_kw
		
	p=kw
	h=min((mkw-kw)/10.00,5.00)	
	t=h
	if (h<=0):
		h=0
		t=0.5
	elif (h<0.5):
		h=0.5
		t=h
	else:
		h=round5(h)
		t=h
	
	while (kw <= mkw+(1*h)):
		ad=Plant(kw)
		ad.define()
		if( kw > max_kw or ad.Savings < 0):
			ad.present_c(bcolors.RED)
		elif (kw < reqr_kw):	
			ad.present_c(bcolors.YELLOW)
		else:
			ad.present()
		p=p+t
		kw=round5(p)
	
	show = tab1.draw()
	print (show)

	
#####################################################################################################################################################Random
def small_plant():
	print ("\nDo you want to check possibility of smaller plants? (ENTER for yes , type no) ")
	while 1:
		ki=str(input_str())
		if find(ki,'no'):
			print ("\n\t\t\t\t\t We would like to see you again, Thank you")
			sys.exit()
		elif ki=='':
			global show_type
			show_type = "small"
			break
		else:
			printc ('r',"please enter as mentioned")	
def save(name):
	print ("Under construction")
	sys.exit()			
###############################################################################################################################################Calculations
def kW_required():
	kW_reqr = float(EN_cons/(days_in_year*hours_in_day))
	return kW_reqr

def plant_area_calc(reqr_kW):
	p_area = float( 10.7639 * (reqr_kW * hours_in_day * 100.000)/(Panel_efficiency * Irradiation) )
	return p_area
	
def area_to_kW(area):
	kW_a = float((area * (Panel_efficiency * Irradiation))/(10.7639 * hours_in_day * 100.0000))
	return kW_a 

def state_policy(kW):
	state_gov = 0
	global S_Govt_subsidy
	if (S_Govt_subsidy):
		#for GUJARAT
		if (find(state,'guj') or find(state,'Guj')):
			if (kW <=2):							
				state_gov = kW*10000.00
			else:
				state_gov = 20000.00	
		else:
			printc ('r',"Policy for \""+state+"\" state is not known to me. please let me know the policy before second run.")
			printc ('b',"\tIn this calculations state goverment policy is not being affected. \n\t(It will be in effect after policy is known)")	
			S_Govt_subsidy = False
			
	return float(state_gov)
	
	
def instalation(reqr_kW):
	invst = reqr_kW * Instl_rate
	ctrl_gov = float(invst) * (ctrl_gov_percentage/100.00)						
	state_gov = state_policy(reqr_kW)
	
	if (Govt_subsidy and S_Govt_subsidy):
		invst_gov = invst - ctrl_gov - state_gov
	elif (Govt_subsidy and not S_Govt_subsidy):
		invst_gov = invst - ctrl_gov
	elif (not Govt_subsidy and S_Govt_subsidy):
		invst_gov = invst - state_gov
	else:
		invst_gov = invst
			
	return invst, invst_gov

def payback(plant):	#returns no of years
	x=-1.00
	yr=0.00
	int(x)
	int(yr)
	while (int(x)<0.00 and yr < years_of_operation):
		yr=yr+0.25
		x=float(plant.savings(yr))
	if (yr == years_of_operation):
		return False
	else:
		return float2(yr)

def maxlimit():
	if (cons_kW != reqr_kW):
		k = float(area_to_kW(Avbl_area)) + 0.05
		reason = "Area unavailability"
	elif (area_bool and float(reqr_plant.Area) > float(Avbl_area)):
		k = float(area_to_kW(Avbl_area)) + 0.05
		reason = "Area unavailability"
	else:
		k=reqr_kW
		i=Plant(k)
		i.savings()
		reason = "financial disbenefit (lower interest rate than depriciation)"
		while (i.int_rate_n > Depr_rate):
			k=k+0.05 
			i=Plant(k)
			i.savings()
			if (area_bool and float(i.Area) > float(Avbl_area)):
				reason = "Area unavailability"
				break
	return k-0.05, reason
	
def Depriciation(invest,n=years_of_operation):						#Total depriciated amount after n years
	mult = float((Depr_rate/100.00)+1.00)
	mult_factor = float(math.pow(mult,n))
	depri_amount = float(invest * mult_factor)
	return depri_amount
	
def Bill_back(kW,n=years_of_operation):							#Total bill amount in n years
	if (float(EN_rate_incrmt) != 0):
		rate = 1.00+(float(EN_rate_incrmt)/100.00)
		mult_fact1 = (1.00-(pow(rate,float(n))))
		mult_fact2 = (1.00-rate)
		bill_benefit = 0.00
		if (kW>=cons_kW):
			bill_benefit = float(Rs_cons*(mult_fact1/mult_fact2))
		else:
			bill_benefit = float(kW*hours_in_day*days_in_year*Rs_kWh*(mult_fact1/mult_fact2))
		
	elif (float(EN_rate_incrmt) == 0 and kW>=cons_kW):
		bill_benefit = float(Rs_cons * n)
	else:
		bill_benefit = float(kW*hours_in_day*days_in_year*Rs_kWh*n)
	return float(bill_benefit)
def excess_energy(kW,n=years_of_operation):							#Value in Rs. of excess energy
	if (kW > cons_kW):
		per_day_kWh = 0.00
		per_day_kWh = float(kW - cons_kW) * hours_in_day
		per_year_kWh = per_day_kWh * days_in_year
		Rs_per_year = per_year_kWh * EN_purchase_rate
		Rs_n_year = float(Rs_per_year * n)
		return float(Rs_n_year)
	else:
		return 0.00
		
########################################################################################################################################Plant_class
class Plant:
	
	def savings(self,n=years_of_operation):
		self.depri_amount_n = Depriciation(self.cost_sub,n)
		self.bill_benefit_n = Bill_back(self.kW,n)
		self.Rs_n_year_n = excess_energy(self.kW,n)
		self.Final_amount_n = self.bill_benefit_n + self.Rs_n_year_n
		self.Savings_n = int(self.Final_amount_n) - int(self.depri_amount_n)
		self.int_rate_n = float((math.exp((math.log(self.Final_amount_n/self.cost_sub)/n))-1.00)*100.00)
		return self.Savings_n
	
	def define(self):
		n=years_of_operation
		self.depri_amount = Depriciation(self.cost_sub,n)
		self.bill_benefit = Bill_back(self.kW,n)
		self.Rs_n_year = excess_energy(self.kW,n)
		self.Final_amount = self.bill_benefit + self.Rs_n_year
		self.Savings = int(self.Final_amount) - int(self.depri_amount)
		self.int_rate = ((math.exp((math.log(self.Final_amount/self.cost_sub)/n))-1.00)*100.00)
		self.paybp()
		return self.Savings
	
	def paybp(self):
		if (not payback(self)):
			self.pay_back_period = ("> "+str(years_of_operation))
		else:	
			self.pay_back_period = float2(payback(self))

	def present(self):
		row =[ self.kW, float2(self.Area), comma(float2(self.cost_sub)), comma(float2(self.depri_amount)), comma(float2(self.bill_benefit)), comma(float2(self.Rs_n_year)), comma(float2(self.Final_amount)), comma(float2(self.Savings)), float2(self.int_rate), self.pay_back_period]
		tab1.add_row(row)
		
	def present_c(self,c):
		row =[ get_color_string(c,float2(self.kW)), get_color_string(c, float2(self.Area)), get_color_string(c,comma(float2(self.cost_sub))), get_color_string(c,comma(float2(float(self.depri_amount)))), get_color_string(c,comma(float2(self.bill_benefit))), get_color_string(c,comma(float2(self.Rs_n_year))), get_color_string(c,comma(float2(self.Final_amount))), get_color_string(c,comma(float2(self.Savings))), get_color_string(c,float2(self.int_rate)), get_color_string(c,self.pay_back_period)]
		tab1.add_row(row)	
		
	def __init__(self,a=0.00):	
		self.kW = a
		self.Area = plant_area_calc(a)
		self.cost, self.cost_sub = instalation(a)
		self.define()
		
######################################################################################################################################################Main
if __name__ =="__main__":
#inputs
	print ("Welcome #######################################################################################################")
	print ("find best size of SOlAR roof top plant for your home or office")
	print ("---------------------------------------------------------------------------------------------------------------")
	print ("\nNote:\n\t You can go to advance settings if you want to change any default settings which are as per current economic situation and as per "+place+"'s geographical location.")
	
	while 1:
		init()							#taken over by initialisation function
		
		while 1:
			print_defaults()
			print ("\nPress Enter to proceed with above values \t\t\tTo change any default value type advance")
			ki=str(input_str())
			
			if find(ki,'adv'):
				adv_init()
			elif ki=='':
				break
			else:
				printc ('r',"please enter as mentioned")
			
	#calculation
		global reqr_kW
		global cons_kW
		global max_kW, reason
		global plant_area
		global investment, investment_govt
		cons_kW = kW_required()							#required size
		if (cons_kW == 0 and area_bool):
			print ("\n\tZero consumption detected \n\tTip: Solar roof-top plants are best with on-site usage (house, office etc) due to net metering policy for domastic solar roof-top plants")
			reqr_kW = area_to_kW(Avbl_area)
			show_type = "unique"
			string = "Possible plant"
			break
		elif (cons_kW == 0):
			print ("There is some input error, please enter non zero consumption or provide area") 	
			continue
		else:
			reqr_kW = cons_kW
			string = "Your required plant"
			break
			
	reqr_plant = Plant(reqr_kW)						#making Plant class object with required kW , initialization
	plant_area = reqr_plant.Area						#required plant area
	investment, investment_govt = reqr_plant.cost, reqr_plant.cost_sub	#required investment
	max_kW, reason = maxlimit()						#maximum size
	if (max_kW <= 1):
		show_type = "unique"
	
	printc ('y',"\n"+string+" size is "+str(float2(reqr_kW))+" kW and area required is "+str(float2(plant_area))+" sq.ft.")
	printc ('y',"Total subsidised investment amount for the plant of your need is "+str(comma(float2(investment_govt)))+" Rs.")
	
	if (max_kW < reqr_kW):
		abc='r'
	else:	
		abc='y'	
	printc (abc,"Maximum plant size due to "+str(reason)+" is "+str(float2(max_kW))+" kW\n")
	
	#Area verification	
	if (area_bool and plant_area > Avbl_area):
		printc ('r',"Area required is more than available area. In this condition we can have plant which partially satisfies your requirment or you may try to accuire more area for plant.")
		small_plant()
	
	#Investment verification	
	if (dsrd_invst_bool and investment_govt > dsrd_invst):
		printc ('r',"Investment required is more than your available funding. Difference is of "+(str(comma(float2(investment_govt-dsrd_invst))))+" Rs. You can go for partial requirment plants")		
		small_plant()
	
	reqr_plant.define()							#complete initialization							
	
#Presentation	
	#making table with different kW to present for choice
	presentation(show_type,max_kW,reqr_kW)

#Checking for input for any specific kW value or exit command
	while 1:
		print ("\n\nDo you want data for any specific plant?\nIf so enter kW of the desired plant : \t\tTo save above table TYPE Save \t\tTo exit press ENTER")
		ki=str(input())
		if find(ki,'save'):
			print ("Provide the Name of the file :")
			nm = str(input_str())
			save(nm)
		elif (ki==''):
			break
		#elif (ki == int		##type of variable
		elif (is_number(ki)):
			Dsrd_size = float(ki)
			if (Dsrd_size > 0.20):
				presentation('unique',max_kW,reqr_kW,Dsrd_size)
			else:
				printc ('r',"Please enter value greater than 0.2 kW")
				continue	
		else:
			printc ('r',"please enter as mentioned")	
#end of the program
	print ("\n\nThank you for trusting us, hope you get the size which suits you\n")
####termination
