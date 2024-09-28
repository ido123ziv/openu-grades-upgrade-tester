# Uni Grades Checker
This is a simple `pandas` project in python to determine how I can increase my BSc
Average by retaking an exam, We are entitled of re-taking 3 exams without retaking the course.

The logic is to create a product between assignments weights and my grades, 
then looping on the result dataframe to see which impact can be made.

All the data is from the OpenU website, you can clone and try on your own.

Output:
```console
If you score 87.0 (25.0 more)
 in Linear Algebra 2
 The Average will increase by: 1.047619047619051

If you score 91.0 (25.0 more)
 in Introduction to the Theory of Computations and Complexity
 The Average will increase by: 1.0

If you score 100.0 (25.0 more)
 in Logic
 The Average will increase by: 0.9523809523809632

If you score 100.0 (25.0 more)
 in Advanced Programming in Java
 The Average will increase by: 0.9523809523809632

If you score 95.0 (25.0 more)
 in Introduction to Cyber Security
 The Average will increase by: 0.9047619047619122


Process finished with exit code 0

```

# How to Start
First scrape Uni website, then:

```shell
pip install -r 'requirements.txt'
```

I'm working with `Python 3.8.3` but you can use later versions

Good luck!