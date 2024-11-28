var xGDataPoints = document.getElementsByClassName("Opta-events-layer")[0].childNodes;
var xGValues = "";
var teamName = "";
var extraDataObject;
for (let i = 0; i< xGDataPoints.length; i++){
    var extraData = "";
    if (xGDataPoints[i].getAttribute("class").includes("Opta-Home") == true){
        teamName = "0";
    }
    else{
        teamName = "1";
    }
    extraDataObject = xGDataPoints[i].getElementsByTagName("foreignObject")[0].getElementsByTagName("dd");
    for (let j = 0; j < extraDataObject.length; j++){
        extraData += extraDataObject[j].innerHTML+",";
    }
    extraData = extraData.slice(0,extraData.length-1);

    xGValues += teamName+","+xGDataPoints[i].getAttribute("data-value")+","+extraData+"\n";
}
console.log(xGValues);