# Election-Analysis

## Overview of Election Audit

A Colorado Board of Elections employee has given you the following tasts to complete the election audit of a recent local congressional election.
1. Calculate the total number of votes cast.
2. Get a complete list of counties where votes were cast.
3. Calculate the total number of votes cast in each county.
4. Calculate the total percentage of votes cast in each county.
5. Determine the county with the largest voter turnout.
6. Get a complete list of candidates who received votes.
7. Calculate the total number of votes each candidate received.
8. Calculate the percentage of votes each candidate won.
9. Determine the winner of the election based on popular votes.

## Resources
•	Data Source: election_results.csv <br>
• Software: Python 3.7.6, Visual Studio Code, 1.61.0

## Election-Audit Results
The analysis of the election show that:<br>
&emsp;•	There were 369711 votes cast in the election.<br>
&emsp;• The counties were:<br>
&emsp;&emsp;o	Jefferson which had 10.5% of the vote with 38855 votes cast.<br>
&emsp;&emsp;o	Denver which had 82.8% of the vote with 306055 votes cast.<br>
&emsp;&emsp;o	Arapahoe which had 6.7% of the vote with 24801 votes cast.<br>
&emsp;• The county with the highest voter turnout was Denver.<br>
&emsp;• The candidates were:<br>
&emsp;&emsp;o	Charles Casper Stockham<br>
&emsp;&emsp;o	Diana DeGette<br>
&emsp;&emsp;o	Raymon Anthony Doane<br>
&emsp;•	The candidate results were:<br>
&emsp;&emsp;o	Charles Casper Stockham received 23.0% of the vote and 85213 number of votes.<br>
&emsp;&emsp;o	Diana DeGette received 73.8% of the vote and 272892 number of votes.<br>
&emsp;&emsp;o	Raymon Anthony Doane received 3.1% of the vote and 11606 number of votes.<br>
&emsp;•	The winner of the election was:<br>
&emsp;&emsp;o	Diana DeGette, who received 73.8% of the vote and 272892 number of votes.

## Election-Audit Summary
The code is written to evaluate any election. By using lists and loops, the code pulls information directly from the CSV data. The use of lists creates flexibility that allows for a large number of candidates. The loops assure each row in the CSV data will be counted:

![code_example](https://user-images.githubusercontent.com/24308495/136892611-b3a1e5ba-3de1-4dde-8b3c-c989796e1074.PNG)
<br>
<br>
<br>
<br>
If a future CSV included a 4th column with party affiliation, the code could be updated to include that by integrating a list to hold the party affiliation. The party affiliation would be updated at this point in the code:

![party affiliation](https://user-images.githubusercontent.com/24308495/136894622-6170f344-e153-484c-92e8-4fc54f788956.PNG)

The affiliation could be included to the candidate_votes dictionary variable, along with the candidate name, so that it could be referenced in the text document.
<br>
<br>
<br>
<br>
The code rounds percentages off to the tenths place. This was not an issue in this specific election because the race was not particularly close. However, if this code was used to audit a close election, such as the state of Florida in the 2000 presidential election, it would need to provide a more precise number in order to be meaningful. To do this, we would update this line of code:

![more_precise_decimal](https://user-images.githubusercontent.com/24308495/136896133-a7fea85f-39e8-4aec-ad9a-9c6f8c8518be.PNG)

We would change the number in {vote_percentage:.1f} to indicate how places after the decimal we want to print. For example, if we wanted to print the number to thousandths decimal place, we would enter {vote_percentage:.3f}.


