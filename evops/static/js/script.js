var map = L.map('map')
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

$(document).ready(function () {
    const ctx = document.getElementById("myChart").getContext("2d");
  
    const myChart = new Chart(ctx, {
      type: "line",
      data: {
        datasets: [{ label: "Population Average Fitness",  }],
      },
      options: {
        borderWidth: 3,
        borderColor: ['rgba(89, 131, 75, 1)',],
      },
    });
  
    function addData(label, data) {
      myChart.data.labels.push(label);
      myChart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
      });
      myChart.update();
    }
  
    function removeFirstData() {
      myChart.data.labels.splice(0, 1);
      myChart.data.datasets.forEach((dataset) => {
        dataset.data.shift();
      });
    }
  
    const MAX_DATA_COUNT = 200;
    //connect to the socket server.
    //   var socket = io.connect("http://" + document.domain + ":" + location.port);
    var socket = io.connect();
  
    //receive details from server
    socket.on("updateSensorData", function (msg) {
      console.log("Received sensorData :: " + msg.date + " :: " + msg.value);
  
      // Show only MAX_DATA_COUNT data
      if (myChart.data.labels.length > MAX_DATA_COUNT) {
        removeFirstData();
      }
      addData(msg.date, msg.value);
    });
  });
