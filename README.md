# tenant_project
A real estate company is looking to process tenant information for its clients. The clients have Excel files that contain each tenant's information and the various transactions incurred by the tenant. For instance, an example of a transaction is when the tenant pays rent or when the tenant pays for parking.
The data in the Excel file is not normalized. For each file, the owner of the company manually normalizes the data in each file before the data can be used for modeling purposes.


### Data Structure
The headers in the first row of the Excel file map to the Tenant Transaction data. 

Each Tenant’s data is prefixed with the word Tenant and has the following information:

 - Name
 - Code
 - Main Unit No
 - Property
 - General Contact
 - Telephone
 - Lease Start Date
 - Lease End Date
 - Vacate Date


### Rules
 - Inclusive, Exclusive and Tax are money amounts.
 - If the Inclusive amount is 0, skip that transaction.
 - If the Period cell is empty, assume the Period is the same as the last cell that wasn’t empty.
 - If Vacate Date is null, flag that tenant as Active
 - You may use the string “Software supplied by: MDA Property Systems www.mdapropsys.com” as your end of file condition.


