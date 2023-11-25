document.addEventListener('DOMContentLoaded', function() {
    fetch('http://ec2-3-129-63-152.us-east-2.compute.amazonaws.com:5000/get_monthly_crime_stat')
        .then(response => response.json())
        .then(data => {
            const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
            const labels = data.map(item => monthNames[item.Month - 1]); // Mapping month numbers to month names
            const monthCount = data.map(item => item.Month_Count);
            const monthCountSE = data.map(item => item.Month_Count_SE);
            const monthCountNY = data.map(item => item.Month_Count_NY);

            const ctx = document.getElementById('crimeChart').getContext('2d');
            const crimeChart = new Chart(ctx, {
                type: 'bar', // or 'line' if you prefer
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Total Count',
                        data: monthCount,
                        backgroundColor: 'rgba(255, 99, 132, 0.5)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 1
                    },
                    {
                        label: 'Count in SE',
                        data: monthCountSE,
                        backgroundColor: 'rgba(54, 162, 235, 0.5)',
                        borderColor: 'rgba(54, 162, 235, 1)',
                        borderWidth: 1
                    },
                    {
                        label: 'Count in NY',
                        data: monthCountNY,
                        backgroundColor: 'rgba(75, 192, 192, 0.5)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1
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
