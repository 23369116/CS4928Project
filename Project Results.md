## RQ1 (M2 bounded reproduction)
The paper found a statistically significant difference in the co-occurrence of SAT-specific warnings and smell presence, after comparing multiple different Static Analysis Tools with each other alongside architectural smells and getting a variety of p-values for each.

We compared a number of Java projects with PMD alongside our architectural smells program Designite and obtained a p-value correlation of 1.5214904766760475e-96, which is a statistically insignificant correlation. 

It is likely that our method of reproduction was incorrect in some fashion which lead to such a low result. We cannot claim to have reproduced the paper's results.

## Event A 
Event A was attempting to find a p-value correlation on just one Java project and comparing its results to M2.

After running our earlier setup on the Java project Freemind from the dataset, we obtained a p-value correlation of 0.0002584864021800933.

This value is also statistically insignificant, yet it is higher than M2 and shows a higher correlation between architectural smells and static analysis warnings than M2.

## M4


## Event B 
Event B involved adding a new dependency across modules in a selected Java project and re-running our analysis to see if the correlation between smells and warnings changed.

Our results indicate a somewhat statistically significant p-value correlation of 0.087979.

This shows that the added dependencies increased the correlation between architectural smells and static analysis warnings compared to the previous analysis without said dependencies, adding credence to the idea that the relationship strengthens depending on code smells, despite our low interpretation value.



