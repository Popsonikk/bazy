from neo4j import GraphDatabase, basic_auth
 
driver = GraphDatabase.driver("neo4j+s://88ab5c8a.databases.neo4j.io",
auth=basic_auth("neo4j", "pLaaUtuEkCQ-CUI9zGJPJugYVX8IoVGFzdnbbSXBMKs"))

while True:
    option=int(input("Podaj numer:\n1.Sprawdź Ulubione\n2.Rekomendacja Filmu\n3.Rekomendacja Aktora\n4.Zakończ\n"))
    match option:
         case 1:
            us=input("Użytkownik: ")
            cypher_query = '''
            MATCH (u:User {name:$myUser })-[r:RATED {rating:5}]->(m:Movie)
            RETURN m.title AS likedMovies ORDER BY RAND() LIMIT 50
            '''
            records, summary, keys = driver.execute_query(cypher_query, database_="neo4j",myUser=us)
            for record in records:
               print(record.data())
         case 2:
            us=input("Użytkownik: ")
            mv=input("Film: ")
            cypher_query = '''
            MATCH (u:User)-[r:RATED {rating:5}]->(m:Movie {title:$myMovie}) 
            WHERE u.name <> $myUser
            WITH u.name AS findedUser 
            ORDER BY RAND() LIMIT 1 
            MATCH (u2:User )-[r2:RATED {rating:5}]->(m2:Movie) 
            WHERE u2.name = findedUser AND m2 <> $myMovie  
            RETURN m2.title AS recommendedMovies ORDER BY RAND() LIMIT 10
            '''
            records, summary, keys = driver.execute_query(cypher_query, database_="neo4j",myUser=us,myMovie=mv)
            for record in records:
               print(record.data())   
         case 3:
            us=input("Użytkownik: ")
            mv=input("Film: ")
            cypher_query = '''
            MATCH (u:User)-[r:RATED {rating:5}]->(m:Movie {title:$myMovie})<-[:ACTED_IN]-(a:Actor) 
            WHERE u.name=$myUser 
            WITH a.name AS findedActor 
            ORDER BY RAND() LIMIT 1 
            MATCH (a2:Actor {name: findedActor})-[:ACTED_IN]->(m2:Movie) 
            WHERE m2<>$myMovie 
            RETURN m2.title AS recommendedMovies ORDER BY RAND() LIMIT 10
            '''
            records, summary, keys = driver.execute_query(cypher_query, database_="neo4j",myUser=us,myMovie=mv)
            for record in records:
               print(record.data())
         case 4:
            print("Koniec programu")
            driver.close()
            break