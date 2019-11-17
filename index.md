# Grade Prediction API

This site will serve as a techblog for the development of our grade prediction AI.

### Team ShallowMind members:

Cédric Chauvet, Department of Information Systems, Hanyang University<br/>
Zachary Frank, Department of Computer Science, Hanyang University<br/>
Emyl van der Kooi, Department of Nuclear Engineering, Hanyang University

## Introduction:



## Dataset:





The dataset contains 33 different variable columns, detailed below. Not all of these are useful for our project though, since they cant be applied to higher education. 





To be able to use this dataset with our neural network we have to do two things; Remove unnecessary columns, and replace non-integer values with binary integer values.

To be left with the useful columns, we run this code:
<img src="images/training.JPG" alt="code" class="inline"/>



To replace string values with integer values, we run this:
<img src="images/replace.JPG" alt="code" class="inline"/>

These two together leaves us with a 'processed-tdata.csv' file that we can load with numpy!

## Methodology:




## Evaluation and Analysis:


## Related Work:



## Conclusion:



