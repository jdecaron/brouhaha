Outdated installation instructions are on the website:  
http://qwebirc.org/faq  

Additional dependencies:  
* Node and node package manager (>= 0.6.0) --- see `package.json`
  
To get started configure the `config.py` file as necessary and compile the static resources as follows:  
```
npm install
grunt
```
Now that all static files are set up and your config.py is configured for your irc server run `run.py` and navigate to `127.0.0.1:9090` and sign into the qwebirc instance.  

Now that everythings configured you can begin changing files. Run `grunt` after updating static resources to recompile the application.
