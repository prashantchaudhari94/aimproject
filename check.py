#2
'''it get data from "insert_table.html" file and store this data into "enqiry1 table".
its render the "disp_table.html" file. but it not shown any entry in this table.  '''

@app.route('/disp_table1', methods=['GET', 'POST'])
def disp_table1():
    # but_id = str(request.form['myBut'])
    #recid = request.args.get('recid')
    #recid = str(recid)
    #print(request.form.get('recid'))
    cursor = mysql.connection.cursor()
    party_name = str(request.form.get('party_name'))
    contact_no=request.form.get('contact_no')
    email_id=request.form.get('email_id')
    address_from=request.form.get('address_from')
    address_to=request.form.get('address_to')
    t_moving_date=str(request.form.get('t_moving_date'))
    #t_moving_date='2021-03-10'
    city_load=request.form.get('city_load')
    city_unload=request.form.get('city_uload')
    house_area = request.form.get('house_area')
    p_visit_date=str(request.form.get('p_visit_date'))
    floor_no_load=request.form.get('floor_no_load')
    floor_no_unload=request.form.get('floor_no_unload') 
    lift_Ld=request.form.get('lift_Ld')
    lift_Ld=1
    lift_Unld=request.form.get('lift_Unld')
    print("but_id=", house_area, lift_Ld, address_to)
    #today = datetime.today()
    #today1 = today.strftime("%Y-%m-%d")
    timestamp=datetime.now()
    today1 = timestamp.strftime("%Y-%m-%d")
    #cursor.execute ( 'INSERT INTO enquiry1 (date_of_enquiry, party_name, party_mobile_no, party_mail_id, tentative_shifting_date, address_loading, city_loading, address_unloading,city_unloading, floor_no_loading, floor_no_unloading, preferred_visit_date, household_size, active )  values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(today1, party_name, contact_no,email_id, t_moving_date, address_from, city_load, address_to, city_unload, floor_no_load, floor_no_unload, p_visit_date, house_area, 1 ))
  
    cursor.execute ( 'INSERT INTO enquiry1 (party_name, party_mobile_no,party_mail_id,tentative_shifting_date, address_loading,city_loading, address_unloading, city_unloading, household_size, preferred_visit_date, lift_availability_loading,lift_availability_unloading) values (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)',(party_name,contact_no,email_id, t_moving_date,address_from,city_load,address_to, city_unload, house_area,p_visit_date,lift_Ld,lift_Unld))
    mysql.connection.commit()
    #return ('Party=' + party_name)
    return render_template('disp_table.html')



#3
### MAIN Route -application start
"""it get data from "insert_table.html" file.
select enquiry1 and visit table.
select material table
select memo table.
it render "disp_table.html"file."""

@app.route('/disp_table', methods=['GET', 'POST'])
def disp_table():
    # but_id = str(request.form['myBut'])
    #recid = request.args.get('recid')
    #recid = str(recid)
    #print(request.form.get('recid'))
    cursor = mysql.connection.cursor()
    party_name = str(request.form.get('party_name'))
    contact_no=request.form.get('contact_no')
    email_id=request.form.get('email_id')
    address_from=request.form.get('address_from')
    address_to=request.form.get('address_to')
    t_moving_date=str(request.form.get('t_moving_date'))
    #t_moving_date='2021-03-10'
    city_load=request.form.get('city_load')
    city_unload=request.form.get('city_uload')
    house_area = request.form.get('house_area')
    p_visit_date=str(request.form.get('p_visit_date'))
    floor_no_load=request.form.get('floor_no_load')
    floor_no_unload=request.form.get('floor_no_unload') 
    lift_Ld=request.form.get('lift_Ld')
    lift_Ld=1
    lift_Unld=request.form.get('lift_Unld')
    print("but_id=", house_area, lift_Ld, address_to)
    #today = datetime.today()
    #today1 = today.strftime("%Y-%m-%d")
    timestamp=datetime.now()
    today1 = timestamp.strftime("%Y-%m-%d")
    #cursor.execute ( 'INSERT INTO enquiry1 (date_of_enquiry, party_name, party_mobile_no, party_mail_id, tentative_shifting_date, address_loading, city_loading, address_unloading,city_unloading, floor_no_loading, floor_no_unloading, preferred_visit_date, household_size, active )  values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(today1, party_name, contact_no,email_id, t_moving_date, address_from, city_load, address_to, city_unload, floor_no_load, floor_no_unload, p_visit_date, house_area, 1 ))
  
    cursor.execute ( 'INSERT INTO enquiry1 (party_name, party_mobile_no,party_mail_id,tentative_shifting_date, address_loading,city_loading, address_unloading, city_unloading, household_size, preferred_visit_date, lift_availability_loading,lift_availability_unloading) values (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)',(party_name,contact_no,email_id, t_moving_date,address_from,city_load,address_to, city_unload, house_area,p_visit_date,lift_Ld,lift_Unld))
    mysql.connection.commit()
    
    cursor = mysql.connection.cursor()
    insert_but=""   
    
    #When disp_list called directly there is no value to insert_but (gives error)
    insert_but=request.form.get('insert')
    if not insert_but :
        insert_but="a"                   #This is dummy value. To ensure routing, if not calling from 'insert' button selection. 
    print("but selected", insert_but)
    #cursor.execute("SELECT * FROM enquiry1")
    #cursor.execute("select enquiry1.*, memo.visit_no_id from enquiry1 left join memo ON enquiry1.enquiry_no_id = memo.enquiry_no_id;")
    cursor.execute("select enquiry1.*, visit.visit_no_id from enquiry1 left join visit ON enquiry1.enquiry_no_id = visit.enquiry_no_id;")
    data = cursor.fetchall()


    ### if material table data is present then select 
    if "Material" in insert_but :
        #memo_list()
        cursor.execute('select material_name,stock_UM from material')
        material_data = cursor.fetchall()    
        return render_template('memo_mat_list.html', material_data=material_data)
###

    cursor.execute("SELECT enquiry_no_id, memo_date FROM memo")
    memo_data = cursor.fetchall()
    for row in memo_data:
        enquiry_no_id = row[0]
        memo_date = row[1]

    return render_template('disp_table.html', data=data, memo_date=memo_data)

def memo_list(): 
    print("in memo list")
    #return render_template('disp_table.html', data=data, memo_date=memo_data)


