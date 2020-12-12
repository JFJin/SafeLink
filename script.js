$.ajax({
    url:"http://127.0.0.1:5000/data",
    type: "POST",
    success: function(resp){
        console.log(resp);
    },
    error: function(er, a, b){
        console.log("error has occurred");
    }
});