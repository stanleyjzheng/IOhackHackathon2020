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

app.get('/p/:id', function(req, res) {
	var id = req.params.id;
	var type = id[0];
	var individual = "";
	for(var i = 1; i < id.length; i++) {
		individual += id[i].toString();
	}
	var info = individual.split("-");
	var iid = info[0].toString();
	if(info[1]) {
	var sid = info[1].toString();
}

	if(type=="e") {
		const isvalidpy = spawn('python', ['is_valid_shopper.py', sid, iid]);
	var validity = false;
	isvalidpy.stdout.on('data', function(data) {
		if(data.toString()=="True") {
					res.sendFile(__dirname + '/client/enter.html');
					const newshopperpy = spawn('python', ['add_to_current_shoppers.py', sid, iid]);
					newshopperpy.on('close', function() {
					console.log("added new shopper");
					var data = {id: iid, store: sid};
					io.sockets.emit("enterstore", data);

					const removevalidpy = spawn('python', ['remove_from_valid_shoppers.py', sid, iid]);
					removevalidpy.on('close', function() {
						console.log("Valid shopper removed");
					});
					var store = sid;



					const vacantpy = spawn('python', ['vacant_valid_shoppers.py', store]);
		vacantpy.stdout.on('data', function(data) {
			if (data.toString() == "True") {
				const nextpy = spawn('python', ['next_in_queue.py', store]);
				nextpy.stdout.on('data', function(data) {
					var kk = data.toString();
					const getinpy = spawn('python', ['add_to_valid_shoppers.py', store, kk]);
					getinpy.on('close', function() {
						const removequeuepy = spawn('python', ['remove_from_queue.py', store, kk]);
						removequeuepy.on('close', function() {
							console.log("succesfully moved from queue to valid shoppers");
							var package = {id: kk, store: store};
							io.sockets.emit("getin", package);
						});
					});
				});
			}
		});





			
			}); 



		} else{
			if(type=="e") {
				res.sendFile(__dirname + '/client/denied.html');
			} else{
				res.sendFile(__dirname + '/client/missing.html');
			}
		}
		});
	} else if (type=="l") {
		const leavepy = spawn('python', ['remove_from_current_shoppers', sid, iid]);
		leavepy.on('close', function() {
			console.log("Shopper left");
			var data = {id: iid, store: sid};
			io.sockets.emit("leavestore", data);
			res.sendFile(__dirname + '/client/leave.html');
		});
	} else {
		res.sendFile(__dirname + '/client/missing.html');
	}
	


	
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
	socket.on("enterqueue", function(data) {
		var id = data.id.toString();
		var store = data.store.toString();
		const enterqueuepy = spawn('python', ['add_to_queue.py', store, id]);
		enterqueuepy.on('close', function() {
			console.log("Succesfully added to queue at store " + store);
		});
		const reorderpy = spawn('python', ['sort_queue.py', store]);
		reorderpy.on('close', function() {
			console.log("Succesfully reordered");
		});

		

		const vacantpy = spawn('python', ['vacant_valid_shoppers.py', store]);
		console.log("here");
		vacantpy.stdout.on('data', function(data) {
			console.log(data.toString());
			if (data.toString() == "True") {
				console.log("here1");
				
				const nextpy = spawn('python', ['next_in_queue.py', store]);
				nextpy.stdout.on('data', function(data) {
					console.log("here2");
					var kk = data.toString();
					const getinpy = spawn('python', ['add_to_valid_shoppers.py', store, kk]);
					getinpy.on('close', function() {
						const removequeuepy = spawn('python', ['remove_from_queue.py', store, kk]);
						removequeuepy.on('close', function() {
							console.log("succesfully moved from queue to valid shoppers");
							var data = {id: kk, store: store};
							io.sockets.emit("getin", data);
							console.log(data);
						});
					});
				});
			}
		});

	});
	socket.on("leavequeue", function(data) {
		var id = data.id.toString();
		var store = data.store.toString();
		const leavequeuepy = spawn('python', ['remove_from_queue.py', store, id]);
		leavequeuepy.on('close', function() {
			console.log("Succesfully added to queue at store " + store);
		});
	});
	
});