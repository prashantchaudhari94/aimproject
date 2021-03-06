#dep:1.0
import os
import MySQLdb
from datetime import datetime, timedelta
from flask import Flask, render_template, request, url_for, redirect, session
from flask_mysqldb import MySQL,MySQLdb
import re
import math
from flask_paginate import Pagination, get_page_parameter
  
app = Flask(__name__)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pc@soft94'
app.config['MYSQL_DB'] = 'packer'
#app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("login.html")

#loginpage
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        #if user.uername==username and user.password==password:
        #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user WHERE binary username = %s AND  binary password = %s' , (username, password, ))
        account = cursor.fetchone()        
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            return redirect(url_for('disp_table'))
        else:
            msg = 'Incorrect username or password !'

    return render_template('login.html', msg=msg)


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO user (username, password, email) VALUES (% s, % s, % s)',
                           (username, password, email))
            mysql.connection.commit()
            msg = 'User successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg=msg)



@app.route('/disp_table', methods=['GET', 'POST'])
def disp_table():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor()
        insert_but=""       
        #When disp_list called directly there is no value to insert_but (gives error)
        insert_but=request.form.get('insert')
        if not insert_but :
            insert_but="a"                   #This is dummy value. To ensure routing, if not calling from 'insert' button selection. 
        print("but selected", insert_but)

        cursor.execute("select enquiry1.*, visit.visit_no_id from enquiry1 left join visit ON enquiry1.enquiry_no_id = visit.enquiry_no_id;")

        data = cursor.fetchall()
        
###########
        # if material table data is present then select 
        if "Material" in insert_but :
            #memo_list()
            cursor.execute('select material_id, material_name,stock_UM from material')
            material_data = cursor.fetchall()    
            return render_template('material_selection.html', material_data=material_data)

        cursor.execute("SELECT enquiry_no_id, memo_date FROM memo")
        memo_data = cursor.fetchall()
        for row in memo_data:
            enquiry_no_id = row[0]
            memo_date = row[1]
        
        return render_template('disp_table.html', data=data, memo_data=memo_data, username=session['username'])
    else:
        return redirect(url_for('login'))

#######


###
 


        
        



#pagination

@app.route('/material_select', methods=['GET', 'POST'])
def material_select():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor()
        enq_id = request.form.get('enq_number')
        memo_id = request.form.get('memo_number')
        print(enq_id,memo_id)
        insert_but=""                        #When disp_list called directly there is no value to insert_but (gives error)
        insert_but=request.form.get('insert')
        if not insert_but :
            insert_but="a"                   #This is dummy value. To ensure routing, if not calling from 'insert' button selection. 
        print("but selected:", insert_but, ",",enq_id)
        #####
        '''material_id = request.form.getlist('material_id[]')
        material_name=request.form.getlist('material_name[]')
        memo_id = request.form.getlist('memo_id[]')
        qty_in_stock=request.form.getlist('qty_in_stock[]')
        qty_issued=request.form.getlist('qty_issued[]')'''

        if "Material" in insert_but :
            cursor.execute('select material_id, material_name,stock_UM from material')
            material_data = cursor.fetchall()
            total=len(material_data)
            enq_id = request.form.get('enq_number')   
            memo_id= request.form.get('memo_number')
            msg = ''
    
        '''for  index in range(len(material_id)):
            if (int(qty_issued[index]) > int(qty_in_stock[index])):
                msg="Entered quantity is greater than available stock"
                #print([material_name[i],"Entered quantity is greater than available stock"])
            else:
                cur.execute("INSERT INTO cost ( material_id,material_name,memo_id,total_stock,qty_issued) VALUES (%s, %s,%s,%s, %s) ", (material_id[index],material_name[index],memo_id[index],qty_in_stock[index],qty_issued[index]))
                stock=int(qty_in_stock[index])-int(qty_issued[index])
                id=material_id[index]
                print(stock)
                cur.execute("UPDATE cost SET current_stock="+str(stock)+" WHERE material_id="+str(id)) 
                data=cur.fetchall()     
                mysql.connection.commit()

                cur.close()  
            return redirect(url_for('cost'))'''

        return render_template('material_selection.html', material_data=material_data, enq_id=enq_id,memo_id=memo_id)




@app.route('/material_issued',methods=['GET', 'POST'])
def material_issued():
     if 'loggedin' in session:
        cursor = mysql.connection.cursor()
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        message=""
        if request.method=='POST':
            print(request.form)
            material_id = request.form.getlist('material_id[]')
            material_name=request.form.getlist('material_name[]')
            memo_id = request.form.getlist('memo_id[]')
            qty_in_stock=request.form.getlist('qty_in_stock[]')
            qty_issued=request.form.getlist('qty_issued[]')
            
            #for i, index  in enumerate(material_name):
              #if(int(qty_issued[i]) < int(qty_in_stock[i])):
                    #flash('Looks like you have changed your name!')
                    #return("Entered quantity is greater than available stock")


           #if qty_in_stock <= qty_issued:


            for  index in range(len(material_id)):
                        #if (int(qty_issued[index]) > int(qty_in_stock[index])):
                            #print([material_name[index],"Entered quantity is greater than available stock"])
                        #else:  
                        cur.execute("INSERT INTO cost ( material_id,material_name,memo_id,total_stock,qty_issued) VALUES (%s, %s,%s,%s, %s) ", (material_id[index],material_name[index],memo_id[index],qty_in_stock[index],qty_issued[index]))
                        stock=int(qty_in_stock[index])-int(qty_issued[index])
                        id=material_id[index]
                        print(stock)
                        #update in material table.
                        cur.execute("UPDATE material SET current_st="+str(stock)+" WHERE material_id="+str(id))
                        ####
                        cur.execute("UPDATE cost SET current_stock="+str(stock)+" WHERE material_id="+str(id))
                        data=cur.fetchall()     
                        mysql.connection.commit()

            cur.close()  
            return redirect(url_for('cost'))
            

@app.route('/cost', methods=['GET', 'POST'])
def cost():
    cursor = mysql.connection.cursor()
    memo_id= request.form.get('memo_number')
    #cursor.execute("select cost.*, memo.memo_id from cost left join memo ON cost.memo_id = memo.memo_id;")
    cursor.execute("SELECT * FROM cost ")
    data = cursor.fetchall()
    return render_template('cost.html', data=data,memo_id=memo_id)
    

@app.route('/page1/<my_var>')
def page1(my_var):
    # but_id = str(request.form['myBut'])
    # my_var = request.args.get('my_var', None)
    print(request.form.get('my_var'))
    print(my_var)
    return render_template("page1.html", my_var=my_var)
    print("but_id=", but_id)
    #but_id = str(request.args.get('myBut'))
    return but_id


@app.route('/enq_visit', methods=['GET', 'POST'])
def enq_visit():
    if 'loggedin' in session:
        recid = request.form.get('recid')
        preferred_visit_date = request.form.get('p_visit_date')
        exe_name = request.form.get('exe_name')
        article_list = request.form.get('article')
        
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO visit (preferred_visit_date, enquiry_no_id, visit_Executor_name, article_list) VALUES (%s, %s, %s, %s)',
                            (preferred_visit_date, recid, exe_name, article_list))
        mysql.connection.commit()
        
        return redirect(url_for('disp_table'))
    else:
        return redirect(url_for('login'))    

@app.route('/disp_table1', methods=['GET', 'POST'])
def disp_table1():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor()
        party_name = str(request.form.get('party_name'))
        contact_no=request.form.get('contact_no')
        email_id=request.form.get('email_id')
        address_from=request.form.get('address_from')
        address_to=request.form.get('address_to')
        t_moving_date=str(request.form.get('t_moving_date'))
        city_load=request.form.get('city_load')
        city_unload=request.form.get('city_uload')
        house_area = request.form.get('house_area')
        p_visit_date=str(request.form.get('p_visit_date'))
        lift_load=request.form.get('lift_load')
        lift_unld=request.form.get('lift_unld')
        floor_no_load=request.form.get('floor_no_load')
        floor_no_unload=request.form.get('floor_no_unload') 
        insurence_required=request.form.get('insurance')
        visit_req=request.form.get('visit')
        print("but_id=", house_area, lift_load,  address_to)
        timestamp=datetime.now()
        today1 = timestamp.strftime("%Y-%m-%d")
        cursor.execute ( 'INSERT INTO enquiry1 (date_of_enquiry, party_name, party_mobile_no, party_mail_id, tentative_shifting_date, address_loading, city_loading, address_unloading,city_unloading, lift_availability_loading, lift_availability_unloading, floor_no_loading, floor_no_unloading, preferred_visit_date,insurance_required, visit_required, household_size, active )  values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', 
            (today1, party_name, contact_no,email_id, t_moving_date, address_from, city_load, address_to, city_unload, lift_load, lift_unld,  floor_no_load, floor_no_unload, p_visit_date, insurence_required, visit_req, house_area, 1 ))
        mysql.connection.commit()

        return redirect(url_for('disp_table'))
    else:
        return redirect(url_for('login'))





@app.route('/insert',methods=['GET', 'POST'])
def insert():
    if 'loggedin' in session:
        timestamp=datetime.now()
        tommrrow = timestamp + timedelta(5)
        today1 = tommrrow.strftime("%Y-%m-%d") 
        return render_template('insert_table.html',today1=today1)
    else:
         return redirect(url_for('login'))





@app.route('/insert_table', methods=['GET', 'POST'])
def insert_table():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor()
        name = request.form['name']
        alist = request.form['alist']

        cursor.execute( 'INSERT INTO visit (name, alist, enquiry_no_id ) values (% s, %s)', (name, alist))
        mysql.connection.commit()
        return ('Data in table- success')
    else:
        return redirect(url_for('login'))



@app.route('/open_enq', methods=['GET', 'POST'])
def open_enq():
    if 'loggedin' in session:
        timestamp=datetime.now()
        today1 = timestamp.strftime("%Y-%m-%d")

        cursor = mysql.connection.cursor()
        
        recid = request.form['enqid_select']
        print ("first recid ", recid, today1)
            
        cursor.execute('select * from enquiry1 where enquiry_no_id = %s', (recid,))
        data = cursor.fetchall()
        for row in data:
            party_name = row[2]
            address_loading = row[6]
            address_unloading = row[8]
            
        visit_no = 0
        try :    
            cursor.execute('select visit_no_id from visit where enquiry_no_id = %s', (recid,))
            data_visit = cursor.fetchall()
            for row in data_visit:
                visit_no = row[0]
        except :
            visit_no=0
        print ("after try visit_id ", visit_no, recid)
        submit_selected=request.form['submit']
        #print ('Submit', submit_selected)
        if submit_selected in 'Edit Record':
            return("Edit Record pg to call")

        if submit_selected in 'Open Enquiry':
            return render_template('open_enq.html', data=data, recid=recid)

        if submit_selected in 'Visit':
            cursor.execute('select fname,lname, executive_id from executive')
            executive_names = cursor.fetchall()
            print ('Exe Names ', executive_names )
            
        #validation for visit    
            cursor.execute('select visit_no_id from visit where enquiry_no_id = %s', (recid,))
            entry=cursor.fetchall()
            if entry:
                return("Visit complete, Check for Quotation")
            else:
                return render_template('enq_visit.html', data=data, recid=recid, party_name=party_name, executive_names=executive_names,entry=entry)      
        
        if submit_selected in 'Quotation Form' :
            print ("In quot =", visit_no)
            if visit_no == 0 :
                return("Please complete visit first")

            return render_template('quot_form.html', data=data, recid=recid, party_name=party_name, address_loading=address_loading, address_unloading=address_unloading, visit_no = visit_no, today1=today1 )   
        
        if submit_selected in 'Work Order Memo' :
            try :    
                cursor.execute('select * from memo where enquiry_no_id = %s', (recid,))
                data_enqid = cursor.fetchall()
                print ("in workorder ", recid, len(data_enqid))   # corrected this to start checking that already memo is done.

                memo_data = row
                for row in data_enqid:
                    
                    enquiry_no_id = row[3]
                    memo_id=row[0]
                    print ("enq_id = ", enquiry_no_id, memo_data)
                    #return ("Page with work memo values.",enquiry_no_id)
                if not len(data_enqid) is 0 :                     #NOT 0. memo already exists. only show memo
                    return render_template('memo_display.html',memo_data=data_enqid, party_name=party_name, recid=recid,memo_id=memo_id) 
                else :                                 # New memo. Collect values
                    return render_template('memo_form.html', data=data, recid=recid, party_name=party_name, address_loading=address_loading, address_unloading=address_unloading, visit_no = visit_no, today1=today1 )             
            except :
                print ('In except')

            return render_template('memo_form.html', data=data, recid=recid, party_name=party_name, address_loading=address_loading, address_unloading=address_unloading, visit_no = visit_no, today1=today1 ) 
        else :
            return ("Page yet to design.")
    else:
        return redirect(url_for('login'))



#5.it select quotation table. and display quotation tracker page.
@app.route('/quot_tracker', methods=['GET', 'POST'])
def quot_tracker():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor()
        #recid = request.form['enqid_select']
        cursor.execute("SELECT * FROM quotation")
        data = cursor.fetchall()
        return render_template('quot_tracker.html', data=data)
    else:
        return redirect(url_for('login'))

@app.route('/workorder_tracker', methods=['GET', 'POST'])
def workorder_tracker():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor()
        memo_id= request.form.get('memo_number')
        cursor.execute("SELECT * FROM memo")
        data = cursor.fetchall()
        
        return render_template('workorder_tracker.html',data=data,memo_id=memo_id)
    else:
        return redirect(url_for('login'))

#6 Insert data into memo table.
@app.route('/memo_success', methods=['GET', 'POST'])
def memo_success():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor()
        today = datetime.today()
        d1 = today.strftime("%Y-%m-%d")
        memodate = request.form.get('memodate')   
        consignor= request.form.get('consignor')
        consignorAdd = request.form.get('consignorAdd')
        recid = request.form.get('recid')
        visit_no = request.form.get('visit_no')
        party_name = request.form.get('party_name')
        consignee  = request.form.get('consignee1')
        consigneeAdd  = request.form.get('consigneeAdd')
        driver_name = request.form.get('driver_name')
        driver_allowace = request.form.get('driver_allowace')
        superviser_name = request.form.get('superviser_name')
        superviser_amt = request.form.get('superviser_amt')
        good_desc = request.form.get('good_desc')
        truck_no = request.form.get('truck_no')
        truck_owner = request.form.get('truck_owner')
        labour_name = request.form.get('labour_name')
        labour_charges = request.form.get('labour_charges')
        fright_charges = request.form.get('fright_charges')

        cursor.execute( 'INSERT INTO memo (enquiry_no_id, visit_no_id, memo_date, consignor, consignor_address, consignee, consingnee_address, driver_name, driver_allowance, superviser_name, superviser_amt, good_description, truck_no, truck_owner,labour_name, labour_charges, fright_charges ) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', 
            (recid, visit_no, memodate, consignor, consignorAdd, consignee, consigneeAdd, driver_name, driver_allowace, superviser_name, superviser_amt, good_desc, truck_no, truck_owner, labour_name, labour_charges, fright_charges ))
        mysql.connection.commit()
        print ("Enq Id=", recid, memodate,d1, visit_no,party_name, consignor, consignorAdd, consignee, driver_name, driver_allowace, superviser_name, superviser_amt, truck_owner,truck_no) 
        return render_template('memo_success.html', recid=recid, visit_no = visit_no, party_name=party_name)
        #return ("Page with work memo save all values")
    else:
        return redirect(url_for('login'))


@app.route('/quot_save', methods=['GET', 'POST'])
def quot_save():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor()
        recid = request.form.get('recid')
        visit_no = request.form.get('visit_no')
        party_name = request.form.get('party_name')
        quot_date = request.form.get('quot_date')
        charges_type = request.form.get('charges_type')
        details = request.form.get('details')
        offer_details = request.form.get('offer_details')
        amount = request.form.get('amount')
        tax = request.form.get('tax')
        invoice_req=request.form.get('invoice_req')
        cursor.execute( 'INSERT INTO quotation (enquiry_no_id, visit_no_id, party_name,  quotation_date, charges_type, details, offer_details, amount, tax, invoice_required  ) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (recid, visit_no, party_name,  quot_date, charges_type, details, offer_details,  amount, tax, invoice_req))
        mysql.connection.commit()
        #return ("Quotation saved")
        return redirect(url_for('disp_table'))
    
    return redirect(url_for('login'))

@app.route('/logout',methods=['GET', 'POST'])
def logout():
    session.pop('loggedin',None)
    session.pop('username',None)
    return redirect(url_for('login'))    

if __name__ == "__main__":
#    app.run(host='192.168.1.200', port=5000, debug=True)
     app.run(host='0.0.0.0', port=5000, debug=True)

