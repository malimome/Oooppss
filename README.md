Oooppss
=======
This is a failed project!
If you are using two keyboard layouts in your system and you have never said OoOppss after typing something into google search or the address bar, you have always been lucky to have the right layout. 
But it happens to many people when something is typed in language X layout but it was supposed to be english. 
This website written in Python (django) is supposed to fix this problem. For each keyboard layout L commonly used in the world, and for each top viewed websites W, a page LW exists in this site. Th page LW contains the domain name for the website W as if typed in keyboard layout L. So search engines will index these pages using the keywords in them. 
Now a user searches for the website W in the layout L and we expected to see the page LW in the results of the search. Then the user clicks on the link to page LW and the page will redirect to the right website. 

But this didn't work! While our site was indexed by search engines but it was not shown as a top result in google because the google crawler was confused because the site would redirect to another site. 
