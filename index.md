# Grade Prediction API

This site will serve as a techblog for the development of our grade prediction AI.

### Team ShallowMind members:

Cédric Chauvet, Department of Information Systems, Hanyang University<br/>
Zachary Frank, Department of Computer Science, Hanyang University<br/>
Emyl van der Kooi, Department of Nuclear Engineering, Hanyang University

## Introduction:



## Dataset:
The dataset being used to train the neural network to predict grades is ta portugese survey-based grade dataset where grades and multiple variables are reported for 386 students.
https://www.kaggle.com/dipam7/student-grade-prediction

The dataset contains 33 different variable columns, detailed below. Not all of these are useful for our project though, since they cant be applied to higher education or outside of the dataset. The useful columns are in bold and the ones to be removed are in italics.<br/> 
*school - student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)<br/>* 
**sex - student's sex (binary: 'F' - female or 'M' - male)<br/>
age - student's age (numeric: from 15 to 22)<br/>
address - student's home address type (binary: 'U' - urban or 'R' - rural)<br/>**
*famsize - family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)<br/> 
Pstatus - parent's cohabitation status (binary: 'T' - living together or 'A' - apart)<br/> 
Medu - mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)<br/> 
Fedu - father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education or 4 – higher education)<br/> 
Mjob - mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')<br/> 
Fjob - father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')<br/> 
reason - reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other')<br/> 
guardian - student's guardian (nominal: 'mother', 'father' or 'other')<br/>*
**traveltime - home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)<br/> 
studytime - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)<br/> 
failures - number of past class failures (numeric: n if 1<=n<3, else 4)<br/> 
schoolsup - extra educational support (binary: yes or no)<br/>**
*famsup - family educational support (binary: yes or no)<br/> 
paid - extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)<br/>*
**activities - extra-curricular activities (binary: yes or no)<br/>** 
*nursery - attended nursery school (binary: yes or no)<br/> 
higher - wants to take higher education (binary: yes or no)<br/>* 
**internet - Internet access at home (binary: yes or no)<br/> 
romantic - with a romantic relationship (binary: yes or no)<br/>** 
*famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)<br/>*
**freetime - free time after school (numeric: from 1 - very low to 5 - very high)<br/> 
goout - going out with friends (numeric: from 1 - very low to 5 - very high)<br/> 
Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)<br/> 
Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)<br/> 
health - current health status (numeric: from 1 - very bad to 5 - very good)<br/>** 
*absences - number of school absences (numeric: from 0 to 93)<br/>
G1 - first period grade (numeric: from 0 to 20)
G2 - second period grade (numeric: from 0 to 20)*
**G3 - final grade (numeric: from 0 to 20, output target)**

To be able to use this dataset with our neural network we have to do two things; Remove unnecessary columns, and replace non-integer values with binary integer values. 

To be left with the useful columns, we run this code:
<img src="images/training.JPG" alt="code" class="inline"/>



To replace non-integer values with integer values, we run this:
<img src="images/replace.JPG" alt="code" class="inline"/>

These two together leaves us with a 'processed-tdata.csv' file that we can load with numpy!

## Methodology:




## Evaluation and Analysis:


## Related Work:



## Conclusion:



