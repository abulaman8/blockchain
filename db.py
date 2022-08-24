import psycopg2

conn = psycopg2.connect(

    database="voteblocks",
    user = "postgres",
    password = "mahrujan",
    host = "127.0.0.1",
    port = "5432"

)

cur = conn.cursor()

# cur.execute(
#     '''CREATE TABLE VOTERS
#     (
#         ID SERIAL PRIMARY KEY NOT NULL,
#         NAME TEXT NOT NULL,
#         CONSTITUENCY TEXT NOT NULL,
#         POLLING_BOOTH TEXT NOT NULL
#     );
#     '''
# )



cur.execute(
    '''
    INSERT INTO VOTERS (NAME, CONSTITUENCY, POLLING_BOOTH)
    VALUES ('ABULAMAN', 'ODC', 'KR')
    '''
    )


conn.commit()
conn.close()