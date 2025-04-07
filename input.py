import csv

names = []
salary_hours = []
salary = []

with open('input.csv', 'r') as file:
    csv_file = csv.DictReader(file, delimiter=',')
    for line in csv_file:
        names.append(line['name'])
        salary_hours.append(line['worked_hours'])
        

for hours in salary_hours:
        salary.append(float(hours) * 15)
        
with open('output.csv', 'w') as file:
    csv_file = csv.writer(file)
    csv_file.writerow(['name', 'salary'])
    csv_file.writerows(zip(names, salary))

# Another way with functions
def extract(filename='input.csv'):
    datas = []
    with open(filename, 'r') as file:
        csv_file = csv.DictReader(file)
        for lines in csv_file:
            datas.append(lines)
        return datas


def transform(datas_to_transform):
    datas_to_load = []
    for data in datas_to_transform:
        transformed_data = {}
        transformed_data['name'] = data['name']
        transformed_data['salary'] = int(data['worked_hours']) * 15
        datas_to_load.append(transformed_data)
    return datas_to_load

def load(datas_to_load, filename='output_2.csv'):
    with open(filename, 'w') as file:
        fieldnames = ['name', 'salary']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for data in datas_to_load:
            writer.writerow(data)

def pipeline():
    extract_datas = extract('input.csv')
    load_datas = transform(extract_datas)
    load(load_datas, 'output_2.csv')

pipeline()