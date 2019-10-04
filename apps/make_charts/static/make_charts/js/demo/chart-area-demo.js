// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Area Chart Example
var line_ctx = document.getElementById("myAreaChart").getContext('2d');
$.ajax({
    method: "GET",
    url: "/line",
    success: function(data){
        console.log(data)
        var chartData = data.data
        var labels = data.labels
        
        console.log("chart-line-demo.js")
        var myChart = new Chart(line_ctx, {
            type: 'line',
            data: {
              labels: labels,
              datasets: [{
                label: "% Correct",
                lineTension: 0,
                backgroundColor: "rgba(2,117,216,0.2)",
                borderColor: "rgba(2,117,216,1)",
                pointRadius: 5,
                pointBackgroundColor: "rgba(2,117,216,1)",
                pointBorderColor: "rgba(255,255,255,0.8)",
                pointHoverRadius: 5,
                pointHoverBackgroundColor: "rgba(2,117,216,1)",
                pointHitRadius: 50,
                pointBorderWidth: 2,
                data: chartData,
              }],
            },
            options: {
              scales: {
                xAxes: [{
                  time: {
                    unit: 'date'
                  },
                  gridLines: {
                    display: true
                  },
                  ticks: {
                    maxTicksLimit: 14
                  }
                }],
                yAxes: [{
                  ticks: {
                    min: 0,
                    max: 100, 
                    maxTicksLimit: 10
                  },
                  gridLines: {
                    color: "rgba(0, 0, 0, .125)",
                  }
                }],
              },
              legend: {
                display: false
              }
            },
        }) 
    },
    errors: function(error_data){
        console.log(error_data)
    }
})