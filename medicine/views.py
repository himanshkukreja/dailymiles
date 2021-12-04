from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
import os
import json


class Medicine():
    def __init__(self):
        self.loc = "static/medicines"

    def getAllMedicines(self):
        return os.listdir(self.loc)

    def getImagesOfMedicine(self, med):
        imageLoc = os.path.join(self.loc, med, "images")
        return os.listdir(imageLoc)[0]

    def getData(self, med):
        dataLoc = os.path.join(self.loc, med, "data.json")
        with open(dataLoc, 'r') as f:
            data = f.read()
        data = json.loads(data)
        return data

    def getAllData(self):
        data = []
        allMeds = self.getAllMedicines()

        for med in allMeds:
            data.append({
                "name": med,
                "link": self.getData(med)["link"],
                "img": os.path.join(self.loc, med, "images", self.getImagesOfMedicine(med))
            })

        return data


def home(request):
    obj = Medicine()
    context = {
        "title": "Daily Miles",
        "allData": obj.getAllData(),
    }
    return render(request, 'medicine/home.html', context)
