from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


#! Creating the viariable which let me make more dynamic the creation of months in monthly_challenges function
monthly_challenges = {
    "January ":  "Play the violin 20 minutes per day",
    "February":  "Study 2 hours daily",
    "March":     "Make excercise 20 minutes per day",
    "April":     "Walk arround your house at least 1 hour",
    "May":       "Play the violin 20 minutes per day",
    "June":      "Study 2 hours daily",
    "July":      "Make excercise 20 minutes per day",
    "August":    "Walk arround your house at least 1 hour",
    "September": "Drink 20 litters of water every day, huh? 🤔",
    "October":   "Make 26 hours of excersie every day!",
    "November":  "Recover every calorie of the last month eating a lot of lasagne",
    "December":  "Say goodbye to this year lil bro..."
}

#* Creating dynamic paths:
def index(request):
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    #! Standard Python

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) #! /challenge/january
    return HttpResponseRedirect(redirect_path)

    #*                          This over here are hardcoded
    # return HttpResponseRedirect("/challenges/" + redirect_month)



def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
    except:
        return HttpResponseNotFound("<h1> This month is not supported </h1>")