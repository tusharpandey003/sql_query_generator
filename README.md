# sql query generator

Welcome to this GitHub repository, a unique blend of Streamlit, SQLite, and generative AI to create a Text-to-SQL generator and text information extractor.

The core functionality of this application lies in its ability to convert natural language queries into SQL queries. This is achieved through the use of a generative AI model, Gemini Pro. The model takes the user’s text input and generates the corresponding SQL query, bridging the gap between natural language and structured query language.

Once the SQL query is generated, it’s executed on a SQLite database, ‘student.db’. SQLite, a C library that provides a lightweight disk-based database, allows for a wide spectrum of queries and commands to be executed. The ‘student.db’ database is manually generated and serves as the data source for the user queries.

The results from the database query are then presented to the user, providing them with the requested information in an easy-to-understand format. This makes the application a powerful tool for anyone looking to extract information from a database using natural language.

In conclusion, this repository showcases the power of combining different technologies to create a user-friendly and functional application. It serves as a valuable resource for those interested in Streamlit, SQLite, generative AI, or natural language processing. Explore the repository and delve into the fascinating world of Text-to-SQL generation!
