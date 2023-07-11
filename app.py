from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pandas


app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///tenant_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init DB
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Tenant(db.Model):
    __tablename__ = 'tenants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    code= db.Column(db.Integer())
    main_unit_no = db.Column(db.Integer())
    property = db.Column(db.String())
    general_contact = db.Column(db.String())
    telephone = db.Column(db.String())
    lease_start_date=db.Column(db.String())
    lease_end_date=db.Column(db.String())
    vacate_date=db.Column(db.String())


    def __init__(self, name, code, main_unit_no, property, general_contact, telephone, lease_start_date, lease_end_date, vacate_date):
        self.name = name
        self.code = code
        self.main_unit_no = main_unit_no
        self.property = property
        self.general_contact = general_contact
        self.telephone = telephone
        self.lease_start_date=lease_start_date
        self.lease_end_date=lease_end_date
        self.vacate_date=vacate_date

    def __repr__(self):
        return f"<Car {self.name}>"

class Transactions(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    transaction_code = db.Column(db.String())
    period = db.Column(db.String())
    date = db.Column(db.String())
    transaction = db.Column(db.String())
    remarks=db.Column(db.String())
    exclusive=db.Column(db.String())
    tax_amount = db.Column(db.String)
    inclusive = db.Column(db.String())

    def __init__(self, transaction_code, period, date, transaction, remarks, exclusive, tax_amount, inclusive):
        self.transaction_code = transaction_code
        self.period = period
        self.date =date
        self.transaction = transaction
        self.remarks = remarks
        self.exclusive = exclusive
        self.tax_amount = tax_amount
        self.inclusive = inclusive

    def __repr__(self):
        return f"<Car {self.transaction_code}>"


# Read the csv file
df = pandas.read_csv('data/MuseaumData.csv')
df['UserCode'] = df['Code'].where(df['Period'] == 'Tenant')
df['UserCode'].fillna(method='ffill', inplace=True)
df_tenants = df[df['Period'] == 'Tenant']
df_tenants['is_active'] = df['VacateDate'].isnull()
df_tenant_trans = df[df['Period'] != 'Tenant']
df_tenant_trans['Period'].fillna(method='ffill', inplace=True)
df[['Exclusive', 'Tax Amount', 'Inclusive']] = df[['Exclusive', 'Tax Amount', 'Inclusive']].apply(pandas.to_numeric,
                                                                                                    downcast='float',
                                                                                                    errors='coerce')
df_tenant_trans = df_tenant_trans[df_tenant_trans['Inclusive'] != 0]
df_tenants.reset_index()

# Return transactions
df_tenant_trans = df_tenant_trans[df_tenant_trans['Inclusive'] != 0]

@app.route('/tenants')
def get_tenant_data():
    
    for index, tenant in df_tenants.iterrows():
        stmt = Tenant(code=tenant["Code"],
                            name=tenant["Date"],
                            main_unit_no=tenant["Code"],
                            property=tenant["Tax Amount"],
                            general_contact=tenant["Name"],
                            telephone=tenant["Telephone"],
                            lease_start_date=tenant["LeaseStart"],
                            lease_end_date=tenant["LeaseEnd"],
                            vacate_date=tenant["VacateDate"])
        db.session.add(stmt)
        db.session.commit()
    return "Successful commited the data"

@app.route('/transactions')
def get_transaction_data():
    for index, trans in df_tenant_trans.iterrows():
        stmt = Transactions(transaction_code=trans['Code'],
                            period=trans['Period'], 
                            date=trans['Date'],
                            transaction=trans['Transaction'],
                            remarks=trans['Remarks'],
                            exclusive=trans['Exclusive'],
                            tax_amount=trans['Tax Amount'],
                            inclusive=trans['Inclusive'])
        
        db.session.add(stmt)
        db.session.commit()
    return "Successful commited the data"



if __name__ == '__main__':
    app.run()