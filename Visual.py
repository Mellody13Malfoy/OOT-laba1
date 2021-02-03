import psycopg2
def postgress(body):
    conn = psycopg2.connect(
        database = "d6mmd7unpk293m",
        user = "ymzvjikzasawlb",
        password = "8690ca0c44f3b15d10391b4eb3679641ebad4ff734fb52ab87e9cec37ee8fd35",
        host = "ec2-46-137-170-51.eu-west-1.compute.amazonaws.com",
        port = "5432",
    )
    
    print("Connected to PostgressSQL DB")
    
    keyboard = body
    
    get_request = "\'"+str(keyboard)+"\'"
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM film_data WHERE name % "+str(get_request)+";")
    row = cur.fetchone()
    if row is not None:
        print(row)
        a = row
        row = cur.fetchone()
    id=a[0]
    avatar=a[1]
    name=a[2]
    year=a[3]
    discription=a[4]
    link= a[5]
    return a
    print(name, year)