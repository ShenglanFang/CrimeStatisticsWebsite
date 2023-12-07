document.addEventListener('DOMContentLoaded', function() {
    console.log("labels: ");
    fetch('http://ec2-3-129-63-152.us-east-2.compute.amazonaws.com:5000/crime_weekday_data')
        .then(response => response.json())
        .then(data => {
            const labels = data.map(item => item.Week_Day);
            const weekDayCount = data.map(item => item.Week_Day_Count);
            const weekDayCountSE = data.map(item => item.Week_Day_Count_SE);
            const weekDayCountNY = data.map(item => item.Week_Day_Count_NY);
            console.log("labels: " + labels);

            const ctx = document.getElementById('crimeChart').getContext('2d');
            const crimeChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                            label: 'Total Count',
                            data: weekDayCount,
                            backgroundColor: 'rgba(255, 99, 132, 0.2)',
                            borderColor: 'rgba(255, 99, 132, 1)',
                            borderWidth: 1
                        },
                        {
                            label: 'Count in SE',
                            data: weekDayCountSE,
                            backgroundColor: 'rgba(54, 162, 235, 0.2)',
                            borderColor: 'rgba(54, 162, 235, 1)',
                            borderWidth: 1
                        },
                        {
                            label: 'Count in NY',
                            data: weekDayCountNY,
                            backgroundColor: 'rgba(75, 192, 192, 0.2)',
                            borderColor: 'rgba(75, 192, 192, 1)',
                            borderWidth: 1
                        }
                    ]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        });
});
