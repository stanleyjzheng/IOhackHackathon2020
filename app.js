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
	res.sendFile(__dirname + '/client/index.html');
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
		const authenticatepy = spawn('python', ['authenticate.py', data.user.toString(), data.pass.toString()]);
		authenticatepy.stdout.on('data', function(data) {
			if(data.toString() != "False") {
				isAuthenticated = true;
				id = parseInt(data.toString());
				console.log("login true");
				socket.emit("loggingin", {success: true, id: id});
			} else{
				console.log("login false")
				socket.emit("loggingin", {success: false});
			}
		});

	});
	socket.on("place_id", function(data) {
		console.log("triggered");
		var place_id = data.place_id;
		var storelist = [];
		console.log(place_id);
		const placecalculations = spawn('python', ['offlinetest.py', place_id.toString()]);
		placecalculations.stdout.on('data', function(data) {
			storelist = data.toString().split("\r\n");
			storelist = storelist.join("~");
		});
		placecalculations.on('close', function() {
			console.log(storelist);
			socket.emit("stores", {array: storelist});
		});

	})
	socket.on("registration", function(data) {
		const registerpy = spawn('python', ['new_user.py', data.first, data.last, data.email, data.pass, data.number, data.age, data.health]);
		registerpy.on('close', function() {
			console.log("Succesfully registered new user");
		});
	});
	
});

