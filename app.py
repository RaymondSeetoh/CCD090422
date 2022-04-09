#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template


# In[2]:


app =Flask(__name__)


# In[3]:


import joblib


# In[4]:


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST": #this happens after pressing button submit
        income = request.form.get("income") #add after testing
        age = request.form.get("age") #add after testing
        loan = request.form.get("loan") #add after testing
        income = float(income) #add after testing
        age = float(age) #add after testing
        loan = float(loan) #add after testing
        print(income, age, loan) #add after testing
        model1=joblib.load("CART") #add after testing
        pred1 = model1.predict([[income, age, loan]]) #add after testing
        model2=joblib.load("RF") #add after testing
        pred2 = model2.predict([[income, age, loan]]) #add after testing
        model3=joblib.load("GB") #add after testing
        pred3 = model3.predict([[income, age, loan]]) #add after testing
        return(render_template("index.html", result1=pred1, result2=pred2, result3=pred3)) #change from "1" to pred1, pred2, pred3
    else:
        return(render_template("index.html", result1="2", result2="2", result3="2")) #this happens before pressing button submit


# In[ ]:


if __name__=="__main__":
  app.run()


# In[ ]:




