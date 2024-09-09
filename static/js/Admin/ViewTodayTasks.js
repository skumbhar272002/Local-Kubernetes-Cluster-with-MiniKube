const renderTodayChart = (data, labels) => {
    var ctx = document.getElementById("myChartToday").getContext("2d");
    var myChartToday = new Chart(ctx, {
      type: "pie",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Today's Tasks",
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
          text: "Today's Tasks",
        },
      },
    });
  };
  
  const getTodayChartData = () => {
    fetch("Aget_today_tasks")
      .then((res) => res.json())
      .then((Tresults) => {
        console.log('Tresults',Tresults)
        
        const Ttasks_data = Tresults.Ttype_time_data;
        
        const [labels, data] = [
          Object.keys(Ttasks_data),
          Object.values(Ttasks_data),
        ];
  
        renderTodayChart(data, labels);
      });
  };
  
  document.onload = getTodayChartData();
  