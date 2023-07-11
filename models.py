from .app import db


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
