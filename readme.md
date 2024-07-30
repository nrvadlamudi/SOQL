This is SOQL, a SQL injection library that obfuscates SQL commands so that the desired command can bypass certain Web Application Firewalls (WAFs).
The generator allows for several types of obfuscation, including: Inline Comment Transformation, URL Encoding, Invalid Percent Endoding, and Nesting Stripped Expressions.

The purpose of this generator is to provide a pipeline to generate obfuscation or transform large datasets of regular SQL expressions to create datasets used for training classification models that can detect malicious obfuscated SQL queries. 

My paper detailing all of the steps of this process and the results of the resulting classification models can be read [here](https://github.com/nrvadlamudi/SOQL/blob/main/annotated-nrv434_final.pdf)
