# UrT Web Monitor 

Just another UrT Server Monitor with html5 and JS extras!
It is a python clone of urt-webmonitor

### What does it do? 

The web application tracks Urban Terror game servers and updates player and server data in a fixed interval. If you're using a modern web browser which has html5 desktop notification support, it can also send desktop notifications on certain events. 

<b>Demo:</b> <a href="http://urtweb.rs.af.cm/">http://urtweb.rs.af.cm</a> (The demo is hosted on AppFog and because of their extremely volatile service, it can be down time to time. We shall soon move it to our own hosted environment for better uptime)

### How can it help? 

Never again leave your browser to check your favorite Urban Terror game servers. Keep the application open in a tab and let it do the job for you!

### How do I install it? 

The application uses python bottle.py in the backend. You need a web server that supports python. To fetch the server data, the application also requires outbound socket connections. Some shared hosting could have such outbound connections disabled. Please check with your host in such cases. 

Edit config.json to add the servers you want to track.

### How can I report a bug / request a feature? 

Please report any issues or feature requests on Github - <a href="https://github.com/urtbd/urt-pywebmonitor/issues">https://github.com/urtbd/urt-pywebmonitor/issues</a> :) 

