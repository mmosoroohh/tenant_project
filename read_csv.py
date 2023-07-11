import pandas

def read_csv(csv_file):
    # Read the csv file
    df = pandas.read_csv(csv_file)
    df['UserCode'] = df['Code'].where(df['Period'] == 'Tenant')
    df['UserCode'].fillna(method='ffill', inplace=True)
    df_tenants = df[df['Period'] == 'Tenant']
    df_tenants['is_active'] = df['VacateDate'].isnull()
    df_tenant_trans = df[df['Period'] != 'Tenant']
    df_tenant_trans['Period'].fillna(method='ffill', inplace=True)
    df_tenant_trans[['Exclusive', 'Tax Amount', 'Inclusive']] = df_tenant_trans[['Exclusive', 'Tax Amount', 'Inclusive']].apply(pandas.to_numeric,
                                                                                                        downcast='float',
                                                                                                        errors='coerce')
    df_tenant_trans = df_tenant_trans[df_tenant_trans['Inclusive'] != 0]
    df_tenants.reset_index()

    # Return transactions
    df_tenant_trans = df_tenant_trans[df_tenant_trans['Inclusive'] != 0]

    return df_tenant_trans, df_tenants