var express = require('express');
var app = express();
var serv = require('http').Server(app);
const {spawn} = require('child_process');

app.use(express.static(__dirname + '/client'));

// const {spawn} = require('child_process');
// const python = spawn('python', ['testpy.py', '1', '2']);
// python.stdout.on('data', function(data){
// 	console.log(data.toString());
// });

app.get('/', function(req, res) {
	res.sendFile(__dirname + '/client/signin.html');
});

app.get('/testindex', function(req, res) {

});

var server = app.listen(5000, function () {
   var host = server.address().address
   var port = server.address().port
   
   console.log("App has started and is listening at http://%s:%s", host, port)
})

var io = require('socket.io')(server,{});

io.sockets.on('connection', function(socket){
	console.log('socket connection on: ' + socket.id);
	socket.on("login", function(data){
		var isAuthenticated = false;
		var id = 0;
		const authenticatepy = spawn('python', ['\\queueing\\python_files\\authenticate.py'], data.user.toString(), data.pass.toString());
		console.log(data.user);
		authenticatepy.stdout.on('data', function(data) {
			if(data) {
				isAuthenticated = true;
				id = parseInt(data);
				console.log("login true");
			} else{
				console.log("login false")
			}
		});

	});
	
});