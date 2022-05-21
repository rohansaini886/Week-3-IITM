import pandas as pd
import sys
from jinja2 import Template
import matplotlib.pyplot as plt

def course(data, id):
    crs = []
    for i in data:
        if i[1] == int(id):
            crs.append(i[2])
    if len(crs) == 0:
        return valid()
    dict = {}
    for i in crs:
        if i not in dict.keys():
            dict[i] = 1
        else:
            dict[i] += 1
    x = list(dict.keys())
    y = list(dict.values())
    plt.bar(x, y)
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    plt.savefig("output.png")

    template = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"/>
        <title> Course Data </title>
    </head>
    <body>
        <div id="intro">
            <h1>Course Details</h1>
        </div>
        <div id="main">
            <table border = 2>
                <tr>
                    <th>Average Marks</th>
                    <th>Maximum Marks</th>
                  </tr>
                <tr>
                    <td>{{avg}}</td>
                    <td>{{max}}</td>
                </tr>
            </table>
        </div>
    <img src = "output.png" >
    </body>
</html>'''
    
    content = Template(template).render(avg = round(sum(crs)/len(crs), 2), max = max(crs))
    html_file = open('output.html', 'w')
    html_file.write(content) 
    html_file.close()


def student(data, id):
    stu = []
    total = 0
    for i in data:
        if i[0] == int(id):
            stu.append(list(i))
            total += i[2]
    if len(stu) == 0:
        return valid()
        
    template = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"/>
        <title> Student Data </title>
    </head>
    <body>
        <div id="intro">
            <h1>Student Details</h1>
        </div>
        <div id="main">
            <table border = 2>
                <thead>
                <tr>
                    <th>Student id</th>
                    <th>Course id</th>
                    <th>Marks</th>
                </tr>
                </thead>
                <tbody>
                {% for i in stu %}
                <tr>
                    <td>{{ i[0] }}</td>
                    <td>{{ i[1] }}</td>
                    <td>{{ i[2] }}</td>
                </tr>
                {% endfor %}
                </tbody>
            <tbody>
            <tr>
                <td colspan='2'>Total Marks</td>
                <td>{{total}}</td>
            </tr>
            </tbody>
            </table>
        </div>
    </body>
</html>'''

    content = Template(template).render(stu = stu, total = total)
    html_file = open('output.html', 'w')
    html_file.write(content) 
    html_file.close()
    

def valid():
    
    template = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"/>
        <title> Something Went Wrong </title>
    </head>
    <body>
        <div id="intro">
            <h1>Wrong Inputs</h1>
        </div>
        <div id="main">
            Something Went Wrong
        </div>
    </body>
</html>'''

    content = Template(template).render()
    html_file = open('output.html', 'w')
    html_file.write(content) 
    html_file.close()


d = pd.read_csv('data.csv')
data = d.values

if sys.argv[1] == "-c":
    id = sys.argv[2]  
    course(data, id)
elif sys.argv[1] == "-s":
    id = sys.argv[2] 
    student(data, id)
else:
    valid()
