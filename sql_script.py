
"""

Created on 15th June, 2020
@author: Alfred Ocaka

This class connects to SQL server, query data from the tables, generate indicators
and save in a CSV file

Two packages are required for the script to run; pandas and Pyodbc

i.e  pyodbc for connecting to the SQL database  and pandas for data analysis
"""
import pandas as pd 
import pyodbc


"""[SQL Connection]
Creating connection to the SQL server
"""

class  Malaria:

    df_result = ""
    
    def __init__ (self):
        pass
   

    

    def dataframes(self, df_result):

        """[summary]

        Creates connection to the SQL Server

        Query the four tables and  put them into   dataframes

        Merge the  four tables and put them in to a dataframe
        """

         sql_conn = pyodbc.connect('DRIVER={ODBC Driver  for SQL Server};
                            SERVER=CHAI;
                            DATABASE=MALARIA_FOR_COUNTRY_X;
                            Trusted_Connection=yes') 

        
        # quering FOCUS_AREA table and putting it in to  dataframe
        df_focus_area = pd.read_sql("SELECT * FROM [FOCUS_AREA]", sql_conn)

        #  quering HOUSE_HOLDS table and putting it in to   dataframe
        df_household = pd.read_sql("SELECT * FROM [HOUSE_HOLDS]", sql_conn)

        # # quering HOUSE_HOLD_MEMBERS table and putting it in to   dataframe
        df_household_members = pd.read_sql("SELECT * FROM [HOUSE_HOLD_MEMBERS]", sql_conn)

        # # quering HOUSE_HOLD_MEMBERS table and putting it in to   dataframe
        df_blood_screening = pd.read_sql("SELECT * FROM [BLOOD_SCREENING_INFO]", sql_conn)

        # Merging HOUSE_HOLD_MEMBERS   and  HOUSE_HOLDS  dataframes
        df_hh = pd.merge(df_household_members,df_household  ,on="HLD_ID", how="inner")

        # Merging df_hh results with blood screening   dataframes
        self.df_result = pd.merge(df_hh,df_blood_screening  ,on="MEMBER_ID", how="inner")
    
    def agg_results(self):
        """[]

        This methods  aggregate the output indicators

        Save the ouput to a csv file
        """

        df_result["Total Members"] = self.df_result["MEMBER_ID"]
        df_result["Total Provinces (based on house holds added)"] = self.df_result["FOCUS_AREA_ID "]
        df_result["Total Houses"] = self.df_result["HLD_ID"]
        df_result["Total Spend Night outside"] = self.df_result["SPENDS_NIGHT_OUTDOOR "]
        df_result["Total Tests Done"] = self.df_result["IS_TESTED "] is 1
        df_result["Total Positive Cases"] = self.df_result["TEST_RESULT "] is 'Positive Pf '
        df_result["Month-Year"] = self.df_result['DATE_CREATED _x'].dt.strftime('%b-%Y')

        result = df_result.groupby(df_result["Month-Year"]).agg({ 'Total Provinces (based on house holds added)':len,'Total Houses':len, 'Total Members':sum,'Total Spend Night outside':sum,'Total Tests Done':len,'Total Positive Cases':sum }).rename(columns={})
        result.to_csv("myresult.csv")

malara = Malaria()
malara.agg_results


