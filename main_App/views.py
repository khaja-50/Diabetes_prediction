from django.shortcuts import render, get_object_or_404, redirect
from .forms import PatientForm,SearchForm,editform
from django.core.paginator import Paginator
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import patient
from django.db.models import Q
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm 
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import os
from django.http  import HttpResponse

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the path to the CSV file relative to the script's directory
os.path.join(script_dir, "diabetes.csv")




def index(request):
    form = PatientForm()
    # Check if the form has been submitted
    if request.method == 'POST':
        # Bind the form to the submitted data
        form = PatientForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            diabetes_dataset=pd.read_csv(os.path.join(script_dir, "diabetes.csv"))
            df = diabetes_dataset.copy(deep = True)
            df.describe().T
            x=diabetes_dataset.drop(columns='Outcome',axis=1)#droping col 
            y=diabetes_dataset['Outcome']
            scaler=StandardScaler()
            scaler.fit(x)
            Standard_data=scaler.transform(x)
            x=Standard_data
            x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,stratify=y,random_state=2)#0.2 20% test data 
            print(x.shape,x_train.shape,x_test.shape)
            svmclassifier=svm.SVC(kernel='linear')
            svmclassifier.fit(x_train,y_train) #x_train is data and y_train is lebal
            from sklearn import metrics
            x_test_preduction=svmclassifier.predict(x_test)
            SVMP=svma=test_accuracy_score=accuracy_score(x_test_preduction,y_test)
            print(test_accuracy_score,'svm')
            from sklearn.ensemble import RandomForestClassifier
            rfc = RandomForestClassifier(n_estimators = 100, criterion = 'entropy', random_state = 0,
                                max_features = 'sqrt',max_depth = 10)
            rfc.fit(x_train, y_train)
            x_test_preduction=rfc.predict(x_test)
            RFP=rfca=test_accuracy_score=accuracy_score(x_test_preduction,y_test)
            print(test_accuracy_score,'RANDOM F')
            from sklearn.tree import DecisionTreeClassifier
            dtree = DecisionTreeClassifier()
            dtree.fit(x_train, y_train)
            x_test_preduction=dtree.predict(x_test)
            RFP= dtreea=test_accuracy_score=accuracy_score(x_test_preduction,y_test)
            print(test_accuracy_score,'DTREE')
            p= form.cleaned_data['Pregnancies']
            G= form.cleaned_data['Glucose']
            BP= form.cleaned_data['BloodPressure']
            ST= form.cleaned_data['SkinThickness']
            I= form.cleaned_data['Insulin']
            BMI= form.cleaned_data['BMI']
            DPF= form.cleaned_data['DiabetesPedigreeFunction']
            A= form.cleaned_data['Age'] 
            inputdata=(p,G,BP,ST,I,BMI,DPF,A)   
            npa=np.asarray(inputdata)
            inx=npa.reshape(1,-1)
            std_scal=scaler.transform(inx)
            std_scal
            pre=svmclassifier.predict(std_scal)
            print(pre)
            pre2=rfc.predict(std_scal)
            print(pre2)
            pre3=dtree.predict(std_scal)
            print(pre3)
            S = form.save(commit=False)
            S.Outcome = pre3    
            S.save()
            context={'result':S,'svm':pre,'rfc':pre2,'dtree':pre3,'svma':svma,'rfca':rfca,'dtreea':dtreea}
            return render(request,'report.html',context)
    else:
        context={'form': form}
        return render(request, 'index.html', context)
    
    # Render the template with the form
    
def home(request):

    return render(request,'home.html')

def report(request):
    print(request)
    return render(request,'report.html')


def Records(request):
    form = SearchForm(request.GET)
    query = request.GET.get('query')
    

    Xpatient=patient.objects.all().order_by('-id')
    count=patient.objects.count()
    if query:
        Xpatient = Xpatient.filter(
            Q(name__icontains=query) |
            Q(address__icontains=query) |  
            Q(so__icontains=query) |
            Q(Outcome__icontains=query) |
            Q(Age__icontains=query)|
            Q(BMI__icontains=query)|
             Q(BloodPressure__icontains=query)|
              Q(SkinThickness__icontains=query)|
              Q(gender__icontains=query)|
               Q(id__icontains=query)|
               Q(Pregnancies__icontains=query)|
                Q(Insulin__icontains=query)|
                 Q(Glucose__icontains=query)|
                 Q( DiabetesPedigreeFunction__icontains=query)
        )
      
    p = Paginator(Xpatient,10)
    pno = request.GET.get('page')
    pdivsions = p.get_page(pno)
    context={'divisions':pdivsions,'form': form,'query': query,'count':count}
    return render(request,'records.html',context)    



def delete_record(request,id):
    obj=patient.objects.get(id=id)
    obj.delete()
    #messages.success(request,"Record Deleted Successfully") 
    return redirect('records')   
def edit_record(request, id):
    # Retrieve the existing record from the database
    record = get_object_or_404(patient, id=id)

    if request.method == 'POST':
        # If the form is submitted with updated data
        form = editform(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('records')  # Redirect to a success page or URL
    else:
        # If it's a GET request, populate the form with the existing record's data
        form = editform(instance=record)

    context = {'form': form, 'record': record}
    return render(request, 'editform.html', context)




def report_pdf(request,id):
    record = get_object_or_404(patient, id=id)
    template_path ='pdfreport.html'
    context = {'record': record}
# Create a Django response object, and specify content_type as pdf
    response = HttpResponse (content_type='application/pdf')
    response [ 'Content-Disposition'] ='attachment; filename="report.pdf"'
# find the template and render it.
    template = get_template (template_path)
    html = template.render(context)
# create a pdf
    def link_callback(uri, rel):
    # If the URI starts with "http" or "www.", it's an external image
     if uri.startswith("http") or uri.startswith("www."):
        return uri
    # If it's a local image, make sure the image path is correct
     elif uri.startswith("/static/"):
        # Remove the leading "/static" part to get the relative path
        relative_path = uri[len("/static/"):]
        # Construct the full local path to the image
        local_path = os.path.join(os.path.dirname(__file__), relative_path)
        return local_path
    # Handle other cases if needed
     else:
        # Return an empty string or another fallback URI
        return ""

    pisa_status=pisa.CreatePDF(
        html, dest=response,
        link_callback=link_callback
    )
# if error then show some funy view
    if pisa_status.err:
       return HttpResponse ('We had some errors <pre>' + html + '</pre>')
    return response



def about(request):
    context={}
    return render(request,'about.html',context)


