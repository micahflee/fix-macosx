# Fix Mac OS X 

This is the code that powers <https://fix-macosx.com/>.

It is a fork of Micah Lee's <https://fixubuntu.com/>; prior to Ubuntu 14.10, Ubuntu's default behavior
was very similar to Mac OS X 10.10 Yosemite.

Copyright 2013-2014 Micah Lee, and licensed under AGPLv3. See [LICENSE](/LICENSE) for more info.

Mac OS X additions are Copyright (c) 2014 Landon Fuller <landon@landonf.org>


## Developing

* Install [Node.js](http://nodejs.org/download/)
* Install Grunt: `npm install -g grunt-cli`
* Install the Node.js dependencies: `cd fixosx && npm install`
* Run `grunt build` to build the static site,
  `grunt` to build and watch for changes (http://localhost:8001/)
