document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('predict-form');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        const message = document.getElementById('message').value;

        try {
            const response = await fetch('http://127.0.0.1:5000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `message=${encodeURIComponent(message)}`,
            });

            const data = await response.json();
            resultDiv.innerHTML = `
                <h1>Prediction Result</h1>
                <p>${data.result}</p>
                <p>Phishing Mail Forecast: ${data.phishing_forecast.toFixed(2)}%</p>
                <p>Legitimate Mail Forecast: ${data.legitimate_forecast.toFixed(2)}%</p>
            `;

        } catch (error) {
            resultDiv.innerHTML = `<p>Error during prediction: ${error.message}</p>`;
        }
    });
});