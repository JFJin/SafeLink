console.log("this is the bg.js file");

chrome.runtime.onMessage.addListener(
    function(request, sender, response){
        console.log("we're in");

        $.ajax({
            url:"https://safe-link.herokuapp.com/",
            //url:"https://127.0.0.1:5000/",
            type: "POST",
            data: request,
            success: function(resp){
                console.log(resp);
                response(resp)
            },
            error: function(er, a, b){
                console.log("error has occurred");
            }
        });
        return true;
            //sendResponse(JSON.stringify(temp));
        //chrome.tabs.executeScript(null, {file: "script.js"});
    }
);