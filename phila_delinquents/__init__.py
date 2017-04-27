ORIGINAL_HEADER = (
    'Owner',
    'OPA_Number',
    'Street_Code',
    'House_Number',
    'Principal_Due',
    'Penalty_Due',
    'Interest_Due',
    'Other_Charges_Due',
    'Total_Due',
    'Num_Yrs_Owed',
    'Most_Recent_Yr_Owed',
    'Oldest_Yr_Owed',
    'Most_Recent_Payment_Date',
    'Return_Mail',
    'Coll_Agency_Num_Yrs',
    'Coll_Agency_Most_Recent_Yr',
    'Coll_Agency_Oldest_Yr',
    'Coll_Agency_Principal_Owed',
    'Coll_Agency_Total_Owed',
    'Yr_of_Last_Assessment',
    'Total_Assessment',
    'Taxable_Assessment',
    'Exempt_Abate_Assessment',
    'Homestead_Value',
    'Net_Tax_Value_After_Hmstd',
    'Building_Code',
    'Detail_Bld_Description',
    'General_Building_Description',
    'Building_Category',
    'Property_Address',
    'City',
    'State',
    'Zip_Code',
    'Co_owner',
    'Mailing_Address',
    'Mailing_City',
    'Mailing_State',
    'Mailing_Zip',
    'Council_District',
    'x_Long',
    'Y_Lat',
    'Payment_Agreement',
    'Agreement_Agency',
    'Sequestration_Enforcement',
    'Bankruptcy',
    'Yrs_in_Bankruptcy',
    'Most_Recent_Bankrupt_Yr',
    'Oldest_Bankrupt_Yr',
    'Principal_Sum_Bankrupt_Yrs',
    'Total_Amount_Bankrupt_Yrs',
    'Sheriff_Sale',
    'Liens_Sold_1990s',
    'Liens_Sold_2015',
    'Assessment_Under_Appeal',
)

CLEAN_HEADER = (
    'owner',
    'opa_number',
    'street_code',
    'house_number',
    'principal_due',
    'penalty_due',
    'interest_due',
    'other_charges_due',
    'total_due',
    'num_years_owed',
    'most_recent_year_owed',
    'oldest_year_owed',
    'most_recent_payment_date',
    'return_mail',
    'collection_agency_num_years',
    'collection_agency_most_recent_year',
    'collection_agency_oldest_year',
    'collection_agency_principal_owed',
    'collection_agency_total_owed',
    'year_of_last_assessment',
    'total_assessment',
    'taxable_assessment',
    'exempt_abatement_assessment',
    'homestead_value',
    'net_tax_value_after_homestead',
    'building_code',
    'detail_building_description',
    'general_building_description',
    'building_category',
    'property_address',
    'city',
    'state',
    'zip_code',
    'co_owner',
    'mailing_address',
    'mailing_city',
    'mailing_state',
    'mailing_zip',
    'council_district',
    'long', #TODO: These should be lowerecased in the next dataset
    'lat',
    'payment_agreement',
    'agreement_agency',
    'sequestration_enforcement',
    'bankruptcy',
    'years_in_bankruptcy',
    'most_recent_bankrupt_year',
    'oldest_bankrupt_year',
    'principal_sum_bankrupt_years',
    'total_amount_bankrupt_years',
    'sheriff_sale',
    'liens_sold_1990s',
    'liens_sold_2015',
    'assessment_under_appeal',
)




DB_TABLE = 'TaxDelinquency'

GEOCODE_SQL = '''
    UPDATE TaxDelinquency
    SET (shape, property_address) = (
        SELECT shape, street_address FROM GIS_AIS.address_summary
        WHERE opa_account = opanumber
        AND ROWNUM = 1
    )
    WHERE shape IS NULL
'''