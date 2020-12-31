# -*- coding: utf-8 -*-
"""applicrecneed.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IQjAtmOvXmMqnM67NjuETOzya3cSaeWO

This code is to select the suitable Application records according to the selected credidit cart records
"""

import pandas as pd
names =['ID','Feature1','Feature2','Feature3','labels']
df = pd.read_csv('drive/My Drive/credit_record_new.csv',header=None,sep=',',names=names)
print(df)

import numpy as np
ID_vector_Credit_Card=np.int64(np.array(df['ID']))
print(ID_vector_Credit_Card.dtype)

"""Now, we import the application records and seletc the same ID from credit cards records"""

names =['ID','CODE_GENDER','FLAG_OWN_CAR','FLAG_OWN_REALTY','CNT_CHILDREN',\
        'AMT_INCOME_TOTAL','NAME_INCOME_TYPE','NAME_EDUCATION_TYPE','NAME_FAMILY_STATUS','NAME_HOUSING_TYPE',\
        'DAYS_BIRTH','DAYS_EMPLOYED','FLAG_MOBIL','FLAG_WORK_PHONE','FLAG_PHONE',\
        'FLAG_EMAIL','OCCUPATION_TYPE','CNT_FAM_MEMBERS',]
print(names)

df1 = pd.read_csv('drive/My Drive/application_record.csv',header=0,sep=',',names=names)
print(df1)

"""Ok, we have import the application data. Now, we need to transform the data into avaliable format, i.e., numercal format."""

ID_vector_Application=np.array(df1['ID'])
Gender_vector=np.array(df1['CODE_GENDER'])
Car_vector=np.array(df1['FLAG_OWN_CAR'])
Property_vector=np.array(df1['FLAG_OWN_REALTY'])
Children_vector=np.array(df1['CNT_CHILDREN'])
IncomeAnnual_vector=np.array(df1['AMT_INCOME_TOTAL'])
IncomeType_vector=np.array(df1['NAME_INCOME_TYPE'])
Edu_vector=np.array(df1['NAME_EDUCATION_TYPE'])
Housing_vector=np.array(df1['NAME_HOUSING_TYPE'])
Age_vector=np.array(df1['DAYS_BIRTH'])
WorkingAge_vector=np.array(df1['DAYS_EMPLOYED'])

print(ID_vector_Application.dtype)

LengthApplRec=len(ID_vector_Application)
other=[]

for index in range(LengthApplRec):
  if Gender_vector[index]=='F':
    Gender_vector[index]=-1
  else:
    Gender_vector[index]=1
  
  if Car_vector[index]=='Y':
    Car_vector[index]=1
  else:
    Car_vector[index]=-1

  if Property_vector[index]=='Y':
    Property_vector[index]=1
  else:
    Property_vector[index]=-1

  if IncomeType_vector[index]=='Working':
    IncomeType_vector[index]=1;
  elif IncomeType_vector[index]=='Commercial associate':
    IncomeType_vector[index]=2;
  elif IncomeType_vector[index]=='Pensioner':
    IncomeType_vector[index]=3;
  elif IncomeType_vector[index]=='State servant':
    IncomeType_vector[index]=4;
  elif IncomeType_vector[index]=='Student':
    IncomeType_vector[index]=5;
  

  if Edu_vector[index]=='Secondary / secondary special':
    Edu_vector[index]=1;
  elif Edu_vector[index]=='Higher education':
    Edu_vector[index]=2;
  elif Edu_vector[index]=='Incomplete higher':
    Edu_vector[index]=3;
  elif Edu_vector[index]=='Lower secondary':
    Edu_vector[index]=4;
  elif Edu_vector[index]=='Academic degree':
    Edu_vector[index]=5;

  if Housing_vector[index]=='House / apartment':
    Housing_vector[index]=1;
  elif Housing_vector[index]=='With parents':
    Housing_vector[index]=2;
  elif Housing_vector[index]=='Municipal apartment':
    Housing_vector[index]=3;
  elif Housing_vector[index]=='Rented apartment':
    Housing_vector[index]=4;
  elif Housing_vector[index]=='Co-op apartment':
    Housing_vector[index]=5;
  elif Housing_vector[index]=='Office apartment':
    Housing_vector[index]=5;


print(Gender_vector)
print(Car_vector)
print(Property_vector)
print(IncomeType_vector.shape)
print(Edu_vector)
print(Housing_vector)

Age_vector=(Age_vector.astype(float))/365
WorkingAge_vector=(WorkingAge_vector.astype(float))/365

print(Age_vector)
print(WorkingAge_vector)

"""Now, we could divide the application into training set and test set according to the ID in credit card records"""

LengthCrelRec=len(ID_vector_Credit_Card)
ID_vector_Appl_train=[]
ID_vector_Appl_test=[]

Gender_vector_train=[]
Gender_vector_test=[]

Car_vector_train=[]
Car_vector_test=[]

Property_vector_train=[]
Property_vector_test=[]

Children_vector_train=[]
Children_vector_test=[]

IncomeAnnual_vector_train=[]
IncomeAnnual_vector_test=[]

IncomeType_vector_train=[]
IncomeType_vector_test=[]

Edu_vector_train=[]
Edu_vector_test=[]

Housing_vector_train=[]
Housing_vector_test=[]

Age_vector_train=[]
Age_vector_test=[]

WorkingAge_vector_train=[]
WorkingAge_vector_test=[]

Labels_vector_train=[]

Label_credid_card=np.array(df['labels'])
deletePosition=[]

for index in range(LengthCrelRec):
  position=np.argwhere(ID_vector_Application==ID_vector_Credit_Card[index])
  if not position:
    deletePosition.append(position)
  else:
    ID_vector_Appl_train.append(ID_vector_Credit_Card[index])
    Gender_vector_train.append(Gender_vector[position])
    Car_vector_train.append(Car_vector[position])   
    Property_vector_train.append(Property_vector[position])   
    Children_vector_train.append(Children_vector[position])   
    IncomeAnnual_vector_train.append(IncomeAnnual_vector[position]) 
    IncomeType_vector_train.append(IncomeType_vector[position])   
    Edu_vector_train.append(Edu_vector[position])
    Housing_vector_train.append(Housing_vector[position])   
    Age_vector_train.append(Age_vector[position])   
    WorkingAge_vector_train.append(WorkingAge_vector[position])
    Labels_vector_train.append(Label_credid_card[index])

"""Now, we could make the training set file and testing set file"""

training_set=np.array([ID_vector_Appl_train,Labels_vector_train,Gender_vector_train,Car_vector_train,Property_vector_train,Children_vector_train,IncomeAnnual_vector_train,IncomeType_vector_train,Edu_vector_train,Housing_vector_train,Age_vector_train,WorkingAge_vector_train]);
print(training_set.shape)
names=['ID_vector_Appl_train','Labels_vector_train','Gender_vector_train','Car_vector_train','Property_vector_train','Children_vector_train','IncomeAnnual_vector_train','IncomeType_vector_train','Edu_vector_train','Housing_vector_train','Age_vector_train','WorkingAge_vector_train']
np.savetxt('drive/My Drive/CreditCardTraining_set.csv', training_set.T,delimiter = ',' )

ID_vector_Appl_test=ID_vector_Application.copy()
Gender_vector_test=Gender_vector.copy()
Car_vector_test=Car_vector.copy()
Property_vector_test=Property_vector.copy()
Children_vector_test=Children_vector.copy()
IncomeAnnual_vector_test=IncomeAnnual_vector.copy()
IncomeType_vector_test=IncomeType_vector.copy()
Edu_vector_test=Edu_vector.copy()
Housing_vector_test=Housing_vector.copy()
Age_vector_test=Age_vector.copy()
WorkingAge_vector_test=WorkingAge_vector.copy()

print(ID_vector_Appl_test.shape)

position=[]
for index in range(len(ID_vector_Appl_train)):
  position.append(np.argwhere(ID_vector_Application==ID_vector_Appl_train[index]))
position=np.array(position)

ID_vector_Appl_test=np.delete(ID_vector_Appl_test,position)
Gender_vector_test=np.delete(Gender_vector_test,position)
Car_vector_test=np.delete(Car_vector_test,position)
Property_vector_test=np.delete(Property_vector_test,position)
Children_vector_test=np.delete(Children_vector_test,position)
IncomeAnnual_vector_test=np.delete(IncomeAnnual_vector_test,position)
IncomeType_vector_test=np.delete(IncomeType_vector_test,position)
Edu_vector_test=np.delete(Edu_vector_test,position)
Housing_vector_test=np.delete(Housing_vector_test,position)
Age_vector_test=np.delete(Age_vector_test,position)
WorkingAge_vector_test=np.delete(WorkingAge_vector_test,position)
print(ID_vector_Appl_test.shape)

testing_set=np.array([ID_vector_Appl_test,Gender_vector_test,Car_vector_test,Property_vector_test,Children_vector_test,IncomeAnnual_vector_test,IncomeType_vector_test,Edu_vector_test,Housing_vector_test,Age_vector_test,WorkingAge_vector_test]);
print(testing_set.shape)
np.savetxt('drive/My Drive/CreditCardPrediction_set.csv', testing_set.T,delimiter = ',' )