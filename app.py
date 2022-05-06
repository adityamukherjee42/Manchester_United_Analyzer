import pandas as pd
import streamlit as st
import plotly.express as px



def tables(Standard_Stats):
    z=secondary_option(Standard_Stats)
    option_2 = st.selectbox('Select Secondary Data to view',z)
    final_columns=[( 'Unnamed: 0_level_0',  'Player')]
    for i in Standard_Stats.columns:
        if option_2==i[0]:
            final_columns.append(i)
    print(final_columns)
    Standard_Stats=Standard_Stats[final_columns]
    Standard_Stats.columns=Standard_Stats.columns.droplevel()
    list(Standard_Stats.columns).remove('Player')
    x_axis=st.selectbox('Select x axis',list(Standard_Stats.columns))
    k=list(Standard_Stats.columns)
    k.remove(x_axis)
    y_axis=st.selectbox('Select y axis',k)
    button1=st.button("Create Graph")
    if button1:
        df=Standard_Stats[[x_axis,y_axis,'Player']]
        df=df[:len(df)-2]
        fig = px.scatter(df,x=x_axis,y=y_axis,color='Player')
        st.title("Scatter plot")
        st.write('On this plot, we see the standing of eac player in relation to other players of the same team')
        st.plotly_chart(fig,use_container_width = True)
        st.sidebar.title("Current Table ")
        st.sidebar.dataframe(df)
        Standard_Stats=Standard_Stats.sort_values(x_axis,axis=0,ascending=False).reset_index(drop=True)
        st.title("Box")
        st.write('Here, we look out for the average performence of the team and weather the team as a whole is performing or there are any individual brilliances or individual disasters')
        col1, col2 = st.columns([1, 1])
        fig3 = px.box(Standard_Stats[2:len(Standard_Stats)], y=x_axis)
        fig4 = px.box(Standard_Stats[2:len(Standard_Stats)], y=y_axis)
        col1.plotly_chart(fig3,use_container_width = True)
        col2.plotly_chart(fig4,use_container_width = True)
        df_line=pd.DataFrame()
        print(Standard_Stats)
        for i in list(Standard_Stats.columns):
            if i=='Player':
                continue
            df_line['{}'.format(i)]=Standard_Stats['{}'.format(i)].rank(pct=True)
        df_line['Player']=Standard_Stats['Player']
        df_line=df_line[2:7]
        df_line=df_line.set_index('Player',drop=True)
        df_line=df_line.transpose()
        st.title("Line Plot")
        st.write('Here we take the top 5 players for all the stats and convert the values into percentile.Then we plot each as a line.This shows us the realtion between diffrent statistics')
        fig1 = px.line(df_line)
        st.plotly_chart(fig1,use_container_width = True)



def secondary_option(df):
    z=[]
    for i in df.columns:
        if 'Unnamed' in i[0]:
            continue
        z.append(i[0])
    z=list(set(z))
    return z

st.set_page_config(layout = "wide")

st.header("Manchester United Statistics")
st.write("Here we look at the individual stats taken from fbref,and compare them using data that you select.Yes this tool is an interactive and user friendly tool which gives user the power of customization which they can use to create their own graphs.")


df = pd.read_html('https://fbref.com/en/squads/19538871/Manchester-United-Stats')

Standard_Stats=df[0]
GoalKeeping=df[2]
Passing=df[5]
Advanced_Goalkeeping=df[3]
Shooting=df[4]
Pass_Types=df[6]


option_1=['Standard Stats','Goalkeeping','Passing','Advanced GoalKeeping','Shooting','Pass Types']
st.sidebar.image("logo.png")
st.sidebar.title("Select the Primary data to view")
page = st.sidebar.selectbox('Select Primary Data to view',option_1)

if page=='Standard Stats':
    z=secondary_option(Standard_Stats)
    option_2 = st.selectbox('Select Secondary Data to view',z)
    final_columns=[( 'Unnamed: 0_level_0',  'Player')]
    for i in Standard_Stats.columns:
        if option_2==i[0]:
            final_columns.append(i)
    print(final_columns)
    Standard_Stats=Standard_Stats[final_columns]
    Standard_Stats.columns=Standard_Stats.columns.droplevel()
    print(Standard_Stats)
    list(Standard_Stats.columns).remove('Player')
    x_axis=st.selectbox('Select x axis',list(Standard_Stats.columns))
    k=list(Standard_Stats.columns)
    k.remove(x_axis)
    y_axis=st.selectbox('Select y axis',k)
    button1=st.button("Create Graph")
    if button1:
        df=Standard_Stats[[x_axis,y_axis,'Player']]
        df=df[:len(df)-2]
        fig = px.scatter(df,x=x_axis,y=y_axis,color='Player')
        st.plotly_chart(fig,use_container_width = True)
        st.sidebar.title("Current Table ")
        st.sidebar.dataframe(df)
          
if page=='Goalkeeping':
    tables(GoalKeeping)
if page=='Passing':
    tables(Passing)
if page=='Advanced GoalKeeping':
    tables(Advanced_Goalkeeping)
if page=='Shooting':
    tables(Shooting)
if page=='Pass Types':
    tables(Pass_Types)







