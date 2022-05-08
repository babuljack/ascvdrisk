from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .ascvd import *
# Create your views here.

def Home(request):
    return render(request,'index.html')


def Calculate(request):
    
    age=int(request.GET.get('age'));
    Totalcholesterol=int(request.GET.get('Totalcholesterol'));
    Diabetes=bool(request.GET.get('Diabetes'));
    hdl=int(request.GET.get('HDL'));
    Gender=request.GET.get('Gender');
    smoker=bool(request.GET.get('smoker'));
    Systolic=int(request.GET.get('Systolic'));
    Race=bool(request.GET.get('Race'));
    hypertensive=bool(request.GET.get('hypertensive'));
    
    ascvd = ASCVD(
        age=age,
        diabetic=Diabetes,
        smoker=smoker,
        hypertensive=hypertensive,
        systolic=Systolic,
        gender=Gender,
        hdl=hdl,
        total_cholesterol=Totalcholesterol,
        race=Race,
    )

    ten_year=ascvd.compute_ten_year_score()
    lifetime_risk=ascvd.compute_lifetime_risk()
    optimal_lifetime=ascvd.compute_optimal_lifetime()
    risk_reduction=ascvd.compute_ten_year_risk_reduction(quit_smoking=True, statin_therapy=True)
    data={
        'ten_year':ten_year,
        'lifetime_risk':lifetime_risk,
        'optimal_lifetime':optimal_lifetime,
        'risk_reduction':risk_reduction,
         
    }                               
                                        

    return JsonResponse(data)    