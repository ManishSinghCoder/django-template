from django.shortcuts import render
from django.http import HttpResponse


projectObject = [
    {
        'id': '1',
        'title': 'newProject',
        'description': 'hey my new Project'
    },
    {
        'id': '2',
        'title': 'newProject2',
        'description': 'hey my new Project2'
    },
    {
        'id': '3',
        'title': 'newProject3',
        'description': 'hey my new Project3'
    }
]


def projects(request):
    msg = 'you are the project'
    number = 8
    context = { 'message':msg, "number": number, 'projectObj': projectObject }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    msg= "simple project"
    projectObj = None
    for i in projectObject:
        if i['id'] == pk:
            projectObj = i
    
    data = { 'message':msg, 'number': int(pk), 'projectObj': projectObj }

    return render(request, 'projects/singleProjects.html', data)

