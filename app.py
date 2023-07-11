from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .read_csv import read_csv



app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///tenant_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init DB
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .models import Tenant, Transactions




@app.route('/tenants')
def get_load_data():
    df_tenant_trans, df_tenants = read_csv('data/MuseaumData.csv')
    for _, tenant in df_tenants.iterrows():
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
    

    for _, trans in df_tenant_trans.iterrows():
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

    return "Successful load the data"


if __name__ == '__main__':
    app.run()
