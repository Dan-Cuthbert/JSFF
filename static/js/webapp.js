maxPlayers = 14;
auctionPosition = 0;

function getInfo() {
    var player = document.getElementById("player").value;
    var cost = document.getElementById("cost").value;
    var team = document.getElementById("team").value;
    var position = document.getElementById("position").value;
    if(player != "" && cost != ""){
        updateBudget(cost, team, player, position);
    } else {
        alert("Missing player or cost");
    }
}

function undo() {
    var player = document.getElementById("player").value;
    var team = document.getElementById("team").value;
    var costAndPos = removePlayerFromTeam(team,player);
    removePlayerFromBigBoard(team,costAndPos[0],costAndPos[1]);
    resetInfo();
}

function updateBudget(cost, team, player, position) {
    var MyRows = $('table#BigBoard').find('tr');
    for (var i = 0; i < MyRows.length; i++) {
        var teamName = $(MyRows[i]).find('td:eq(0)').html();
        if(teamName == team){
            var x = document.getElementById("BigBoard").rows[i].cells;

            if(cost > parseInt(x[2].innerHTML) || parseInt(x[1].innerHTML) == 0){
                alert("Max Budget Exceeded!");
            } else {
                x[1].innerHTML = x[1].innerHTML - cost;
                x[3].innerHTML = parseInt(x[3].innerHTML) - 1;
                x[2].innerHTML = parseInt(x[1].innerHTML) - (parseInt(x[3].innerHTML)) + 1;
                if(position == "QB"){
                    x[4].innerHTML = parseInt(x[4].innerHTML) + 1;
                } else if(position == "RB"){
                    x[5].innerHTML = parseInt(x[5].innerHTML) + 1;
                } else if(position == "WR"){
                    x[6].innerHTML = parseInt(x[6].innerHTML) + 1;
                } else if(position == "TE"){
                    x[7].innerHTML = parseInt(x[7].innerHTML) + 1;
                } else if(position == "K"){
                    x[8].innerHTML = parseInt(x[8].innerHTML) + 1;
                } else{
                    x[9].innerHTML = parseInt(x[9].innerHTML) + 1;
                }
                addToRoster(cost, team, player, position);
                resetInfo();
                whosBringingOut();
                if(team == "Dan"){
                    youLikeThat();
                } else if(team == "Bob"){
                    bobRoss();
                }
            }
        }
    }
}

function resetInfo(){
    var player = document.getElementById("player").value = "";
    var cost = document.getElementById("cost").value = 1;
}

function addToRoster(cost, team, player, position){
    var table = document.getElementById(team);

    var row = table.insertRow(-1);

    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);

    cell1.innerHTML = player;
    cell2.innerHTML = cost;
    cell3.innerHTML = position;
}

function removePlayerFromTeam(team, player){
    var table = document.getElementById(team);
    for (var i = 1; i < table.rows.length; i++) {
        var row = table.rows[i].cells;
        if(row[0].innerHTML == player){
            var cost = row[1].innerHTML;
            var pos = row[2].innerHTML;
            table.deleteRow(i);
            return [cost, pos];
        }
    }
}

function removePlayerFromBigBoard(team, cost, position){
    var MyRows = $('table#BigBoard').find('tr');
    for (var i = 0; i < MyRows.length; i++) {
        var teamName = $(MyRows[i]).find('td:eq(0)').html();
        if(teamName == team){
            var x = document.getElementById("BigBoard").rows[i].cells;

            x[1].innerHTML = parseInt(x[1].innerHTML) + parseInt(cost);
            x[3].innerHTML = parseInt(x[3].innerHTML) - 1;
            x[2].innerHTML = parseInt(x[1].innerHTML) - (maxPlayers - parseInt(x[3].innerHTML)) + 1;
            if(position == "QB"){
                x[4].innerHTML = parseInt(x[4].innerHTML) - 1;
            } else if(position == "RB"){
                x[5].innerHTML = parseInt(x[5].innerHTML) - 1;
            } else if(position == "WR"){
                x[6].innerHTML = parseInt(x[6].innerHTML) - 1;
            } else if(position == "TE"){
                x[7].innerHTML = parseInt(x[7].innerHTML) - 1;
            } else if(position == "K"){
                x[8].innerHTML = parseInt(x[8].innerHTML) - 1;
            } else{
                x[9].innerHTML = parseInt(x[9].innerHTML) - 1;
            }
        }
    }
}

function whosBringingOut() {
    do {
        if(auctionPosition < 11){
            auctionPosition++;
        } else {
            auctionPosition = 0;
        }
    } while(document.getElementById(draftOrder[auctionPosition]).rows.length >= 14);

    document.getElementById("auctioneer").innerHTML = draftOrder[auctionPosition];
}

function playVictoryMusic() {
    var victoryMusic = document.getElementById("victory");
    victoryMusic.volume = 0.1;
    victoryMusic.play();
}

function youLikeThat() {
    var youLikeThat = document.getElementById("youLikeThat");
    youLikeThat.volume = 0.5
    youLikeThat.play();
}

function bobRoss() {
    var bobRoss = document.getElementById("bobRoss");
    bobRoss.volume = 1.0
    bobRoss.play();
}

var draftOrder = {};
draftOrder[0] = "Dan";
draftOrder[1] = "Steve S";
draftOrder[2] = "Andrew";
draftOrder[3] = "Alex";
draftOrder[4] = "Tom E";
draftOrder[5] = "Bob";
draftOrder[6] = "Christian";
draftOrder[7] = "Tom G";
draftOrder[8] = "Steve P";
draftOrder[9] = "Jim";
draftOrder[10] = "Ryan";
draftOrder[11] = "Eric";

var input = document.getElementById("playerSubmission");
var input2 = document.getElementById("team");
var input3 = document.getElementById("position");
input.addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        getInfo();
        var player = document.getElementById("player");
        player.focus();
    }
});
input2.addEventListener("change", function(event) {
    var player = document.getElementById("player");
    player.focus();
});
input3.addEventListener("change", function(event) {
    var player = document.getElementById("player");
    player.focus();
});