const renderYestChart = (data, labels) => {
    var ctx = document.getElementById("myChartYest").getContext("2d");
    var myChartYest = new Chart(ctx, {
      type: "pie",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Yesterday's Tasks",
            data: data,
            backgroundColor: [
              "rgba(255, 99, 132, 0.2)",
              "rgba(54, 162, 235, 0.2)",
              "rgba(255, 206, 86, 0.2)",
              "rgba(75, 192, 192, 0.2)",
              "rgba(153, 102, 255, 0.2)",
              "rgba(255, 159, 64, 0.2)",
            ],
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 206, 86, 1)",
              "rgba(75, 192, 192, 1)",
              "rgba(153, 102, 255, 1)",
              "rgba(255, 159, 64, 1)",
            ],
            borderWidth: 1,
          },
        ],
      },
      options: {
        title: {
          display: true,
          text: "Yesterday's Tasks ",
        },
      },
    });
  };
  
  const getYestChartData = () => {
    fetch("get_yest_tasks")
      .then((res) => res.json())
      .then((Yresults) => {
       
        const Ytasks_data = Yresults.Ytype_time_data;
       
        const [labels, data] = [
          Object.keys(Ytasks_data),
          Object.values(Ytasks_data),
        ];
        
  
        renderYestChart(data, labels);
      });
  };
  
  document.onload = getYestChartData();
  