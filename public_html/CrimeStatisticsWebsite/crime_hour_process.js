document.addEventListener('DOMContentLoaded', function() {
    // Fetch data from the Flask API
    fetch('http://ec2-3-129-63-152.us-east-2.compute.amazonaws.com:5000/get_hourly_crime_stat')
    .then(response => response.json())
    .then(data => {
        const ctx = document.getElementById('crimeChart').getContext('2d');
        const chart = new Chart(ctx, {
            type: 'line', // or 'bar', 'pie', etc.
            data: {
                labels: data.map(item => item.Hour),
                datasets: [{
                    label: 'Total Count',
                    data: data.map(item => item.Hour_Count),
                    borderColor: 'rgb(255, 99, 132)',
                    backgroundColor: 'rgba(255, 99, 132, 0.5)',
                }, {
                    label: 'Count in SE',
                    data: data.map(item => item.Hour_Count_SE),
                    borderColor: 'rgb(54, 162, 235)',
                    backgroundColor: 'rgba(54, 162, 235, 0.5)',
                }, {
                    label: 'Count in NY',
                    data: data.map(item => item.Hour_Count_NY),
                    borderColor: 'rgb(75, 192, 192)',
                    backgroundColor: 'rgba(75, 192, 192, 0.5)',
                }]
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