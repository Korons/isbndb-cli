# isbndb-cli
Search book metadata from isbndb.com


### Usage:

First set up an alias for the command:

    alias isbndb="python /path/to/isbndbtool.py"

### Some interesting usage examples:

Show all info about book 'prince of thorns'

    isbndbtool -k YOUR_API_KEY -t prince of thorns

You will need to sign up at isbndb.com to get an api key. With a free api key you get 500 searchs a day
