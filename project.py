import cx_Oracle
import re

dsn_tns = cx_Oracle.makedsn('LAPTOP-LBV8A2GC', '1521', service_name='XE')
conn = cx_Oracle.connect(user=r'kandarp', password='kpatel007', dsn=dsn_tns)

def queryFirst():
	c = conn.cursor()
	print("________________________________________________________________")
	print("100|D-Mart    |Surat    |Utran")
	print("110|D-Mart    |Surat    |Vesu")
	print("120|Big Bazaar|Surat    |Utran")
	print("130|Big Bazaar|Surat    |Vesu")
	print("200|D-Mart    |Ahmedabad|Chandkheda")
	print("210|D-Mart    |Ahmedabad|Lal Darwaja")
	print("220|Big Bazaar|Ahmedabad|Chandkheda")
	print("230|Big Bazaar|Ahmedabad|Lal Darwaja")
	print("________________________________________________________________")
	sid=input("Enter supermarketid to find out deapartmentwise total sell: ")
	print("supermarketid\t\ttotalsell")
	print("_____________\t\t__________")
	c.execute("select departmentid,sum(totalcost) from (select * from purchasedetails natural join productproj where supermarketid="+sid+") group by departmentid order by departmentid asc")
	for row in c:
		print(row[0],"\t\t",row[1])


def querySecond():
	c=conn.cursor()
	print("________________________________________________________________")
	print("Here is list of total sell of product for all supermarket")
	print("________________________________________________________________")
	c.execute("select supermarketid,sum(totalcost) from (select * from purchasedetails) group by supermarketid order by supermarketid asc")
	print("supermarketid\t\ttotalcost")
	print("______________\t\t_________")
	for row in c:
		print(row[0],"\t\t\t",row[1])


def queryThird():
	c=conn.cursor()
	print("________________________________________________________________")
	print("1011 Tomato")
	print("1012 Potato")
	print("1013 Onion")
	print("1014 Garlic")
	print("1015 Mango")
	print("1016 Apple")
	print("1017 Banana")
	print("1021 Milk")
	print("1022 Curd")
	print("1023 Buttermilk")
	print("1024 Cheese")
	print("1025 Butter")
	print("1026 Paneer")
	print("1031 Cake")
	print("1032 Biscuit")
	print("1033 Cookies")
	print("1041 Icecream")
	print("1042 Softdrinks")
	print("1043 Juice")
	print("1051 Chips")
	print("1052 Noodle")
	print("1053 Paasta")
	print("________________________________________________________________")
	pid=input("Enter productid to find out total sell of product:")
	print("Name\t\ttotalsell")
	print("____\t\t_________")
	c.execute("select name,sell from ((select productid,sum(totalcost) as sell from purchasedetails where productid="+pid+" group by productid order by productid asc)natural join productproj)")
	for row in c:
		print(row[0],"\t\t",row[1])


def queryFourth():
	c=conn.cursor()
	print("________________________________________________________________")
	print("101 Produce")
	print("102 Dairy")
	print("103 Bakery")
	print("104 Frozen")
	print("105 Packaged")
	print("________________________________________________________________")
	did=input("Enter departmentid to find out lowest sell from each supermarket:")
	print("supermarketid\t\tmin(sell)")
	print("_____________\t\t_________")
	x="select supermarketid,min(sell) as minCost from (select supermarketid,productid,sum(totalcost) as sell from ((select productid from productproj where departmentid="+did+"order by productid asc) natural join purchasedetails) group by productid,supermarketid) group by supermarketid order by supermarketid asc"
	# y="select name,supermarketid,minCost from (select productid where sell=minCost from (select supermarketid,productid,sum(totalcost) as sell from ((select productid from productproj where departmentid=101 order by productid asc) natural join purchasedetails) group by productid,supermarketid)natural join productproj)"
	c.execute(x)
	for row in c:
		print(row[0],"\t\t",row[1])


def queryFifth():
	c=conn.cursor()
	print("________________________________________________________________")
	print("Most valuable product")
	print("________________________________________________________________")
	x="select name,totalsell from (select * from (select productid,sum(purchasequantity) as totalsell from purchasedetails group by productid) where totalsell=(select max(totalsell) from (select sum(purchasequantity) as totalsell from purchasedetails group by productid))) natural join productproj"
	print("Product\t\ttotalcost")
	print("_______\t\t__________")
	c.execute(x)
	for row in c:
		print(row[0],"\t\t",row[1])


def querySixth():
	c=conn.cursor()
	print("________________________________________________________________")
	print("Customer with highest purchase")
	print("________________________________________________________________")
	print("Firstname\t\tLastname\t\tTotalsell")
	print("_________\t\t________\t\t_________")
	x="select firstname,lastname,totalsell from (select * from (select customerid,sum(totalcost) as totalsell from purchasedetails group by customerid) where totalsell=(select max(totalsell) from (select sum(totalcost) as totalsell from purchasedetails group by customerid))) natural join customers"
	c.execute(x)
	for row in c:
		print(row[0],"\t\t\t",row[1],"\t\t\t",row[2])

def customQuery():
	c=conn.cursor()
	print("________________________________________________________________")
	query=input("Enter your query: ")
	query = query[:len(query) - 1]
	print("________________________________________________________________")
	c.execute(query)
	for row in c:
		print(row)


def main():
	done = True
	print("________________________________________________________________")
	print("Welcome to our supermarket database......")
	print("________________________________________________________________")
	while done:
		print("Enter from following options")
		print("________________________________________________________________")
		print("1...To find out deapartmentwise total sell (Dynamic)")
		print("2...To find out total sell of product for all supermarket")
		print("3...To find out total sell of product (Dynamic)")
		print("4...To find out lowest sell from each supermarket (Dynamic)")
		print("5...To find most valuable product")
		print("6...To find out customer with highest purchase")
		print("7...For custom query")
		print("8...Logout")
		print("________________________________________________________________")
		case=int(input())
		if case==1:
			queryFirst()
		elif case==2:
			querySecond()
		elif case==3:
			queryThird()
		elif case==4:
			queryFourth()
		elif case==5:
			queryFifth()
		elif case==6:
			querySixth()
		elif case==7:
			customQuery()
		else:
			done=False
	print("________________________________________________________________")
	print("Thank you for visiting us......")
	print("________________________________________________________________")


if __name__=="__main__":
	main()