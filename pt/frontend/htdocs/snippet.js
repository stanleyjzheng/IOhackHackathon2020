function record() {
    document.getElementById("search").onclick = function() {
      
      //document.getElementById("select").innerHTML = "Select";
  //let userData = data[msg.author.id];
  //perhaps we should print place.place(id)
  data += place.place_id
  fs.appendFile('./data.json', JSON.stringify(data),(err)=>{
    if(err) throw err;
    console.log("saved!")
    });
    }
}
