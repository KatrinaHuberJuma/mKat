// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';
console.log("chart-pie-demo.js line 4")
// Pie Chart Example





var ctx = document.getElementById("myPieChart").getContext('2d');



$.ajax({
    method: "GET",
    url: "/pie",
    success: function(data){
        console.log(data)
        var defaultData = data.data
        var labels = data.labels
        console.log("chart-pie-demo.js line 22")
        var myChart = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: labels,
                datasets: [{
                    label: 'my neat string',
                    data: defaultData,
                }]
            }
        })
    },
    errors: function(error_data){
        console.log(error_data)
    }
})
// ____________________________________________________
// var myPieChart = new Chart(ctx, {
//   type: 'pie',
//   data: {
//     labels: ["New Vocab", "Out of Time", "Misunderstood the Question", "Brain Fart"],
//     datasets: [{
//       data: [12.21, 15.58, 11.25, 8.32],
//       backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745'],
//     }],
//   },
// });

