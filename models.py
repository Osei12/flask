
from app import db
from datetime import datetime

class  MemberRecords(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String)
    other_names = db.Column(db.String)
    gender = db.Column(db.String)
    dob = db.Column(db.String, nullable=True)
    occupation = db.Column(db.String)

    inst_of_work = db.Column(db.String)
    fathers_name = db.Column(db.String)
    mortality_father = db.Column(db.String)
    mothers_name = db.Column(db.String)
    mortality_mother = db.Column(db.String)
    marital_status = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    emergency_contact_name = db.Column(db.String)
    relations = db.Column(db.String)
    emergency_contact_no = db.Column(db.String)
    no_of_children = db.Column(db.String)
    place_of_residence = db.Column(db.String)
    house_no = db.Column(db.String)
    gps_address = db.Column(db.String)
    prominent_landmark = db.Column(db.String)
    hometown = db.Column(db.String)
    region = db.Column(db.String)
    level_of_education = db.Column(db.String)
    name_of_basic_sch = db.Column(db.String)
    name_of_2nd_cycle_sch = db.Column(db.String)
    name_of_tertiary_sch = db.Column(db.String)
    courses_offered = db.Column(db.String)
    post_grad_courses_offered = db.Column(db.String)
    when_were_you_born_again = db.Column(db.String)
    when_did_you_join_the_church = db.Column(db.String)
    baptized_by_immersion = db.Column(db.String)
    baptized_by_holy_spirit = db.Column(db.String)
    active_in_department = db.Column(db.String)
    department = db.Column(db.String)
    date_created = db.Column(db.String, default=datetime.utcnow)
    profile = db.Column(db.String, nullable=True)
    
    
    def __init__(self, surname,other_names,gender,dob,occupation,
                 inst_of_work,fathers_name,mortality_father,mothers_name,
                 mortality_mother,marital_status,email,phone,emergency_contact_name,
                 relations,emergency_contact_no,no_of_children,place_of_residence,
                 house_no,gps_address,prominent_landmark,hometown,region,level_of_education,name_of_basic_sch
                 ,name_of_2nd_cycle_sch,name_of_tertiary_sch,courses_offered,post_grad_courses_offered,
                 when_were_you_born_again,when_did_you_join_the_church,
                 baptized_by_immersion,baptized_by_holy_spirit,active_in_department,department,profile):
        
        self.surname = surname
        self.other_names=other_names
        self.gender =gender
        self.dob =dob
        self.occupation=occupation
        self.inst_of_work = inst_of_work
        self.fathers_name = fathers_name
        self.mortality_father = mortality_father
        self.mothers_name = mothers_name
        self.mortality_mother = mortality_mother
        self.marital_status =marital_status
        self.email =email
        self.phone=phone
        self.emergency_contact_name=emergency_contact_name
        self.relations=relations
        self.emergency_contact_no=emergency_contact_no
        self.no_of_children=no_of_children
        self.place_of_residence=place_of_residence
        self.house_no=house_no
        self.gps_address=gps_address
        self.prominent_landmark=prominent_landmark
        self.hometown=hometown
        self.region=region
        self.level_of_education=level_of_education
        self.name_of_basic_sch=name_of_basic_sch
        self.name_of_2nd_cycle_sch=name_of_2nd_cycle_sch
        self.name_of_tertiary_sch =name_of_tertiary_sch
        self.courses_offered =courses_offered
        self.post_grad_courses_offered=post_grad_courses_offered
        self.when_were_you_born_again=when_were_you_born_again
        self.when_did_you_join_the_church=when_did_you_join_the_church
        self.baptized_by_immersion=baptized_by_immersion
        self.baptized_by_holy_spirit=baptized_by_holy_spirit
        self.active_in_department=active_in_department
        self.department=department
        self.profile=profile
  
       
        
        
        def __repr__(self):
            return f"{self.surname}:{self.other_names}"
        
        