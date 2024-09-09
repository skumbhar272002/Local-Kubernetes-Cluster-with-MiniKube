const renderWeeklyChart = (mondata,tuedata,weddata,thudata,fridata,satdata,sundata) => {
const ctx = document.getElementById('myChartWeekly').getContext('2d');
const myChartWeekly = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Breaks', 'Tasks', 'Meetings'],
        datasets: [
            
        {
            label: 'Monday',
            data: mondata,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)'
                
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)'
            
            ],
            borderWidth: 1
        },





        {
            label: 'Tuesday',
            data: tuedata,
            backgroundColor: [
                'rgba(5, 99, 132, 0.2)',
                'rgba(54, 162, 25, 0.2)',
                'rgba(255, 206, 86, 0.2)'
                
            ],
            borderColor: [
                'rgba(55, 99, 132, 1)',
                'rgba(54, 12, 235, 1)',
                'rgba(5, 6, 86, 1)'
            
            ],
            borderWidth: 1
        },



        {
            label: 'Wednesday',
            data: weddata,
            backgroundColor: [
                'rgba(5, 99, 132, 0.2)',
                'rgba(54, 162, 25, 0.2)',
                'rgba(255, 206, 86, 0.2)'
                
            ],
            borderColor: [
                'rgba(55, 99, 132, 1)',
                'rgba(54, 12, 235, 1)',
                'rgba(5, 6, 86, 1)'
            
            ],
            borderWidth: 1
        },



        {
            label: 'Thursday',
            data: thudata,
            backgroundColor: [
                'rgba(5, 99, 132, 0.2)',
                'rgba(54, 162, 25, 0.2)',
                'rgba(255, 206, 86, 0.2)'
                
            ],
            borderColor: [
                'rgba(55, 99, 132, 1)',
                'rgba(54, 12, 235, 1)',
                'rgba(5, 6, 86, 1)'
            
            ],
            borderWidth: 1
        },
    



        {
            label: 'Friday',
            data: fridata,
            backgroundColor: [
                'rgba(5, 99, 132, 0.2)',
                'rgba(54, 162, 25, 0.2)',
                'rgba(255, 206, 86, 0.2)'
                
            ],
            borderColor: [
                'rgba(55, 99, 132, 1)',
                'rgba(54, 12, 235, 1)',
                'rgba(5, 6, 86, 1)'
            
            ],
            borderWidth: 1
        },


        {
            label: 'Saturday',
            data: satdata,
            backgroundColor: [
                'rgba(5, 99, 132, 0.2)',
                'rgba(54, 162, 25, 0.2)',
                'rgba(255, 206, 86, 0.2)'
                
            ],
            borderColor: [
                'rgba(55, 99, 132, 1)',
                'rgba(54, 12, 235, 1)',
                'rgba(5, 6, 86, 1)'
            
            ],
            borderWidth: 1
        },



        {
            label: 'Sunday',
            data: sundata,
            backgroundColor: [
                'rgba(5, 99, 132, 0.2)',
                'rgba(54, 162, 25, 0.2)',
                'rgba(255, 206, 86, 0.2)'
                
            ],
            borderColor: [
                'rgba(55, 99, 132, 1)',
                'rgba(54, 12, 235, 1)',
                'rgba(5, 6, 86, 1)'
            
            ],
            borderWidth: 1
        },
    
    
    
    
    ]
    },
    options: {
        scales: {
            yAxes: [{ ticks:{beginAtZero:true},stacked: true}],
            xAxes: [{stacked: true}]
        }
    }
});
};





const getWeeklyChartData = () => {
    fetch("Aget_weekly_tasks")
      .then((res) => res.json())
      .then((Wresults) => {
        
        const WMONDAY = Wresults.MONDAY;
        const WTUESDAY = Wresults.TUESDAY;
        const WWEDNESDAY = Wresults.WEDNESDAY;
        const WTHURSDAY = Wresults.THURSDAY;
        const WFRIDAY = Wresults.FRIDAY;
        const WSATURDAY = Wresults.SATURDAY;
        const WSUNDAY = Wresults.SUNDAY;
        const [mondata] = [Object.values(WMONDAY)];
        const [tuedata] = [Object.values(WTUESDAY)];
        const [weddata] = [Object.values(WWEDNESDAY)];
        const [thudata] = [Object.values(WTHURSDAY)];
        const [fridata] = [Object.values(WFRIDAY)];
        const [satdata] = [Object.values(WSATURDAY)];
        const [sundata] = [Object.values(WSUNDAY)];
        renderWeeklyChart(mondata,tuedata,weddata,thudata,fridata,satdata,sundata);
        });
  };
  
  document.onload = getWeeklyChartData();
