var xGDataPoints = document.getElementsByClassName("Opta-events-layer")[0].childNodes;
var xGValues = "";
var teamName = "";
for (let i = 0; i< xGDataPoints.length; i++){
    if (xGDataPoints[i].getAttribute("class").includes("Opta-Home") == true){
        teamName = "0";
    }
    else{
        teamName = "1";
    }
    xGValues += teamName+","+xGDataPoints[i].getAttribute("data-value")+"\n";
}
console.log(xGValues);