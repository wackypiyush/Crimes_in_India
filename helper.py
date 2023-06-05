import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
def state_wise(df):
    state_wise=df[(df['DISTRICT']=="TOTAL")].copy()
    state_wise['Total_Cases']=state_wise['Rape']+state_wise['Kidnapping and Abduction']+state_wise['Dowry Deaths']+state_wise['Assault on women with intent to outrage her modesty']+state_wise['Insult to modesty of Women']+state_wise['Cruelty by Husband or his Relatives']+state_wise['Importation of Girls']
    state_wise.sort_values(by=['Year','STATE/UT'],inplace=True)
    return state_wise

def year_list(df):
    years=df["Year"].unique().tolist()
    years.insert(0,'Overall')

    return years

def state_list(df):
    states=df["STATE/UT"].unique().tolist()
    states.sort()
    states.insert(0,'Overall')

    return states

def case_list():
    cases=['Overall','Rape', 'Kidnapping and Abduction',
       'Dowry Deaths', 'Assault on women with intent to outrage her modesty',
       'Insult to modesty of Women', 'Cruelty by Husband or his Relatives',
       'Importation of Girls']
    
    return cases

def state_district(df,state):
    if state!="Overall":
        districts = df[df['STATE/UT'] == state]['DISTRICT'].unique().tolist()
    else:
        districts=df['DISTRICT'].unique().tolist()
        districts.remove('TOTAL')
    return districts

def fetch_state_list(df,case,state):
    tmp_df=state_wise(df)
    tmp_df=tmp_df.reset_index(drop=True)

    if case=='Overall' and state=='Overall':
        state_grouped = tmp_df.groupby(['STATE/UT']).sum()
        state_grouped["STATE/UT"]=state_grouped.index

        plt.figure(figsize=(15,10))
        ax=sns.barplot(y="Total_Cases",x="STATE/UT",data=state_grouped)
        ax.bar_label(ax.containers[0])
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='center')
        ax.set_xlabel("STATE/UT", size=15)
        ax.set_ylabel("Total_Cases", size=15)
        plt.title(f"Total Cases of each State during 2001 to 2012",fontsize=20)
        
        return tmp_df,plt
    
    elif case=='Overall' and state!='Overall':
        tmp_df=tmp_df[tmp_df["STATE/UT"]==state.upper()]
        tmp_df.reset_index(inplace=True,drop=True)

        plt.figure(figsize=(15,10))
        ax=sns.barplot(y='Total_Cases',x="Year",data=tmp_df)
        ax.bar_label(ax.containers[0])
        ax.set_xlabel("Years", size=15)
        ax.set_ylabel("Total_Cases", size=15)
        plt.title(f"{state.capitalize()} Total Cases Per Year",fontsize=20)
        plt1=plt.gcf()

        plt.figure(figsize=(25,15))
        up=tmp_df.groupby(["DISTRICT"]).sum()
        up=up.drop(columns =["Year","Total_Cases","STATE/UT"])
        up=up.transpose()
        
        d=0.1
        separate=[d,d,d,d,d,d,d]
        ax=up.plot(kind='pie',autopct='%1.1f%%',subplots=True,figsize=(15,10),explode=separate)
        plt.title(f"Total Cases Percentage in {state}",fontsize=24)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)
        plt2=plt.gcf()
        
        return tmp_df,plt1,plt2

    elif case!='Overall' and state!='Overall':
        tmp_df=tmp_df[['STATE/UT','DISTRICT','Year',case]]
        tmp_df=tmp_df[tmp_df["STATE/UT"]==state.upper()]
        tmp_df=tmp_df.reset_index(drop=True)

        plt.figure(figsize=(15,10))
        ax=sns.barplot(y=case,x="Year",data=tmp_df)
        ax.bar_label(ax.containers[0])
        ax.set_xlabel("Years", size=15)
        ax.set_ylabel(case, size=15)
        plt.title(f"{state.capitalize()} {case} Cases Per Year",fontsize=20)
        return tmp_df,plt
    
    elif case!='Overall' and state=='Overall':
        tmp_df=tmp_df[['STATE/UT','DISTRICT','Year',case]]
        tmp_df.reset_index(inplace=True,drop=True)

        state_grouped = tmp_df.groupby(['STATE/UT']).sum()
        state_grouped["STATE/UT"]=state_grouped.index

        plt.figure(figsize=(15,10))
        ax=sns.barplot(y=case,x="STATE/UT",data=state_grouped)
        ax.bar_label(ax.containers[0])
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='center')
        ax.set_xlabel("STATE/UT", size=15)
        ax.set_ylabel(case, size=15)
        plt.title(f"Cases of {case} in each State during 2001 to 2012",fontsize=20)
        
        
        return tmp_df,plt
    

def fetch_year_wise(df,yr):
    if yr=='Overall':
        tmp_df=state_wise(df)
        plt.plot()
    else:
        tmp_df=state_wise(df)
        tmp_df=tmp_df.loc[(tmp_df["Year"]==yr)]
        tmp_df=tmp_df.reset_index(drop=True)

        plt.figure(figsize=(15,10))
        ax=sns.barplot(y="Total_Cases",x="STATE/UT",data=tmp_df)
        ax.bar_label(ax.containers[0])
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90, ha='center')
        ax.set_xlabel("STATE/UT", size=15)
        ax.set_ylabel("Total_Cases", size=15)
        plt.title(f"Total Cases in each State during {yr}",fontsize=20)
        
    
    return tmp_df,plt

def fetch_districts(df,state,district):
    df['Total_Cases']=df['Rape']+df['Kidnapping and Abduction']+df['Dowry Deaths']+df['Assault on women with intent to outrage her modesty']+df['Insult to modesty of Women']+df['Cruelty by Husband or his Relatives']+df['Importation of Girls']
    df.sort_values(by=['Year','STATE/UT'],inplace=True)
    tmp_df=df[(df["DISTRICT"]==district) & (df["STATE/UT"]==state)]
    tmp_df=tmp_df.reset_index(drop=True)

    plt.figure(figsize=(15,10))
    ax=sns.barplot(x="Total_Cases",y="Year",data=tmp_df,orient='h')
    ax.bar_label(ax.containers[0])
    ax.set_xlabel("Total_Cases", size=15)
    ax.set_ylabel("Year", size=15)
    plt.title(f"Total Cases of {district} in {state} in duration 2001-2012",fontsize=20)
    return tmp_df,plt

def fetch_total(df):
    aa=state_wise(df)
    aa=aa.groupby(['DISTRICT']).sum()
    aa.drop(['Year','Total_Cases'],axis=1,inplace=True)
    aa = aa.select_dtypes(include='number')
    aa=aa.transpose()

    d=0.1
    separate=[d,d,d,d,d,d,d]
    aa.plot(kind='pie',autopct='%1.1f%%',subplots=True,figsize=(15,10),explode=separate)
    plt.title("Overall Percentage of Cases during 2001-2012",fontsize=24)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

    return plt
    

