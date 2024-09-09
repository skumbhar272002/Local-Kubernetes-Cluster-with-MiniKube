const renderFilterChart = (data, labels) => {
    var ctx = document.getElementById("myChartFilter").getContext("2d");
    var myChartFilter = new Chart(ctx, {
      type: "pie",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Tasks",
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
          text: "Tasks",
        },
      },
    });
  };
  
  const getFilterChartData = () => {
    fetch("Adate-filter")
      .then((res) => res.json())
      .then((Fresults) => {
        console.log('Fresults', Fresults);
        
        const Ftasks_data = Fresults.Ftype_time_data;
        
        const [labels, data] = [
          Object.keys(Ftasks_data),
          Object.values(Ftasks_data),
        ];
  
        renderFilterChart(data, labels);
      });
  };
  
  document.onload = getFilterChartData();
  