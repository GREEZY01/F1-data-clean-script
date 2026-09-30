# i tried to maake this code as least messy as possible
import pandas as pd

additional_years = 0
input_path = r"C:\Users\ggeor\Desktop\F1 DATA\F1 data project - Sheet1.csv"
output_path = r"C:\Users\ggeor\Desktop\F1 DATA\F1 data project - Sheet1 - cleaned.csv"

clean_years = [
    
]

df = pd.read_csv(input_path)






# ---------------------------  
# removes "[]", "()" and any text inside of the every df elemnt
def remove_uneeded_characters(column):

    df[column] = df[column].str.replace(r'\[.*\]', '', regex=True)
    df[column] = df[column].str.replace(r'\(.*\)', '', regex=True)
    return df[column]

# ---------------------------    



# ---------------------------  
# gets rid of the en dash in the seasoons completed collumn, and expands the range of years into a list of individual years
for i in range(len(df)):


    years = df['Seasons competed'][i].encode('utf-8')
    years = years.decode('utf-8').replace(u'\u2013', '-').replace(' ', '')  # replace en dash with hyphen (bro i thought it was an em dash it took me ages to figure it out lmfao)
    years = list(years.split(','))
     
    
    additional_years = 0
    for i in range(len(years)):
            
            
        if '-' in str(years[i + additional_years ]):
            a, b = years[i + additional_years].split('-')
            a = int(a)
            b = int(b)
                
            years.remove(years[i + additional_years])
            for j in range(a, b + 1):
                years.insert(0, j)
                additional_years += 1
            additional_years -=1
            
        else:
            pass
    clean_years.append(years)
#---------------------------------      
            



# ---------------------------  
# removes nationality column 
df = df.drop("Nationality", axis=1) 

# removes unneeded characters 
df["Race entries"]  = pd.DataFrame({'Race entries': remove_uneeded_characters("Race entries")}) 
df["Podiums"] = pd.DataFrame({'Podiums': remove_uneeded_characters("Podiums")})
df["Race wins"] = pd.DataFrame({'Race wins': remove_uneeded_characters("Race wins")})
df["Points[a]"] = pd.DataFrame({'Points[a]': remove_uneeded_characters("Points[a]")})
df["Race starts"] = pd.DataFrame({'Race starts': remove_uneeded_characters("Race starts")})
df["Fastest laps"] = pd.DataFrame({'Fastest laps': remove_uneeded_characters("Fastest laps")})
df["Driver name"] = pd.DataFrame({'Driver name': remove_uneeded_characters("Driver name")})
    
df["Seasons competed"] = pd.DataFrame({'Seasons competed': clean_years}) # replaces seasons completed column in my data fraom with the clean years.

df.to_csv(r"C:\Users\ggeor\Desktop\F1 DATA\Improved F1 data project - Sheet1 - cleaned.csv", index=False) 
# ---------------------------  

