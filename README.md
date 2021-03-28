<h2>CRAZY PYTHON LOOPS</h2>
Sample 2021
```# original list
school = [["Mary", "Jack", "Tiffany"], 
          ["Brad", "Claire"],
          ["Molly", "Andy", "Carla"]]
```
Standard itteration:
```student_list = []
for class_group in school:
    for student in class_group:
        print(student)
```
Crazy Python list comprehention:
```student_list = [student   for class_group in school   for student in class_group]
                             \___ FIRST ITTERATION ___/  \__ SECOND ITTERATION ____/
```



<i>HTML works</i>
<p>
  How to NEST for-in lopps? <br />
  It is not simle...
  Imagine you have sub-list like that:
  
  text = [("abc","def"),("ghi","ijk"),("lmn","opr")]
  
  text<br />
  >>[tuple<br />
  >>>>[string<br />
  >>>>>>[letter<br />
  
  Loop to iterate inside text:<br />
  <b>for <i>tuple</i> in text</b>   # this will return list of tuples<br />
  <br />
  We have tuples, now we want to iterete inside them:<br />
  <b>for tuple in text + for <i>string</i> in tuple</b>   # this will return list of strings<br />
  <br />
  We have now tuples and strings, now we want to iterete inside strings:<br />
  <b>for tuple in text + for string in tuple + for <i>letter</i> in string</b>  # this will return list of letters<br />
  <br />
  Now as we iterated throu text, tuples, strings and letters we can request at at the begining of phrase what do we want to read (letter)<br />
  <b><i>letter</i> for tuple in text + for string in tuple + for <i>letter</i> in string</b><br />
  DONE!
</p>



<p>
# 2-D List of planets <br>
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']] 
</p>
<p>
# Nested List comprehension with an if condition <br> 
flatten_planets = [planet for sublist in planets for planet in sublist if len(planet) < 6] 
<br>          
print(flatten_planets) </p>
