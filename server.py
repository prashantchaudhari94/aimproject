#dep:1.0
import os
import MySQLdb
from datetime import datetime, timedelta
from flask import Flask, render_template, request, url_for, redirect, session
from flask_mysqldb import MySQL
import re
  
app = Flask(__name__)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pc@soft94'
app.config['MYSQL_DB'] = 'packer'
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def disp_table():
    
    cursor = mysql.connection.cursor()
    insert_but=""       
    #When disp_list called directly there is no value to insert_but (gives error)
    insert_but=request.form.get('insert')
    if not insert_but :
        insert_but="a"                   #This is dummy value. To ensure routing, if not calling from 'insert' button selection. 
    print("but selected", insert_but)

    cursor.execute("select enquiry1.*, visit.visit_no_id from enquiry1 left join visit ON enquiry1.enquiry_no_id = visit.enquiry_no_id;")
    data = cursor.fetchall()
    

    # if material table data is present then select 
    if "Material" in insert_but :
        #memo_list()
        cursor.execute('select material_name,stock_UM from material')
        material_data = cursor.fetchall()    
        return render_template('material_selection.html', material_data=material_data)

    cursor.execute("SELECT enquiry_no_id, memo_date FROM memo")
    memo_data = cursor.fetchall()
    for row in memo_data:
        enquiry_no_id = row[0]
        memo_date = row[1]
    
    return render_template('disp_table.html', data=data, memo_data=memo_data)




@app.route('/material_select', methods=['GET', 'POST'])
def material_select():
    cursor = mysql.connection.cursor()
    enq_id = request.form.get('enq_number')
    insert_but=""                        #When disp_list called directly there is no value to insert_but (gives error)
    insert_but=request.form.get('insert')
    if not insert_but :
        insert_but="a"                   #This is dummy value. To ensure routing, if not calling from 'insert' button selection. 
    print("but selected:", insert_but, ",",enq_id)
    
    if "Material" in insert_but :
        #memo_list()
        cursor.execute('select material_name,stock_UM from material')
        material_data = cursor.fetchall()
        enq_id = request.form.get('enq_number')    
    return render_template('material_selection.html', material_data=material_data, enq_id=enq_id)

@app.route('/material_issued', methods=['GET', 'POST'])
def material_issued():
    enq_id = request.form.get('enq_number')
    material_name=request.form.get('material_name')
    qty_issued=request.form.get('qty_issued') 
    insert=request.form.get('insert')
    #insert=request.form['insert']
    #qty_issued="QTY"
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO material (material_id, Qty_issued) VALUES ( %s,%s)',(material_id,qty_issued))
    mysql.connection.commit()
    
    print("AAA:",enq_id,insert,qty_issued)
    return("Values are=",qty_issued)   

        



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
    recid = request.form.get('recid')
    preferred_visit_date = request.form.get('p_visit_date')
    exe_name = request.form.get('exe_name')
    article_list = request.form.get('article')
    
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO visit (preferred_visit_date, enquiry_no_id, visit_Executor_name, article_list) VALUES (%s, %s, %s, %s)',
                           (preferred_visit_date, recid, exe_name, article_list))
    mysql.connection.commit()
    
    return redirect(url_for('disp_table'))

@app.route('/disp_table1', methods=['GET', 'POST'])
def disp_table1():
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




@app.route('/insert',methods=['GET', 'POST'])
def insert():
    
    timestamp=datetime.now()
    tommrrow = timestamp + timedelta(5)
    today1 = tommrrow.strftime("%Y-%m-%d") 
    return render_template('insert_table.html',today1=today1)


@app.route('/insert_table', methods=['GET', 'POST'])
def insert_table():
    cursor = mysql.connection.cursor()
    name = request.form['name']
    alist = request.form['alist']
    cursor.execute( 'INSERT INTO visit (name, alist, enquiry_no_id ) values (% s, %s)', (name, alist))
    mysql.connection.commit()
    return ('Data in table- success')


@app.route('/open_enq', methods=['GET', 'POST'])
def open_enq():
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
                print ("enq_id = ", enquiry_no_id, memo_data)
                #return ("Page with work memo values.",enquiry_no_id)
            if not len(data_enqid) is 0 :                     #NOT 0. memo already exists. only show memo
                return render_template('memo_display.html',memo_data=data_enqid, party_name=party_name, recid=recid) 
            else :                                 # New memo. Collect values
                return render_template('memo_form.html', data=data, recid=recid, party_name=party_name, address_loading=address_loading, address_unloading=address_unloading, visit_no = visit_no, today1=today1 )             
        except :
            print ('In except')

        return render_template('memo_form.html', data=data, recid=recid, party_name=party_name, address_loading=address_loading, address_unloading=address_unloading, visit_no = visit_no, today1=today1 ) 
    else :
        return ("Page yet to design.")



#5.it select quotation table. and display quotation tracker page.
@app.route('/quot_tracker', methods=['GET', 'POST'])
def quot_tracker():
    cursor = mysql.connection.cursor()
    #recid = request.form['enqid_select']
    cursor.execute("SELECT * FROM quotation")
    data = cursor.fetchall()
    return render_template('quot_tracker.html', data=data)
    #return ("Page to display quot list and status.")

@app.route('/workorder_tracker', methods=['GET', 'POST'])
def workorder_tracker():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM memo")
    data = cursor.fetchall()
    
    return render_template('workorder_tracker.html',data=data)

#6 Insert data into memo table.
@app.route('/memo_success', methods=['GET', 'POST'])
def memo_success():
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


@app.route('/quot_save', methods=['GET', 'POST'])
def quot_save():
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

if __name__ == "__main__":
#    app.run(host='192.168.1.200', port=5000, debug=True)
     app.run(host='0.0.0.0', port=5000, debug=True)

