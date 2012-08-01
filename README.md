shortening
==========

Another implementation for the Bijective Function suggested at http://stackoverflow.com/questions/742013/how-to-code-a-url-shortener

The foo.py file, is a example of the module usage.

Usage:
	import shortening as sho
	short = sho.encurta(<id used to store the full url in a DB>)
	<variable to store the id used to store the full url in a DB> = sho.expande(short)
