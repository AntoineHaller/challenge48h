import os
from .models import Pathology, User


# Renvoie la liste de toutes les maladies
def pathologyChoices():

    temp = Pathology.query.with_entities(Pathology.id, Pathology.name, Pathology.other_name).all()
    other_name_temp = []

    for x in temp:
        if x[2]:
            array = x[2].split(",")

            for i in range(len(array)):
                if array[i] is not None:
                    other_name_temp.append((x[0], array[i].strip()))

    choices = [(x[0], x[1]) for x in temp] + other_name_temp

    i = 0
    l = len(choices)
    while (i < l and choices[i]):
        if choices[i][1] == '':
            del choices[i]
            l -= 1
        else:
            i += 1

    return choices


# Renvoie la liste de tous les users
def userChoices():
    temp = User.query.with_entities(User.id, User.forename).all()
    choices = [(x[0], x[1]) for x in temp]
    return choices


# Renvoie le nom de l'utilisateur
def getUserName(userId):
    userName =  User.query.filter_by(id=userId).first_or_404().forename
    return userName


# Renvoie le nom de la pathologie
def getPathologyName(pathologyId):
    pathoName = Pathology.query.filter_by(id=pathologyId).with_entities(Pathology.name).first()
    return pathoName


# Renvoie la description de la pathologie
def getPathologyDescription(pathoId):
    pathoDesc = Pathology.query.filter_by(id=pathoId).with_entities(Pathology.description).first()
    return pathoDesc


#  Renvoie l'ICD 10 de la pathologie
def getPathologyIcd10(pathoId):
    pathoIcd10 = Pathology.query.filter_by(id=pathoId).with_entities(Pathology.icd_10).first()
    return pathoIcd10


# Renvoie le nom de la classe
def getTreatmentClassName(icd0Id):
    className = TreatmentClass.query.filter_by(icd_10=icd0Id).with_entities(TreatmentClass.pathology_name).all()
    return className


# Renvoie le nom de la molécule
def getTreatmentMoleculeName(icd0Id):
    moleculeName = TreatmentMolecule.query.filter_by(icd_10=icd0Id).with_entities(TreatmentMolecule.pathology_name).all()
    return moleculeName


# Renvoie le nom du CIS
def getTreatmentCisName(icd0Id):
    cisName = TreatmentCis.query.filter_by(icd_10=icd0Id).with_entities(TreatmentCis.pathology_name).all()
    return cisName
