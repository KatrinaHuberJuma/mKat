// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';
console.log("bar chart file connected")
// Bar Chart Example
var bar_ctx = document.getElementById("myBarChart");


$.ajax({
    method: "GET",
    url: "/bar",
    success: function(data){
          console.log(data)
          var chartData = data.data
          var labels = data.labels

          
          console.log(data)
          var myChart = new Chart(bar_ctx, {
                type: 'bar',
                data: {
                  labels: labels,
                  datasets: [{
                    label: "% wrong",
                    backgroundColor: "rgba(2,117,216,1)",
                    borderColor: "rgba(2,117,216,1)",
                    data: chartData,
                  }],
                },
                options: {
                  scales: {
                    xAxes: [{
                      time: {
                        unit: 'month'
                      },
                      gridLines: {
                        display: true
                      },
                      ticks: {
                        maxTicksLimit: 20
                      }
                    }],
                    yAxes: [{
                      ticks: {
                        min: 0,
                        max: 100,
                        maxTicksLimit: 5
                      },
                      gridLines: {
                        display: true
                      }
                    }],
                  },
                legend: {
                  display: true
                }
              }
          })
    }
})