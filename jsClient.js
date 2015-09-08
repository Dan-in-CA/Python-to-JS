var client = new Paho.MQTT.Client("[url of pi]", Number(9001), "clientId" + Date.now().toString());

// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

//Save current msgerature
var msg = " ";

//Options object for connection
var connect_options = {
    timeout: 3,
    onSuccess: function () {
        // Connection succeeded; subscribe to our topic
        console.log('Connected!');
        client.subscribe('uicomm/p-j', {qos: 0});
    },
    onFailure: function (message) {
        alert("Connection failed: " + message.errorMessage);
    }
};

// connect the client
client.connect(connect_options);

// called when the client loses its connection
function onConnectionLost(responseObject) {
  if (responseObject.errorCode !== 0) {
    console.log("Connection Lost:"+responseObject.errorMessage);
  }
}

// called when a message arrives
function onMessageArrived(message) {
    console.log("Message Arrived:"+message.payloadString);
    $("#msg_txt").html(message.payloadString);      
}
