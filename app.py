from flask import Flask, render_template,redirect,url_for, request,get_flashed_messages,flash
from ext import db, migrate
from werkzeug.utils import secure_filename
import uuid as uuid
import os
import io
import xlwt



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///records.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:dev123@localhost/highdb'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qfsfvbphyhsric:f6fea13cc4fa374803557d838a84043eaeddf2fabb1d957ca2c46cb2c9257ca3@ec2-52-70-45-163.compute-1.amazonaws.com:5432/d1ib009kvn4e4i'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'SJKHSHGYGTFER562768'


UPLOAD_FOLDER = 'static/images/profile/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db.init_app(app)
migrate.init_app(app,db)


## ROUTES
@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/member_list', methods=['GET', 'POST'])
def member_list():
    members = MemberRecords.query.all()
    return render_template('member_list.html', members=members)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    member = MemberRecords.query.get_or_404(id)
    if member:
        db.session.delete(member)
        db.session.commit()
        member = MemberRecords.query.all()
        flash('Deleted succesfuly')
        return redirect(url_for('home'))
    
    return render_template('index.html', member=member)


@app.route('/<int:id>/update', methods=['GET', 'POST'])
def update(id):
    
    member = MemberRecords.query.get_or_404(id)
    if request.method=="POST":
      
        if member:
            dp = request.form.getlist('department')
            department=",".join(map(str,dp))
           
            member.surname = request.form['surname']
            member.other_names = request.form['other_names']
            member.gender = request.form['gender']
            member.dob = request.form['dob']
            member.occupation = request.form['occupation']
            member.fathers_name= request.form['fathers_name']
            member.motality_father= request.form['motality_father']
            member.mothers_name= request.form['mothers_name']
            member.motality_mother= request.form['motality_mother']
            member.marital_status= request.form['marital_status']
            member.email= request.form['email']
            member.phone= request.form['mobile_number']
            member.emergency_contact_name= request.form['emergency_contact_person']
            member.relations= request.form['relations']
            member.emergency_contact_no= request.form['emergency_contact_no']
            member.no_of_children= request.form['no_of_children']
            member.place_of_residence= request.form['place_of_residence']
            member.house_no= request.form['house_no']
            member.gps_address= request.form['gps_address']
            member.prominent_landmark= request.form['prominent_landmark']
            member.hometown= request.form['hometown']
            member.region= request.form['region']
            member.level_of_education= request.form['level_of_education']
            member.name_of_basic_sch= request.form['name_basic_sch']
            member.name_of_2nd_cycle_sch= request.form['name_of_2nd_cycle_sch']
            member.name_of_tertiary_sch= request.form['name_tertiary_sch']
            member.courses_offered= request.form['courses_offered']
            member.post_grad_courses_offered= request.form['post_grad_courses']
            member.when_were_you_born_again= request.form['when_were_born_again']
            member.when_did_you_join_the_church= request.form['when_did_you_join_the_church']
            member.baptized_by_immersion= request.form['baptized_by_immersion']
            member.baptized_by_holy_spirit= request.form['baptized_by_holy_spirit']
            member.active_in_department= request.form['active_department']
            member.department=department
    
            if request.files['upload']:
                member.profile = request.files['upload']
                member.profile=request.files['upload']
                pic_filename = secure_filename( member.profile.filename)
                pic_name = str(uuid.uuid1()) + " _ " + pic_filename
                saver = request.files['upload']
                saver.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
                member.profile=pic_name                
                db.session.commit()
                flash('Updated succesfuly')
                return redirect(url_for('home'))
            else:
                
                db.session.commit()
                flash('Updated succesfuly')
                return redirect(url_for('home'))
                
    return render_template('update.html', member = member)




@app.route('/create', methods=['GET', 'POST'])
def create():
    members = MemberRecords.query.all()
    if request.method=='GET':
         return render_template('add_member.html', members=members)
    if request.method=='POST':
        dp = request.form.getlist('department')
        department=",".join(map(str,dp))
        
        surname = request.form['surname']
        other_names = request.form['other_names']
        gender = request.form['gender']
        dob = request.form['dob']
        occupation = request.form['occupation']
        inst_of_work = request.form['inst_of_work']
        fathers_name= request.form['fathers_name']
        motality_father= request.form['motality_father']
        mothers_name= request.form['mothers_name']
        motality_mother= request.form['motality_mother']
        marital_status= request.form['marital_status']
        email= request.form['email']
        phone= request.form['mobile_number']
        emergency_contact_name= request.form['emergency_contact_person']
        relations= request.form['relations']
        emergency_contact_no= request.form['emergency_contact_no']
        no_of_children= request.form['no_of_children']
        place_of_residence= request.form['place_of_residence']
        house_no= request.form['house_no']
        gps_address= request.form['gps_address']
        prominent_landmark= request.form['prominent_landmark']
        hometown= request.form['hometown']
        region= request.form['region']
        level_of_education= request.form['level_of_education']
        name_of_basic_sch= request.form['name_basic_sch']
        name_of_2nd_cycle_sch= request.form['name_of_2nd_cycle_sch']
        name_of_tertiary_sch= request.form['name_tertiary_sch']
        courses_offered= request.form['courses_offered']
        post_grad_courses_offered= request.form['post_grad_courses']
        when_were_you_born_again= request.form['when_were_born_again']
        when_did_you_join_the_church= request.form['when_did_you_join_the_church']
        baptized_by_immersion= request.form['baptized_by_immersion']
        baptized_by_holy_spirit= request.form['baptized_by_holy_spirit']
        active_in_department= request.form['active_department']

        department=department
        profile = request.files['upload']
        if profile.filename is None:
            profile=request.form['no-pic']
            members = MemberRecords(
            surname=surname,
            other_names=other_names,
            gender=gender,
            dob=dob,
            occupation=occupation,
            inst_of_work=inst_of_work,
            fathers_name=fathers_name,
            mortality_father=motality_father,
            mothers_name=mothers_name,
            mortality_mother=motality_mother,
            marital_status=marital_status,
            email=email,
            phone=phone,
            emergency_contact_name=emergency_contact_name,
            relations=relations,
            emergency_contact_no=emergency_contact_no,
            no_of_children=no_of_children,
            place_of_residence=place_of_residence,
            house_no=house_no,
            gps_address=gps_address,
            prominent_landmark=prominent_landmark,
            hometown=hometown,
            region=region,
            level_of_education=level_of_education,
            name_of_basic_sch=name_of_basic_sch,
            name_of_2nd_cycle_sch=name_of_2nd_cycle_sch,
            name_of_tertiary_sch=name_of_tertiary_sch,
            courses_offered=courses_offered,
            post_grad_courses_offered=post_grad_courses_offered,
            when_were_you_born_again=when_were_you_born_again,
            when_did_you_join_the_church=when_did_you_join_the_church,
            baptized_by_immersion=baptized_by_immersion,
            baptized_by_holy_spirit=baptized_by_holy_spirit,
            active_in_department=active_in_department,
            
            profile=profile,
            department=department
                
            )
            db.session.add(members)
            db.session.commit()
        else:
            pic_filename = secure_filename(profile.filename)
            pic_name = str(uuid.uuid1()) + " _ " + pic_filename
            saver = request.files['upload']
            saver.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
            profile=pic_name
    
            members = MemberRecords(
                
                surname=surname,
                other_names=other_names,
                gender=gender,
                dob=dob,
                occupation=occupation,
                inst_of_work=inst_of_work,
                fathers_name=fathers_name,
                mortality_father=motality_father,
                mothers_name=mothers_name,
                mortality_mother=motality_mother,
                marital_status=marital_status,
                email=email,
                phone=phone,
                emergency_contact_name=emergency_contact_name,
                relations=relations,
                emergency_contact_no=emergency_contact_no,
                no_of_children=no_of_children,
                place_of_residence=place_of_residence,
                house_no=house_no,
                gps_address=gps_address,
                prominent_landmark=prominent_landmark,
                hometown=hometown,
                region=region,
                level_of_education=level_of_education,
                name_of_basic_sch=name_of_basic_sch,
                name_of_2nd_cycle_sch=name_of_2nd_cycle_sch,
                name_of_tertiary_sch=name_of_tertiary_sch,
                courses_offered=courses_offered,
                post_grad_courses_offered=post_grad_courses_offered,
                when_were_you_born_again=when_were_you_born_again,
                when_did_you_join_the_church=when_did_you_join_the_church,
                baptized_by_immersion=baptized_by_immersion,
                baptized_by_holy_spirit=baptized_by_holy_spirit,
                active_in_department=active_in_department,
                profile=profile,
                department=department
                
            )
            db.session.add(members)
            db.session.commit()
            flash('Member added succesfuly')
            return redirect(url_for('create'))



@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    return render_template('dashboard.html')


@app.route('/download/report/excel')
def download_report():
    
    
    all_members = MemberRecords.query.all()

    output = io.BytesIO()
    workbook = xlwt.Workbook()
    
    sh = workbook.add_sheet('Member_report')
    
    
    sh.write(0, 0, 'ID')
    sh.write(0, 1, 'Surname')
    sh.write(0, 2, 'Other Names')
    sh.write(0, 3, 'Gender')
    
    return render_template('index.html', all_members=all_members)

from models import MemberRecords

with app.app_context():
    db.create_all()


if __name__=="__main__":
    app.run(debug=True)
    
