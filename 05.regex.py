# Regular expressions are a compact way of specifiying patterns in text. While Django URLconfs allow arbitrary regexes for powerful URL matching, you'll probably only use a few regex symbols in practice. Here's a selection of common symbols;

.            any single character
\d           any single digit
[A-Z]        Any character betwee A and Z (uppercase)
[A-Za-z]     Any character between a and z (case insensitive)
+            One or more of the previous expressions (e.g. \d+ matches one or more digits)
[^/]+        One or more characters until (and not including a forward slash)
?            Zero or one of the previous expressions (e.g. \d? matches zero or one digits)
*            Zero or more of the previous expressions (e.g. \d? matches zero, one, or one digits
{1, 3}       Between one and three (inclusive) of the previous expression (e.g., \d{1, 3} matches one, two or three digits)