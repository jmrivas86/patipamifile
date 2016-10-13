  /* Highlight */
  $( document ).ready(function() {
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var ws_path = ws_scheme + '://' + window.location.host + "/";
    console.log("Connecting to " + ws_path);
    var socket = new ReconnectingWebSocket(ws_path);
    // Handle incoming messages
    socket.onmessage = function (message) {
        // Decode the JSON
        console.log("Got websocket message " + message.data);
        var data = JSON.parse(message.data);
        // Handle errors
        if (data.error) {
            alert(data.error);
            return;
        }
        // Handle joining
        if (data.file_box_url) {
            var fileboxp = $(
                    "<p>" +
                    "<i class='fa fa-file' aria-hidden='true'></i>" +
                    "<a href="+ data.file_box_url +">" + data.file_name +"</a>" +
                    "</p>"
            );
            $("#box-body-"+data.box_id).append(fileboxp);
            $("#countbox-"+data.box_id).text(data.total_files+" Files");
        } else {
            console.log("Cannot handle message!");
        }
    };

    socket.onopen = function () {
        console.log("Connected to box socket");
    };
    socket.onclose = function () {
        console.log("Disconnected from box socket");
    }
  });
