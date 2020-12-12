//alert("This is SafeLink");
console.log("Hello World");


var dom = document.domain;

var doc = document.documentElement.innerHTML;
//console.log(doc);

var aTag = document.getElementsByTagName("a");
//console.log(aTag[0]);

var badlinks = [];
badlinks.push(dom);
var linkdict = {};
//aTag.forEach(element => {
    //console.log(element);
//});
for (let i = 0; i < aTag.length; i++){
    //console.log(aTag[i].href);
    var link = aTag[i].href;
    badlinks.push(aTag[i])
    linkdict[link] = aTag[i]

    // if (link.indexOf('bit.ly')!=-1){
    //     linkdict[link] = aTag[i]
    //     badlinks.push(aTag[i]);
    // }
    // else if (link.indexOf('redirect') !=-1){
    //     linkdict[link] = aTag[i]
    //     badlinks.push(aTag[i]);
    // }
    // else if (link.indexOf('redirect') !=-1){
    //     linkdict[link] = aTag[i]
    //     badlinks.push(aTag[i]);
    // }
    // else if (link.indexOf(dom) == -1){
    //     linkdict[link] = aTag[i]
    //     badlinks.push(aTag[i]);
    //}
};
msgString = "";
badlinks.forEach(element => {
    msgString += element + ','

});

chrome.runtime.sendMessage({message: msgString}, function(response) {
    console.log("RESPONSE")
    var cleandata = []
    var badsites = response.substring(1, response.length-1);
    badsites = badsites.split(',')
    for (let i = 0; i<badsites.length; i++) {
        if (badsites[i].length > 5){
            cleandata.push(badsites[i].trim().substring(1, badsites[i].length-2))
        }
        //if ( i in linkdict ) 
        //highlight (linkdict[i]);
    }

    for(let i = 0; i < cleandata.length; i++){
        if (cleandata[i] in linkdict)
            console.log(cleandata[i]);
            highlight(linkdict[cleandata[i]]);
    }
    console.log('DONE')

});






//for (let i = 1; i<badlinks.length; i++) {
    //highlight (badlinks[i]);
//}


function highlight(tag) {
    if (tag){
        //var text = tag.textContent;
        var h = tag.innerHTML
        //var index = h.indexOf(text);

        //var s = h.substring(0, index) + '<span style="background-color: aquamarine;">' + h.substring(index, index+text.length) + '</span>' + h.substring(index+text.length);
        var s2 = '<span style="background-color: aquamarine;">' + h + '</span>'
        tag.innerHTML = s2;
        //console.log(text.trim());
    }

}
